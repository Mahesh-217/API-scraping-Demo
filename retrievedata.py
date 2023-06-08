import requests


response = requests.get('http://127.0.0.1:5000/api/profile')



if response.status_code == 200:

    data = response.json()
    print(data)

else:
    print('Error:', response.status_code)
