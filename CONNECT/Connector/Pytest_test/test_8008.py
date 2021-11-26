import configparser
import os
import pytest
from Connector.HttpClient.HttpClient import HttpClient
import jsonpath
from Connector.data.read_yaml import load_yaml


class TestCase:
    @classmethod
    def setup_class(cls):
        conf = configparser.ConfigParser()
        dir_name = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'ConFing')
        print(dir_name)
        conf.read(dir_name + '/conf.ini')
        cls.url = conf.get('wms', 'URL')
        cls.ht = HttpClient()

    @classmethod
    def tear_down(cls):
        cls.ht = HttpClient()
        cls.ht.close_session()

    @pytest.mark.skip('跳过用例')
    def test_01(self):
        self.url = self.url + '/login/'
        self.method = 'post'
        self.params_type = 'json'
        self.case_data = {
            'name': 'admin',
            'password': 123456
        }
        result = self.ht.send_request(url=self.url, method=self.method,
                                      params_type=self.params_type, data=self.case_data)
        print(result.text)
        ass = jsonpath.jsonpath(result.json(), '$..code')[0]
        assert ass == '200'

    @pytest.mark.parametrize('data', load_yaml('../data/data1.yaml'))
    def test_02(self, data):
        for i in data.values():
            print(i)
            for j in i:
                url = self.url + j['url']
                result = self.ht.send_request(
                    url=url, method=j['method'],
                    params_type=j['params_type'],
                    data=j['test_data']
                )
                print(result.text)
                ass = jsonpath.jsonpath(result.json(), j['assert _info']['jsonpath'])[0]
                assert ass == j['assert_info']['expect']


if __name__ == '__main__':
    pytest.main(['-s', '-v'])
