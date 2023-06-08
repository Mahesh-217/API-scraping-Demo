import requests


api=input("Enter API Key")
headers = {'API-Key': api}


response = requests.get('http://127.0.0.1:5000/api/profile', headers=headers)
if response.status_code == 200:

    data = response.json()
    print(data)