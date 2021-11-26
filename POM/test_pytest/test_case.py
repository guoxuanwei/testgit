import pytest
from page_object.login_page import LoginPage
from page_object.register_page import RegisterPage
from page_object.seekgoods_page import SeekGoodsPage
from page_object.addgoods_page import AddGoodsPage
from page_object.cartpage import CartPage


class TestCase:
    goods_num = None

    # 注册
    @pytest.mark.skip('无条件跳过用例')
    @pytest.mark.parametrize('username,password', [('guoxuanwei222', 'guoxuanwei222')])
    def test_01(self, browser, username, password):
        rp = RegisterPage(browser)
        rp.register(username, password)
        text = rp.element_location(('link text', '退出')).text
        assert text == '退出'

    # 登录
    # @pytest.mark.skip
    @pytest.mark.parametrize('username,password', [('guoxuanwei222', 'guoxuanwei222')])
    def test_02(self, browser, username, password):
        lp = LoginPage(browser)
        lp.login(username, password)
        text = lp.element_location(('link text', '退出')).text
        assert text == '退出'

    # 查看商品
    @pytest.mark.parametrize('data', ['苹果'])
    def test_03(self, browser, data):
        sp = SeekGoodsPage(browser)
        sp.seek_goods(data)
        ass = sp.element_location(('xpath', '//h1[contains(text(),"苹果")]')).text
        assert '苹果' in ass

    # 添加购物车
    @pytest.mark.parametrize('data', [5])
    def test_04(self, browser, data):
        ap = AddGoodsPage(browser)
        TestCase.goods_num = str(ap.add_cart(data))
        ap.sleep(1)

    # 校验购物车是否有加入的商品
    def test_05(self, browser):
        cp = CartPage(browser)
        add_num = cp.assert_goods()
        assert add_num == TestCase.goods_num

    # 删除商品
    @pytest.mark.skip
    def test_06(self, browser):
        cp = CartPage(browser)
        all_goods = cp.del_goods()
        assert True == ('苹果' not in all_goods)

    # 清空商品
    @pytest.mark.parametrize('name,value', [('xpath', '//div[contains(@class,"mixed")]/h1')])
    def test_07(self, browser, name, value):
        cp = CartPage(browser)
        cp.del_all_goods()
        ass = cp.element_location((name, value)).text
        assert '您的购物车还是空的' in ass


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_case.py'])
