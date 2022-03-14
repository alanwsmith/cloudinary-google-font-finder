#!/usr/bin/env python3 

import json
import keyring
import requests
import urllib.parse

api_key = keyring.get_password('alan--google-fonts-api--main', 'alan')
url = f"https://www.googleapis.com/webfonts/v1/webfonts?key={api_key}"

response = requests.get(url)
data = json.loads(response.content)

for item in data['items']:
    item['check_url'] = f"https://res.cloudinary.com/demo/image/upload/w_300/co_red,l_text:{item['family']}_20:Cloudinary%20URL%20Builder/horses.png"
    check_response = requests.get(item['check_url'])
    item['status'] = check_response.status_code
    print(f"Font: {item['family']} - Status: {item['status']}")

with open('font-report.json', 'w') as _report:
    json.dump(data['items'], _report, sort_keys=True, indent=2, default=str)

