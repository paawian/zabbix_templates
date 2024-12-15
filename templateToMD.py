import requests
import argparse
import os
import re

# Function to get data from the Zabbix API
def zabbix_api_request(api_url, api_token, method, params):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_token}"
    }
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": 1
    }
    response = requests.post(api_url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json().get("result", {})

# Function to translate item data types
def translate_data_type(data_type):
    data_types = {
        0: "Numeric (float)",
        1: "Character (string)",
        2: "Log",
        3: "Numeric (unsigned)",
        4: "Text"
    }
    return data_types.get(data_type, "Unknown")

# Escape Markdown special characters only when necessary
def escape_markdown(text):
    if not text:
        return ""
    # Escape only characters that interfere with Markdown formatting
    return re.sub(r"([`*_{}\\[\\]()#+-.!|>])", r"\\\1", text)

# Function to resolve item keys in trigger expressions
def resolve_expression(expression, items):
    # Build a dictionary of item IDs to their keys
    item_map = {item["itemid"]: item["key_"] for item in items}
    
    # Replace all item IDs in the expression with their corresponding keys
    for item_id, item_key in item_map.items():
        # Match item IDs embedded within curly braces
        expression = re.sub(rf"\{{{item_id}\}}", item_key, expression)
    
    return expression

# Function to generate Markdown documentation for a template
def generate_markdown(template, api_url, api_token):
    template_id = template["templateid"]
    name = escape_markdown(template["name"])
    description = escape_markdown(template.get("description", "No description provided."))

    # Fetch macros
    macros = zabbix_api_request(api_url, api_token, "usermacro.get", {
        "templateids": template_id
    })

    # Fetch template links
    linked_templates = template.get("templates", [])

    # Fetch items
    items = zabbix_api_request(api_url, api_token, "item.get", {
        "templateids": template_id,
        "output": ["name", "key_", "description", "value_type", "itemid"],
        "selectTags": "extend"
    })

    # Fetch triggers
    triggers = zabbix_api_request(api_url, api_token, "trigger.get", {
        "templateids": template_id,
        "output": ["description", "expression", "priority"],
        "selectDependencies": ["triggerid", "description"],
        "selectTags": "extend"
    })

    # Start building the Markdown content
    md_content = [f"# Template: {name}\n"]
    md_content.append(f"## Overview\n{description}\n")

    # Macros
    md_content.append("## Macros\n")
    if macros:
        md_content.append("| Name | Description | Default Value |")
        md_content.append("|------|-------------|---------------|")
        for macro in macros:
            md_content.append(f"| {escape_markdown(macro['macro'])} | {escape_markdown(macro.get('description', 'No description'))} | {escape_markdown(macro.get('value', 'No default value'))} |")
    else:
        md_content.append("No macros defined.\n")

    # Template links
    md_content.append("## Template Links\n")
    if linked_templates:
        for linked in linked_templates:
            md_content.append(f"- {escape_markdown(linked['name'])}")
    else:
        md_content.append("No linked templates.\n")

    # Items
    md_content.append("## Items\n")
    if items:
        md_content.append("| Name | Description | Data Type | Key | Tags |")
        md_content.append("|------|-------------|-----------|-----|------|")
        for item in items:
            tags = ", ".join([f"{escape_markdown(tag['tag'])}:{escape_markdown(tag['value'])}" for tag in item.get("tags", [])])
            md_content.append(f"| {escape_markdown(item['name'])} | {escape_markdown(item.get('description', 'No description'))} | {translate_data_type(item['value_type'])} | {escape_markdown(item['key_'])} | {tags} |")
    else:
        md_content.append("No items defined.\n")

    # Triggers
    md_content.append("## Triggers\n")
    if triggers:
        md_content.append("| Name | Description | Expression | Severity | Dependencies | Tags |")
        md_content.append("|------|-------------|------------|----------|--------------|------|")
        for trigger in triggers:
            dependencies = ", ".join([escape_markdown(dep["description"]) for dep in trigger.get("dependencies", [])])
            tags = ", ".join([f"{escape_markdown(tag['tag'])}:{escape_markdown(tag['value'])}" for tag in trigger.get("tags", [])])
            severity = ["Not classified", "Information", "Warning", "Average", "High", "Disaster"]
            expression = resolve_expression(trigger["expression"], items)
            md_content.append(f"| {escape_markdown(trigger['description'])} | {escape_markdown(trigger.get('description', 'No description'))} | {escape_markdown(expression)} | {severity[int(trigger['priority'])]} | {dependencies} | {tags} |")
    else:
        md_content.append("No triggers defined.\n")

    return "\n".join(md_content)

# Main function
def main():
    parser = argparse.ArgumentParser(description="Generate Markdown documentation for Zabbix templates.")
    parser.add_argument("api_url", help="Zabbix API URL.")
    parser.add_argument("api_token", help="Zabbix API token.")
    parser.add_argument("output_dir", help="Directory to save Markdown files.")
    args = parser.parse_args()

    # Create output directory if it doesn't exist
    os.makedirs(args.output_dir, exist_ok=True)

    # Fetch templates
    templates = zabbix_api_request(args.api_url, args.api_token, "template.get", {
        "output": ["templateid", "name", "description"],
        "selectTemplates": "extend"
    })

    for template in templates:
        markdown_content = generate_markdown(template, args.api_url, args.api_token)
        output_file = os.path.join(args.output_dir, f"{template['name'].replace(' ', '_')}.md")
        with open(output_file, "w") as f:
            f.write(markdown_content)
        print(f"Generated documentation for template: {template['name']}")

if __name__ == "__main__":
    main()
