import argparse
import os
import requests
import markdown

def fetch_templates(api_url, token):
    """Fetch templates from Zabbix API."""
    headers = {
        "Content-Type": "application/json-rpc"
    }
    payload = {
        "jsonrpc": "2.0",
        "method": "template.get",
        "params": {
            "output": "extend",
        },
        "auth": token,
        "id": 1
    }

    response = requests.post(api_url, json=payload, headers=headers)

    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

    data = response.json()

    if 'error' in data:
        raise Exception(f"API returned an error: {data['error']}")

    return data['result']

def generate_markdown(template):
    """Generate markdown content for a given template."""
    md = f"""# Template: {template['name']}

## Template ID
{template['templateid']}

## Description
{template.get('description', 'No description provided.')}

## Linked Hosts
{', '.join(template.get('hosts', [])) if 'hosts' in template else 'None'}

"""
    return md

def save_markdown(content, output_dir, filename):
    """Save markdown content to a file."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    file_path = os.path.join(output_dir, filename)

    with open(file_path, 'w') as f:
        f.write(content)

    print(f"Saved: {file_path}")

def main():
    parser = argparse.ArgumentParser(description="Fetch Zabbix templates and generate markdown files.")
    parser.add_argument("--api_url", required=True, help="Zabbix API URL.")
    parser.add_argument("--token", required=True, help="Zabbix API authentication token.")
    parser.add_argument("--output_dir", required=True, help="Directory to save the markdown files.")

    args = parser.parse_args()

    try:
        templates = fetch_templates(args.api_url, args.token)

        for template in templates:
            md_content = generate_markdown(template)
            filename = f"template_{template['templateid']}.md"
            save_markdown(md_content, args.output_dir, filename)

        print("All templates have been processed.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()