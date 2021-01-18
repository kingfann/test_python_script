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
        for org in orgs:
            if org['name'] == 'DevNet Sandbox':
                orgid = org['id']
                print(orgid)
except Exception as ex:
    print(ex)

endpoint = f"/organizations/{orgid}/networks"

try:
    response = requests.get(url=f"{base_url}{endpoint}", headers=headers)
    if response.status_code == 200:
        ntws = response.json()
        #print(ntws)
        for ntw in ntws:
           # print(ntw['name'])
            if ntw['name'] == "DevNet Sandbox ALWAYS ON":
                ntwid = ntw['id']
                print(ntwid)           
except Exception as ex:
    print(ex)

endpoint = f"/networks/{ntwid}/devices"

try:
    j = 0 
    response = requests.get(url=f"{base_url}{endpoint}", headers=headers)
    if response.status_code == 200:
        devices = response.json()
        for device in devices:
            print(device['model'], device['serial'])
            print(device)
            j += 1
            print(j)
except Exception as ex:
    print(ex)

