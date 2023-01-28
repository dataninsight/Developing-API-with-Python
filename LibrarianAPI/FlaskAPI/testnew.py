import os
import requests
import json

os.environ['NO_PROXY'] = '127.0.0.1,localhost'

BASE = "http://127.0.0.1:5000/books/"

response = requests.get(BASE + '1') 
print(response.json())
topost = {"title":"title3","content":"content3","id":3}
response = requests.post(BASE + '3', json = topost) 
print(response.json())
# response = requests.get(BASE) 
# print(response.json())
response = requests.get(BASE + '3') 
print(response.json())
topost2 = {"title":"title4","content":"content4","id":4}
response = requests.post(BASE + '4', json = topost2) 
print(response.json())
response = requests.get(BASE + '4') 
print(response.json())
toput = {"title":"titleupdated4","content":"contentupdated4","id":4}
response = requests.put(BASE + '4', json = toput) 
print(response.json())
response = requests.get(BASE + '4') 
print(response.json())
response = requests.delete(BASE + '4') 
print(response.json())
response = requests.get(BASE + '4') 
print(response.json())
