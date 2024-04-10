from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.

def api_home(request, *args, **kwargs):

    # echo back GET data 
    body = request.body # this returns a JSON byte stream 
    print("request.body=",body)
    print(request.GET) # url query params as QueryDict object

    data = {}
    try:
        data = json.loads(body) # convert JSON byte stream into python dict
    except:
        pass

    print(request.headers) # request.headers type is HttpHeaders object
    data['params']= dict(request.GET)
    data['headers']= dict(request.headers) # convert the HttpHeaders object into python dict, else error
    print(request.content_type) # return the request content type 

    print("request.body as JSON data:",data)

    return JsonResponse(data)

