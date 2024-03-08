import requests

def test_access(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return "Access successful"
        else:
            return f"Access denied or error encountered: {response.status_code}"
    except requests.ConnectionError:
        return "Failed to connect"

# Replace with your Nginx server URL or IP
nginx_url = 'http://209.151.154.45:9444' # or 'http://<your-nginx-server-ip>'

print(test_access(nginx_url))
