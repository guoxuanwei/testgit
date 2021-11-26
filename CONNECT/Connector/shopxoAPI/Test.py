from Connector.HttpClient.HttpClient import HttpClient
import unittest
import configparser
import os
import jsonpath
import json
from Connector.shopxoAPI.assertequal import assertEqual


class Test(unittest.TestCase):
    url = None
    token = None
    userid = None
    openid = None
    productid = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.ht = HttpClient()
        conf = configparser.ConfigParser()
        conf_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'ConFing')
        conf.read(conf_dir + "\conf.ini", encoding='utf-8')
        Test.url = conf.get('shopxoapi', 'URL')
        # print(Test.url)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.ht = HttpClient()
        cls.ht.close_session()

    # 登录接口
    def test01_login(self):
        url = Test.url + '/api/login'
        print(Test.url)
        case_data = {
            'username': 'admin',
            'password': '123456'
        }
        result = self.ht.send_request(method='post', params_type='json', url=url, data=case_data)
        print(result.text, type(result.text))
        dict_data = json.loads(result.text)
        # print(dict_data, type(dict_data))
        Test.token = jsonpath.jsonpath(dict_data, '$..token')[0]
        # print(data)
        self.assertEqual(json.loads(result.text)['httpstatus'], 200, msg='断言失败')
        print(result.url, result.headers)

    # 获取用户信息
    def test02_getuserinfo(self):
        url = Test.url + '/api/getuserinfo'
        header = {'token': Test.token}
        print(header)
        result = self.ht.send_request(url=url, method='get', headers=header)
        print(result.text)
        self.assertEqual(result.json()['httpstatus'], 200, msg='断言失败')
        Test.userid = jsonpath.jsonpath(result.json(), '$..userid')[0]
        Test.openid = jsonpath.jsonpath(result.json(), '$..openid')[0]

    # 获取商品信息接口
    def test03_getproductinfo(self):
        url = Test.url + '/api/getproductinfo'
        case_data = {
            'productid': '8888'
        }
        result = self.ht.send_request(method='get', data=case_data, url=url)
        print(result.text)
        print(result.url)
        self.assertEqual(result.json()['httpstatus'], 200, msg='断言失败')
        self.assertEqual(jsonpath.jsonpath(result.json(), '$..productname')[0], '海南麒麟瓜5斤装', msg='断言失败')
        list1 = jsonpath.jsonpath(json.loads(result.text), '$..productname')
        list2 = ['海南麒麟瓜5斤装']
        self.assertTrue(assertEqual(list1, list2), msg='断言失败')
        Test.productid = result.json()['data'][0]['productid']

    # 添加购物车
    def test04_addcart(self):
        url = Test.url + '/api/addcart'
        header = {'token': Test.token}
        case_data = {
            "openid": Test.openid,
            "productid": Test.productid,
            "userid": Test.userid
        }
        result = self.ht.send_request(url=url, data=case_data, headers=header, method='post', params_type='json')
        print(result.text)
        self.assertEqual(result.json()['httpstatus'], 200, msg='断言失败')


if __name__ == '__main__':
    unittest.mian()
