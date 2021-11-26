import os
import allure
import pytest
from page_object.login_page import LoginPage
from page_object.register_page import RegisterPage
from page_object.seekgoods_page import SeekGoodsPage
from page_object.addgoods_page import AddGoodsPage
from page_object.cartpage import CartPage
import time
from selenium import webdriver


class TestCase:
    goods_num = None

    # 登录
    # @pytest.mark.skip
    @allure.feature('用户登录模块')
    @allure.story('登录成功场景')
    @allure.title('用例名称：用户登录--登录成功')
    @allure.issue('http://www.baidu.com')  # bug地址
    @allure.testcase('http://www.baidu.com')  # 用例地址
    @allure.severity('blocker')
    @pytest.mark.parametrize('username,password', [('guoxuanwei222', 'guoxuanwei222')])
    def test_01(self, browser, username, password):
        """
           用例描述：登录-登录成功
           0.浏览器打开系统地址
           1.进入登录界面
           2.输入用户名及密码
           3.点击登录按钮
           assert：登录成功，页面存在退出按钮
        """
        lp = LoginPage(browser)
        # lp.login(username, password)
        with allure.step('assert：断言：登录成功后出现退出按钮'):
            text = lp.element_location(('link text', '退出')).text
            assert text == '退出'

    # 查看商品
    # @pytest.mark.skip()
    @allure.feature('购物车管理模块')
    @allure.story('添加商品场景')
    @allure.title('用例名称：添加商品至购物车')
    @allure.issue('http://www.baidu.com')  # bug地址
    @allure.testcase('http://www.baidu.com')  # 用例地址
    @allure.severity('blocker')
    @pytest.mark.parametrize('data,data1', [('苹果', 5)])
    def test_02(self, browser, data, data1):
        """
              用例描述：查看商品
              0.输入商品名称
              1.点击查询按钮
              2.点击查询出的商品
              assert：添加的商品存在购物车且数量正确
        """
        # 查询商品
        sp = SeekGoodsPage(browser)
        sp.seek_goods(data)
        ass = sp.element_location(('xpath', '//h1[contains(text(),"苹果")]')).text
        # 添加商品
        ap = AddGoodsPage(browser)
        TestCase.goods_num = str(ap.add_cart(data1))
        ap.sleep(1)
        # 校验购物车是否存在商品
        cp = CartPage(browser)
        add_num = cp.assert_goods()
        with allure.step('断言：添加的商品存在购物车且数量正确'):
            assert add_num == TestCase.goods_num

    # 清空购物车
    @allure.feature('购物车模块')
    @allure.story('清空购物车场景')
    @allure.title('用例名称：清空购物车所有商品')
    @allure.issue('http://www.baidu.com')  # bug地址
    @allure.testcase('http://www.baidu.com')  # 用例地址
    @allure.severity('blocker')
    @pytest.mark.parametrize('name,value', [('xpath', '//div[contains(@class,"mixed")]/h1')])
    def test_03(self, browser, name, value):
        """
              用例描述：清空购物车所有商品
              0.进入购物车页面
              1.点击清空按钮
              2.点击确定按钮
              assert：购物车没有商品
        """
        cp = CartPage(browser)
        cp.del_all_goods()
        with allure.step('断言：购物车已清空'):
            ass = cp.element_location((name, value)).text
        assert '您的购物车还是空的' in ass


if __name__ == '__main__':
    pytest.main(['test_case_pytest.py',
                 '--alluredir', './result',
                 '--allure-severities', 'blocker',
                 '--clean-alluredir',
                 '--maxfail', '5', '--reruns', '1'])
    how_time = time.strftime('%Y-%m-%d--%H-%M-%S')
    # os.system('allure serve result')
    os.system('allure generate ./result/ -o ./result-allure{}/ --clean'.format(how_time))
