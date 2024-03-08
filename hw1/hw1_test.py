import paramiko
import requests
import json

def ssh_command(host, key_path, command):
    """Execute an SSH command and return its output."""

    key = paramiko.RSAKey.from_private_key_file(key_path)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username='root', pkey=key)

    stdin, stdout, stderr = client.exec_command(command)
    output = stdout.read().decode() + stderr.read().decode() 
    client.close()
    return output


def check_web_response(url, expected_content):
    """Check if the web page at url contains the expected content."""
    try:
        response = requests.get(url)
        return expected_content in response.text
    except requests.RequestException:
        return False


def get_inventory_groups():
    """Retrieve the inventory groups from Ansible."""
    ansible_host = "209.151.150.14"  # Assuming this is the Ansible host IP
    ssh_key_path = "C:\\Users\\IMPEG\\Desktop\\privatekey1"

    # Run ansible-inventory command to get inventory information
    output = ssh_command(ansible_host, ssh_key_path, "ansible-inventory --list")

    # Parse the JSON output to get inventory groups
    inventory_data = json.loads(output)
    return inventory_data

def hw1_script():
    ansible_host = "209.151.150.14"
    ssh_key_path = "C:\\Users\\IMPEG\\Desktop\\privatekey1"

    output = ssh_command(ansible_host, ssh_key_path, "ansible-playbook /root/deploy/deploy.yaml")
    print("Output from Ansible playbook:", output)

    inventory = get_inventory_groups()

    # Extract red and blue server IPs
    red_servers = inventory.get('red', {}).get('hosts', [])
    blue_servers = inventory.get('blue', {}).get('hosts', [])

    print("Red Team Servers:", red_servers)
    print("Blue Team Servers:", blue_servers)
