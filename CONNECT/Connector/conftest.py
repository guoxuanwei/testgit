import jsonpath
import pytest
import configparser
import os
from Connector.data.read_yaml import load_yaml
from Connector.HttpClient.HttpClient import HttpClient
import allure


# 登录操作
@pytest.fixture(scope='session')
# @pytest.fixture(scope='session', autouse=True)
# @pytest.fixture(scope='class')
@allure.step('登录操作')
def login():
    conf = configparser.ConfigParser()
    dirname = os.path.join(os.path.dirname(__file__), 'ConFing')
    conf.read(dirname + '/conf.ini')
    url = conf.get('wms', 'URL')
    for item in load_yaml('./data/data1.yaml'):
        print(item)
        ht = HttpClient()
        url = url + item['url']
        with allure.step('step1：进行登录'):
            result = ht.send_request(url=url, method=item['method'],
                                     params_type=item['params_type'], data=item['test_data'])
        # print(result.text)
        # if item.get('update_header'):
        #     for token in item['update_header']:
        # print(token)
        # for key, value in token.items():
        # print(key, value)
        # ht.session.headers.update({key: jsonpath.jsonpath(result.json(), value)[0]})
        # token = jsonpath.jsonpath(result.json(), '$..openid')[0]
        return result
        # ass = jsonpath.jsonpath(result.json(), item['assert_info']['jsonpath'])[0]
        # with allure.step('assert：登录成功返回code为200'):
        #     if ass == item['assert_info']['expect']:
        #         return True
        #     else:
        #         return False


if __name__ == '__main__':
    login()
