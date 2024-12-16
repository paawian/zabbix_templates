# -*- coding: utf-8 -*-
"""Zabbix / Monitors Markdown

Parse the result from Zabbix JSON template and generate a
Markdown Document from it.

Usage available with -h|--help argument.

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""
import json
import argparse
import logging

zabbix_items_types = {
    "0": "Zabbix agent",
    "1": "SNMPv1 agent",
    "2": "Zabbix trapper",
    "3": "simple check",
    "4": "SNMPv2 agent",
    "5": "Zabbix internal",
    "6": "SNMPv3 agent",
    "7": "Zabbix agent (active)",
    "8": "Zabbix aggregate",
    "9": "web item",
    "10": "external check",
    "11": "database monitor",
    "12": "IPMI agent",
    "13": "SSH agent",
    "14": "TELNET agent",
    "15": "calculated",
    "16": "JMX agent",
}
logger = logging.getLogger(__name__)


def markdown_table(rows=[]):
    """Generate a markdown table from given list.

    Args:
        rows (List): Data used to generate the table,
                     the first line is the header.

    Returns:
        result (List): None if get failed or Datadog API response
    """
    result = "| " + " | ".join(rows[0].keys()) + " |\n| "
    for h in rows[0].keys():
        result += "------------- |"
    result += "\n"
    for r in rows:
        escaped = [s.translate(str.maketrans({"|": r"\|"})) for s in r.values()]
        result += "| " + " | ".join(escaped) + " |\n"
    return result


def parse_args():
    """ Parse the scripts args
    """
    parser = argparse.ArgumentParser(
        description="""Extract Data from Zabbix
             JSON to put them into a table"""
    )
    # Manage required args
    required = parser.add_argument_group("required arguments")
    # Manage optional args
    required.add_argument(
        "--file",
        "-f",
        dest="file",
        action="store",
        help="File to be used.",
        required=True,
    )
    required.add_argument(
        "--verbose",
        "-v",
        dest="verbose",
        action="store_true",
        help="Activate debug.",
        required=False,
    )
    
    return parser.parse_args()


def return_content_string(content):
    if isinstance(content, list) and not isinstance(content[0], dict):
        return ",".join(content)
    elif isinstance(content, dict) or isinstance(content, list):
        return json.dumps(content) 
    else:
        return str(content)


def generate_list(items=[], keys=["name", "key", "type"]):
    """Generate a list based on given data.

    Args:
        items (List): Data used to generate the dict,
        keys (List): List of the list key.

    Returns:
        result (List): Generated list.
    """
    table = []
    for i in items:
        try:
            row = {
                k: return_content_string(i[k])
                .replace("\n", "<br>")
                .replace("\r", "") if k in i else f"no {k}"
                for k in keys
            }
            table.append(row)
        except:
            logger.exception(f"Failed to process {keys} for item {i}")
    return table


def main(file):
    """Main function of the script."""
    with open(file, "r") as fp:
        obj = json.load(fp)
        if len(obj["zabbix_export"]["templates"]) > 1:
            print("Will not process for more than one template in export")
        template = obj["zabbix_export"]["templates"][0]

        # Init part
        linked_templates_dict = []
        items_dict = []
        triggers_dict = []
        discovery_rules_items_dict = {}
        discovery_rules_triggers_dict = {}
        discovery_rules_dict = []
        macros_dict = []

        # Linked templates part
        linked_templates_dict = []
        if "templates" in template:
            linked_templates_dict = generate_list(template["templates"], keys=["name"])

        # Items part
        if "items" in template:
            items_dict = generate_list(template["items"], keys=["name", "description", "key", "type", "delay"])

            for i in items_dict:
                if i["type"] in zabbix_items_types:
                    i["type"] = zabbix_items_types[i["type"]]
            
            # Extract triggers from items
            for i in template["items"]:
                if "triggers" in i:
                    triggers_dict.extend(generate_list(i["triggers"],keys=["name", "priority", "description", "expression", "tags", "url"]))

        # Macros part
        if "macros" in template:
            macros_dict = generate_list(template["macros"], keys=["macro", "value"])

        # triggers part
        if "triggers" in obj["zabbix_export"]:
            triggers_dict.extend(generate_list(
                obj["zabbix_export"]["triggers"],
                keys=["name", "priority", "description", "expression", "tags", "url"],
            ))
            logger.debug(f"trigger list {triggers_dict}")

        if "discovery_rules" in template:
            discovery_rules_dict = generate_list(
                template["discovery_rules"],
                keys=["name", "key", "description", "type", "lifetime", "delay"],
            )

            for i in discovery_rules_dict:
                if i["type"] in zabbix_items_types:
                    i["type"] = zabbix_items_types[i["type"]]

            for d in template["discovery_rules"]:
                discovery_rules_triggers_dict[d["name"]] = []
                # discovery items part
                if "item_prototypes" in d:
                    items = generate_list(d["item_prototypes"], keys=["name", "description", "key", "type"])

                    for i in items:
                        if i["type"] in zabbix_items_types:
                            i["type"] = zabbix_items_types[i["type"]]

                    for t in [t["trigger_prototypes"] for t in d["item_prototypes"] if "trigger_prototypes" in t]:
                        # trigger item level
                        triggers = generate_list(
                            t,
                            keys=["name", "priority", "description", "expression", "tags", "url"],
                        )

                        discovery_rules_triggers_dict[d["name"]].extend(triggers)
                    discovery_rules_items_dict[d["name"]] = items

                # If trigger at template level
                if "trigger_prototypes" in d:
                # discovery triggers part
                    triggers = generate_list(
                        d["trigger_prototypes"],
                        keys=["name", "priority", "description", "expression", "tags", "url"],
                    )
                    discovery_rules_triggers_dict[d["name"]].extend(triggers)

            # discovery host part TODO

        # Generate full MD
        print("# " + template["name"] + " template description\n")
        print(template["description"] + "\n")

        # Summary
        print("## Summary")
        if len(linked_templates_dict) > 0:
            print("* [templates](#templates)")
        if len(items_dict) > 0:
            print("* [items](#items)")
        if len(macros_dict) > 0:
            print("* [macros](#macros)")
        if len(triggers_dict) > 0:
            print("* [triggers](#triggers)")
        if len(discovery_rules_dict) > 0:
            print("* [discoveries](#discoveries)")
            for d in discovery_rules_items_dict:
                print(
                    """  * [Discovery %s ](#discovery_%s)"""
                    % (d, d.lower().replace(" ", "_"))
                )
        
        # Items
        if len(linked_templates_dict) > 0:
            print('\n<a name="linked templates"></a>\n')
            print("## Linked Templates")
            print(markdown_table(rows=linked_templates_dict))

        # Items
        if len(items_dict) > 0:
            print('\n<a name="items"></a>\n')
            print("## Items")
            print(markdown_table(rows=items_dict))

        # Macros
        if len(macros_dict) > 0:
            print('\n<a name="macros"></a>\n')
            print("## Macros")
            print(markdown_table(rows=macros_dict))

        # Triggers
        if len(triggers_dict) > 0:
            print('\n<a name="triggers"></a>\n')
            print("## Triggers")
            print(markdown_table(rows=triggers_dict))

        # Discovery
        if len(discovery_rules_dict) > 0:
            print('\n<a name="discoveries"></a>\n')
            print("## Discoveries")
            print(markdown_table(rows=discovery_rules_dict))

            # Discovery items
            for d in discovery_rules_items_dict:
                print('\n<a name="discovery_' + d.lower().replace(" ", "_") + '"></a>\n')
                print("## Discovery " + d + "\n")
                print("### Items" + "\n")
                print(markdown_table(rows=discovery_rules_items_dict[d]))
                # If there is triggers
                if len(discovery_rules_triggers_dict) and d in discovery_rules_triggers_dict and len(discovery_rules_triggers_dict[d]) > 0:
                    print("\n### Triggers" + "\n")
                    print(markdown_table(rows=discovery_rules_triggers_dict[d]))


if __name__ == "__main__":
    args = parse_args()
    if args.verbose:
        logging.basicConfig(encoding='utf-8', level=logging.DEBUG)
    main(args.file)