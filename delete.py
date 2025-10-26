import requests

URL = "http://127.0.0.1:8000/aicreate/"
data = {'id': 6}
r = requests.delete(URL, json=data)
data = r.json()
print(data)
