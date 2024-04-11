import requests


# endpoint = 'http://127.0.0.1:8000/api/?abc=abc' 
endpoint = 'http://127.0.0.1:8000/api/'

response = requests.get(endpoint,params={'abc':'abc'}, json={'query':'hello api'})
# json={'query':'hello api'} -> data 
# data={'query':'hello api'} -> form data

print(response.text) # print rax text response

# Http Request -> HTML
# Rest API Http Request -> JSON
# JavaScript Object Notation ~ Python Dict

print(response.status_code)
print(response.json())