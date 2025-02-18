import requests


url = 'https://endoflife.date/api/macos.json'

headers = {
    "Accept": "application/json"
}

latest = requests.get(url, headers=headers).json()[0]['latest']

with open('version.txt', 'w', encoding='utf-8') as f:
    f.write(latest)