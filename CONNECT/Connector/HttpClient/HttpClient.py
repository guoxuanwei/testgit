import requests
import json


class HttpClient:
    def __init__(self):
        self.session = requests.session()

    # 封装发送请求方法
    def send_request(self, method, url, params_type='form', data=None, **kwargs):
        method = method.upper()
        params_type = params_type.upper()
        # 如果data数据为字符串，转化为字典类型
        if isinstance(data, str):
            data = json.loads(data)
        if 'GET' == method:
            response = self.session.request(method=method, url=url, params=data, **kwargs)
            return response
        elif 'POST' == method:
            if 'FORM' == params_type:
                # 传表单数据
                response = self.session.request(method=method, url=url, data=data, **kwargs)
                return response
            else:
                # 传json数据
                response = self.session.request(method=method, url=url, json=data, **kwargs)
                return response
        elif 'PUT' == method:
            if 'FORM' == params_type:
                # 传表单数据
                response = self.session.request(method=method, url=url, data=data, **kwargs)
                return response
            else:
                # 传json数据
                response = self.session.request(method=method, url=url, json=data, **kwargs)
                return response
        elif 'DELETE' == method:
            if 'FORM' == params_type:
                # 传表单数据
                response = self.session.request(method=method, url=url, data=data, **kwargs)
                return response
            else:
                # 传json数据
                response = self.session.request(method=method, url=url, json=data, **kwargs)
                return response
        else:
            raise ValueError(f'request method "{method}" error')

    def __call__(self, method, url, params_type='form', data=None, **kwargs):
        return self.send_request(method, url, params_type, data, **kwargs)

    def close_session(self):
        self.session.close()
