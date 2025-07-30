import requests

url = "http://localhost:8000/login.html"

data = {
    "username": "admin",
    "password": "password"
}


response = requests.post(url, data=data)

print("Status Code:", response.status_code)
print("Response Body:", response.text)

if "invalid" in response.text.lower() or "error" in response.text.lower():
    print("Login Failed.")
else:
    print("Login Succeed.")