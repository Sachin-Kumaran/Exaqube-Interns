import requests
import json

def fetch_api_directly(api_url, headers=None):

    if headers is None:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {'error': f'Status code: {response.status_code}'}

if __name__ == "__main__":
    api_url = "https://hubspotapiproxy.azurewebsites.net/api/hubdbtable/3958129"
    api_data = fetch_api_directly(api_url)
    with(open('data.json', 'w')) as f:
        f.write(json.dumps(api_data, indent=2))

