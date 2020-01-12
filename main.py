import requests

url = 'https://www.virustotal.com/vtapi/v2/file/scan'
params = {'apikey': 'your apikey'}

nome=input("dammi il nome con estensione")
files = {'file': (nome, open(nome, 'rb'))}

response = requests.post(url, files=files, params=params)

print(response.content)
