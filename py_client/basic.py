import requests


# endpoint = 'http://127.0.0.1:8000/api/?abc=abc' 
endpoint = 'http://127.0.0.1:8000/api/'

response = requests.get(endpoint,params={'abc':'abc'}, json={'query':'hello api'})

print(response.text)
print(response.status_code)
print(response.json())