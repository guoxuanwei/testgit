import unittest
import warnings
import json
from Connector.HttpClient.HttpClient import HttpClient
import configparser
import os
import jsonpath
from Connector.MySql.MySqlHelper import MySql


class Test(unittest.TestCase):
    URL = None

    @classmethod
    def setUpClass(cls) -> None:
        Test.mysql = MySql()
        cls.ht = HttpClient()
        conf = configparser.ConfigParser()
        dirname = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'ConFing')
        conf.read(dirname + "/conf.ini")
        Test.URL = conf.get('apidemo', 'URL')
        warnings.simplefilter('ignore', ResourceWarning)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.ht = HttpClient()
        cls.ht.close_session()
        Test.mysql = MySql()
        sql1 = 'delete from permission_userprofile where username="guo1234"'
        print(Test.mysql.delete(sql1))

    # 用户登录
    def test01_login(self):
        url = Test.URL + '/admin/login/'
        case_data = {
            'username': 'admin',
            'password': '123456'
        }
        result = self.ht.send_request(url=url, method='post', params_type='json', data=case_data)
        print(result.text)
        token = jsonpath.jsonpath(result.json(), '$..token')[0]
        self.assertEqual(result.json()['code'], 200, msg='断言失败')
        self.ht.session.headers.update({"Authorization": "Bearer " + token})
        # print(self.ht.session.headers)

    # 创建用户
    def test02_createuser(self):
        url = Test.URL + '/admin/permission/user/'
        case_data = {
            'username': 'guo1234',
            'name': '123456'
        }
        result = self.ht.send_request(url=url, method='post', params_type='json', data=case_data)
        print(result.text)
        self.assertEqual(json.loads(result.text)['code'], 200, msg='断言失败')
        sql = "SELECT id FROM permission_userprofile where username='guo1234'"
        ret = Test.mysql.get_one(sql)
        print(ret[0])
        self.assertTrue(ret[0], msg='断言失败')


if __name__ == '__main__':
    unittest.mian()
