import pytest
import configparser
import os
from Connector.data.read_yaml import load_yaml
from Connector.HttpClient.HttpClient import HttpClient
import jsonpath
import json
import allure


class TestCase:
    conf = configparser.ConfigParser()
    dirname = os.path.join(os.path.dirname(__file__), 'ConFing')
    conf.read(dirname + '/conf.ini')
    url = conf.get('wms', 'URL')

    @allure.feature('用户模块')
    @allure.story('查询用户信息模块--成功场景')
    @allure.title('用例标题：查询用户信息')
    # @allure.severity('blocker')
    @pytest.mark.parametrize('data', load_yaml('./data/data2 nj.yaml'))
    def test_01(self, data, login):
        self.ht = HttpClient()
        self.ht.session.headers.update({'token': jsonpath.jsonpath(login.json(), '$..openid')[0]})
        for i in data.values():
            # print(i)
            for j in i.values():
                for item in j:
                    url = self.url + item['url']
                    with allure.step('step1：发送请求'):
                        result = self.ht.send_request(url=url, method=item['method'], params_type=item['params_type'],
                                                      data=item['test_data'])
                    print(result.text)
                    with allure.step('断言：返回asn_status为1'):
                        assert jsonpath.jsonpath(result.json(), '$..asn_status')[0] == 1


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_case_main.py', '--alluredir', './result', '--clean-alluredir'])
    os.system('allure generate ./result/ -o ./report_allure/ --clean')
