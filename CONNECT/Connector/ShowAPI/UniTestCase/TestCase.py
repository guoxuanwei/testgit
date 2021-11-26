import unittest
from Connector.ShowAPI.ShowAPI import ShowApi
import time
from ddt import ddt, data, unpack, file_data
import jsonpath
from Connector.Method.method import assertListEqual


@ddt
class UnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.expressage = ShowApi()

    # 查询单号
    def test_01(self):
        url = '64-19'
        showapi_timestamp = time.strftime('%Y%m%d%H%M%S')
        case_data = {
            'com': 'zhongtong',
            'nu': '75450632975559',
            'showapi_timestamp': showapi_timestamp}
        result = self.expressage.send_showapi(path=url, method='post', params=case_data)
        print(result.text)
        self.assertEqual(result.json()['showapi_res_code'], 0, msg='断言失败')

    # 查询公司列表
    def test_02(self):
        url = '64-20'
        case_data = {
            'expName': '风'
        }
        result = self.expressage.send_showapi(path=url, params=case_data, method='post')
        print(result.text)
        self.assertEqual(result.json()['showapi_res_code'], 0, msg='断言失败')

    # 单号查询快递公司
    def test_03(self):
        url = '64-21'
        case_data = {
            "nu": "SF1163287169821"
        }
        result = self.expressage.send_showapi(path=url, params=case_data, method='post')
        print(result.text)
        self.assertEqual(result.json()['showapi_res_code'], 0, msg='断言失败')
        self.assertEqual(jsonpath.jsonpath(result.json(), "$..msg")[0], "操作成功!")
        self.assertEqual(jsonpath.jsonpath(result.json(), "$..expName").sort(), ["圆通速递", "顺丰速运", "苏宁快递"].sort())
        self.assertTrue(assertListEqual(jsonpath.jsonpath(result.json(), "$..expName"), ["圆通速递", "顺丰速运", "苏宁快递"]))


if __name__ == '__main__':
    unittest.main()