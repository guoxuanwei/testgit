import requests
import time
import json


# url = 'http://httpbin.org/get'
# data = {'key1': 'value1', 'key2': {'key2': 'value2'}}
# result = requests.get(url=url, params=data)
# print(result.text)
# with open('log.txt', 'w+') as f:
#     f.write(result.text)
# print(result)
# print(result.url)
# print(type(result.text), result.text)
# print(result.headers)
# # r = result.json()
# print(type(result.json()), result.json())
# r = json.loads(result.text)
# print('***************************')
# print(type(r), r)


def find(dic_data):
    dic = {'name': '徐小明', 'age': '20'}
    for i in dic.keys():
        if i == dic_data:
            print("存在")
            break
        else:
            print("不存在")
            break


# data = input('请输入')
# find(data)

dict2 = {'key1': [{'name': '小明', 'age': '23'}, {'name1': '小红', 'age1': '20'}]}
li = dict2['key1']
for i in li:
    print(i)
