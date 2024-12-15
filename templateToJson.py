import argparse
import requests
import os
import json

def get_arguments():
    parser = argparse.ArgumentParser(description="Export templates from Zabbix one by one to JSON files.")
    parser.add_argument("--api-url", required=True, help="Zabbix API URL (e.g., http://zabbix-server/api_jsonrpc.php)")
    parser.add_argument("--api-key", required=True, help="API key for Zabbix authentication.")
    parser.add_argument("--output-path", required=True, help="Directory where JSON files will be saved.")
    return parser.parse_args()

def zabbix_request(api_url, api_key, method, params=None):
    headers = {'Content-Type': 'application/json-rpc'}
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params or {},
        "auth": api_key,
        "id": 1
    }
    response = requests.post(api_url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()

def export_templates(api_url, api_key, output_path):
    # Ensure the output directory exists
    os.makedirs(output_path, exist_ok=True)

    # Get the list of templates
    response = zabbix_request(api_url, api_key, "template.get", {"output": ["templateid", "name"]})
    if 'result' not in response:
        print("Failed to retrieve templates.")
        return

    templates = response['result']
    print(f"Found {len(templates)} templates.")

    # Export each template and save to a file
    for template in templates:
        template_id = template['templateid']
        template_name = template['name']
        print(f"Exporting template: {template_name} (ID: {template_id})")

        # Export the template
        export_response = zabbix_request(api_url, api_key, "configuration.export", {
            "format": "json",
            "options": {
                "templates": [template_id]
            }
        })

        if 'result' not in export_response:
            print(f"Failed to export template: {template_name}")
            continue

        # Convert the serialized JSON string to a dictionary
        try:
            exported_data = json.loads(export_response['result'])
        except json.JSONDecodeError:
            print(f"Error decoding JSON for template: {template_name}")
            continue

        # Save the properly formatted JSON dictionary to a file
        output_file = os.path.join(output_path, f"{template_name}.json")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(json.dumps(exported_data, indent=4, ensure_ascii=False))

        print(f"Template exported and saved to: {output_file}")

if __name__ == "__main__":
    args = get_arguments()
    try:
        export_templates(args.api_url, args.api_key, args.output_path)
    except Exception as e:
        print(f"An error occurred: {e}")
