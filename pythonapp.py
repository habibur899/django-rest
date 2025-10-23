import requests

URL = "http://127.0.0.1:8000/aiinfo/"

response = requests.get(URL)
data = response.json()
print(data)
