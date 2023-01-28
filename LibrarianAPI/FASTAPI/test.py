#!/bin/sh
'''
python -m pip install requests
venv/Librarian/consumingbasicLibrarian.py
'''
import os 
import requests
import json
os.environ['NO_PROXY'] = '127.0.0.1,localhost'
# api_url = "https://jsonplaceholder.typicode.com/todos/1"
api_url = "http://127.0.0.1:8000/books"

topost = {"title": "Book3", "content": "Content3", "id": 3}
response = requests.post(api_url, json=topost)
print(response.json())
print(response.status_code)
response.status_code

topost = {"title": "Book4", "content": "Content4", "id": 4}
response = requests.post(api_url, json=topost)
print(response.json())
print(response.status_code)
response.status_code

response = requests.get(api_url)
# print(response.content)
print(response.json())
print(response.status_code)
# print(response.headers["Content-Type"])

api_url2 = "http://127.0.0.1:8000/books/4"
toput = {"title": "BookUpdated4", "content": "ContentUpdated4"}
response = requests.put(api_url2, json=toput)
print(response.json())
print(response.status_code)

response = requests.get(api_url)
# print(response.content)
print(response.json())
print(response.status_code)
# print(response.headers["Content-Type"])

# api_url3 = "https://jsonplaceholder.typicode.com/todos/10"
# todo = {"title": "Mow lawn"}
# response = requests.patch(api_url, json=todo)
# response.json()

response = requests.delete(api_url2)
print(response.json())
print(response.status_code)

response = requests.get(api_url)
# print(response.content)
print(response.json())
print(response.status_code)
