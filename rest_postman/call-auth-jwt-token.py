import requests

url = "http://127.0.0.1:8000/api/auth/"

payload = "{\r\n    \"username\": \"admin\",\r\n    \"password\": \"volare123\"\r\n}"
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text.encode('utf8'))
