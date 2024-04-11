import requests

endpoint= 'http://127.0.0.1:8000/api/products/'

data = { 'price':'123.01'}
response = requests.post(endpoint, json=data)

print(response.json())