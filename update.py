import requests
import json

URL = "http://127.0.0.1:8000/aicreate/"

data = {
    'id': 1,
    'teacher_name': 'Alice',
    'course_name': 'Machine Learning',
    'course_duration': 12,
    'seat': 50
}

json_data = json.dumps(data)
r = requests.put(URL, json_data)
data = r.json()
print(data)

