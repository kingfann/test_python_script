import requests
import json

merakikey = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
base_url = 'https://api.meraki.com/api/v0'
endpoint = '/organizations'

headers = {
    'X-Cisco-Meraki-API-Key': merakikey
}

try:
    response = requests.get(url=f"{base_url}{endpoint}", headers=headers)
    if response.status_code == 200:
        #   print(response.json())
        orgs = response.json()
        print(orgs)
        for org in orgs:
            if org['name'] == 'DevNet Sandbox':
                orgid = org['id']
                print(orgid)
except Exception as ex:
    print(ex)


