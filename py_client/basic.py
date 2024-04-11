import requests


# endpoint = 'http://127.0.0.1:8000/api/?abc=abc' 
endpoint = 'http://127.0.0.1:8000/api/'

response = requests.post(endpoint, params={'abc':'abc'}, json={'title':'mock product',
                                                               'content':'hello api'})
# json={'query':'hello api'} -> data 
# data={'query':'hello api'} -> form data

# print(response.headers)
print(response.text) # print rax text response

# Http Request -> HTML
# Rest API Http Request -> JSON
# JavaScript Object Notation ~ Python Dict


print(response.status_code)
print(response.json())