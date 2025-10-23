import json

import requests

URL = "http://127.0.0.1:8000/aicreate/"
data = {
    'teacher_name': 'Mejbah',
    'course_name': 'Deep Learning',
    'course_duration': 10,
    'seat': 100
}

json_data = json.dumps(data)
r = requests.post(URL, json_data)
data = r.json()
print(data)
