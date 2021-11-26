from Connector.HttpClient.HttpClient import HttpClient
from hashlib import md5
import configparser
import os

"""
showAPI
接口操作行为封装

"""


class ShowApi:
    # 发送showapi平台的接口
    API_URL = "https://route.showapi.com"

    def __init__(self, showapi_appid=None, showapi_key=None):
        conf = configparser.ConfigParser()
        # dirname = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'ConFig')
        conf.read(r'E:\CONNECT\Connector\ConFing\conf.ini', encoding='utf-8')
        if showapi_appid is None:
            self.showapi_appid = conf.get('showapi', 'SHOWAPI_APPID')
        else:
            self.showapi_appid = showapi_appid
        if showapi_key is None:
            self.showapi_key = conf.get('showapi', 'SECRET_ID')
        else:
            self.showapi_key = showapi_key
        """
        showapi_appid  用户ID
        showapi_key  登录秘钥
        """

    # 生成签名
    # 以key值进行排序，并拼接所有key
    # value值
    def create_sign(self, data=None):
        st = ''
        for i in sorted(data):
            st += i + data[i]
        showapi_sign = st + self.showapi_key
        showapi_sign = md5(showapi_sign.encode(encoding='utf-8')).hexdigest()
        return showapi_sign

    # 发送查询单号接口
    def send_showapi(self, path, method, params):
        params['showapi_appid'] = self.showapi_appid
        showapi_sign = self.create_sign(data=params)
        params['showapi_sign'] = showapi_sign
        try:
            request = HttpClient()
            # 拼接接口路径
            url = self.API_URL + '/' + path
            request.send_request(method=method, url=url, params_type='form', params=params)
            request.close_session()
            return request.send_request(method=method, url=url, params_type='form', params=params)
        except BaseException as e:
            print(f'调用showapi接口失败：{e}')
