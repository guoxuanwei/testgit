import unittest
from Connector.HttpClient.HttpClient import HttpClient
import ddt
import configparser
import os
import jsonpath
import json


@ddt.ddt()
class TestCase(unittest.TestCase):
    conf = configparser.ConfigParser()
    dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'ConFing')
    conf.read(dir + '/conf.ini')
    url = conf.get('wms', 'URL')
    arg_dict = {}

    @classmethod
    def setUpClass(cls) -> None:
        cls.ht = HttpClient()

    @ddt.file_data('../data/data.yaml')
    def test01(self, data):
        for item in data:
            item = json.dumps(item)
            item = item % TestCase.arg_dict
            item = json.loads(item)
            print(item)
            url = TestCase.url + item['url']
            result = self.ht.send_request(url=url, method=item['method'],
                                          params_type=item['params_type'], data=item['test_data'])
            print(result.text)
            self.assertEqual(jsonpath.jsonpath(result.json(),
                                               item['assert_info']['jsonpath'])[0],
                             item['assert_info']['expect'])
            if item.get('update_header'):
                for token in item['update_header']:
                    # print(token)
                    for key, value in token.items():
                        print(key, value)
                        self.ht.session.headers.update({key: jsonpath.jsonpath(
                            result.json(), value)[0]})
            if item.get('set_arg'):
                for asn_code in item['set_arg']:
                    for key, value in asn_code.items():
                        TestCase.arg_dict[key] = jsonpath.jsonpath(result.json(), value)[0]
        print(TestCase.arg_dict)


if __name__ == '__main__':
    unittest.mian()
