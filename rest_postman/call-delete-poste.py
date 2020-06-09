import requests

url = "http://127.0.0.1:8000/api/poste/P8/"

payload = {}
headers = {
    'Authorization': 'token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjIzMjc0NzAwLCJlbWFpbCI6ImFkbWluQHZvbGFyZS5jb20ifQ.FLlQ3JAqVVsV2FF2grVE_o2c8K8QO3eOLJ6E7V8nWm8'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text.encode('utf8'))
