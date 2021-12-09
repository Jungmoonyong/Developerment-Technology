import requests

url = 'https://m00ny.com'

response = requests.get(url)

print(response.status_code)
print(response.text)