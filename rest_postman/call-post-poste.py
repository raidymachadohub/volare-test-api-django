import requests

url = "http://127.0.0.1:8000/api/poste/"

payload = "{\r\n    \"id_poste\": \"P9\",\r\n    \"tipo_poste\": 0\r\n}"
headers = {
    'Authorization': 'token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjIzMjc0NzAwLCJlbWFpbCI6ImFkbWluQHZvbGFyZS5jb20ifQ.FLlQ3JAqVVsV2FF2grVE_o2c8K8QO3eOLJ6E7V8nWm8',
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text.encode('utf8'))
