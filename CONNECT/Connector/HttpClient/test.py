import requests
import json

from Connector.HttpClient.HttpClient import HttpClient

req = HttpClient()
url = 'http://httpbin.org/get'
data = {'key1': 'value1', 'key2': ['value2', 'value3']}
data = json.dumps(data)
print(data, type(data))
# r = requests.get('http://httpbin.org/get', params=payload)
r = req.send_request(method='post', url=url, data=data)
# r = req(method='post', url=url, data=data)

print(r.text)
