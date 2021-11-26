import json
from Connector.HttpClient.HttpClient import HttpClient
import unittest
import ddt
import configparser
import os
import jsonpath


@ddt.ddt()
class TestCase(unittest.TestCase):
    conf = configparser.ConfigParser()
    dir_name = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'ConFing')
    conf.read(dir_name + '/conf.ini')
    url = conf.get('wms', 'URL')
    arg_dict = {}

    @classmethod
    def setUpClass(cls) -> None:
        cls.ht = HttpClient()

    # @unittest.skip('无条件跳过用例!')
    # @ddt.file_data('../data/data1.json')
    @ddt.file_data(r'E:\CONNECT\Connector\data\data1.json')
    def test01_login(self, url, method, params_type, test_data, assert_info):
        url = TestCase.url + url
        result = self.ht.send_request(url=url,
                                      method=method,
                                      params_type=params_type,
                                      data=test_data)
        print(result.text)
        self.assertEqual(jsonpath.jsonpath(result.json(), assert_info['jsonpath'])[0],
                         assert_info['expect'], msg='断言失败')

    # @unittest.skip('无条件跳过用例!')
    @ddt.file_data('../data/data2.json')
    def test02(self, data):
        print(data)
        for item in data:
            # 处理json文件中的格式化字符串
            # 将字典转换为json字符串
            item = json.dumps(item)
            item = item % TestCase.arg_dict
            item = json.loads(item)
            url = TestCase.url + item['url']
            result = self.ht.send_request(url=url,
                                          method=item['method'],
                                          params_type=item['params_type'],
                                          data=item['test_data'])
            print(result.text)
            self.assertEqual(jsonpath.jsonpath(result.json(),
                                               item['assert_info']['jsonpath'])[0],
                             item['assert_info']['expect'], msg='断言失败')
            # token = jsonpath.jsonpath(result.json(), '$..openid')[0]
            # 判断数据中是否有更新header字段
            if item.get('update_header'):
                # 获取token字典
                for header_item in item['update_header']:
                    # print(header_item)
                    for key, value in header_item.items():
                        self.ht.session.headers.update({key: jsonpath.jsonpath(result.json(), value)[0]})
            if item.get('set_arg'):
                for set_arg in item['set_arg']:
                    # print(set_arg)
                    for key, value in set_arg.items():
                        dict_value = jsonpath.jsonpath(result.json(), value)[0]
                        TestCase.arg_dict[key] = dict_value

        print(TestCase.arg_dict)


if __name__ == '__main__':
    unittest.mian()
