import time
from hashlib import md5
import requests

showapi_timestamp = time.strftime('%Y%m%d%H%M%S')
# print(showapi_timestamp)
url = 'https://route.showapi.com/64-19'
case_data = {'showapi_appid': '813537',
             'com': 'zhongtong',
             'nu': '75450632975559',
             'showapi_timestamp': showapi_timestamp}
# 以key值进行排序，并拼接所有key value值
# 生成签名
temp = ''
for i in sorted(case_data):
    temp += i + case_data[i]
# print(temp)
# 加盐
temp += '51b70141c5e44937bbb63307ecb74b3d'
# print(temp)

# 根据md5进行签名转换
showapi_sign = md5(temp.encode(encoding='utf-8')).hexdigest()
# print(showapi_sign)
case_data['showapi_sign'] = showapi_sign
print(case_data)

result = requests.post(url=url, data=case_data)
print(result.text)
print(result.url, result)
print(result.request)

result.close()
