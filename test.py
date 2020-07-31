import requests

BASE="http://127.0.0.1:5000/"

response=requests.put(BASE+"videos/1",{"likes":10})
print(response.json())
input()
response=requests.put(BASE+"videos/2",{"likes":10})
print(response.json())