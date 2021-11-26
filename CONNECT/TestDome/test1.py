# @Time : 2021/6/29 21:22
# @Author : 伯通
# @File : request_base.py
import requests
import json

# requests.get('https://api.github.com/events')
# requests.post('http://httpbin.org/post', data={'key': 'value'})

# 传递url参数  -  GET 请求
payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get('http://httpbin.org/get', params=payload)
print(r.url)

# 响应内容
r = requests.get('https://api.github.com/events')
print(type(r.text))

# JSON响应内容
r = requests.get('https://api.github.com/events')
json_data = r.json()
print(type(json_data))

# 通过json模块来进行转换
r = requests.get('https://api.github.com/events')
# 将JSON字符串转换成python数据类型
json_data = json.loads(r.text)
print(type(json_data))

# 稍微复杂的POST请求
# 在调用post方法时，给data关键字参数赋值python字典对象,相当于提交表单数据
# payload = {'key1': 'value1', 'key2': 'value3'}
# r = requests.post("http://httpbin.org/post", data=payload)
# print(r.text)

# 在调用post方法时，给json关键字参数赋值python字典对象
payload = {"password": "123456", "name": "admin"}
# r = requests.post("http://127.0.0.1:8008/login/", data=payload)
r = requests.post(url="http://127.0.0.1:8008/login/", json=payload)
print('---------------------')
print(r.text)

# 在调用post方法时，给data关键字参数赋值json字符串
payload = {"password": "123456", "name": "admin"}
# 将字典转换成json字符串
payload_json = json.dumps(payload)
print(type(payload_json))
r = requests.post("http://127.0.0.1:8008/login/", data=payload_json)
print(r.text)
print(r.status_code)

# 设置请求的请求头
payload = {'key1': 'value1', 'key2': 'value3'}
headers = {"Content-Type": "application/json"}
r = requests.post("http://httpbin.org/post", json=payload, headers=headers)
print(r.text)
