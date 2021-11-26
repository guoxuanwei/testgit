import allure
from base_page.basepage import BasePage
import os
import configparser


class CartPage(BasePage):
    conf = configparser.ConfigParser()
    dir_name = os.path.join(os.path.dirname(__file__), 'page_conf')
    conf.read(dir_name + '/conf.ini', encoding='utf-8')
    url = conf.get('cart', 'url')
    # 检验商品是否存在
    goods_info = (conf.get('cart', 'goods_info_name'),
                  conf.get('cart', 'goods_info_value'))
    # 商品数量
    goods_num = (conf.get('cart', 'goods_num_name'),
                 conf.get('cart', 'goods_num_value'))
    # 删除商品按钮
    combo_button = (conf.get('cart', 'del_button_name'),
                    conf.get('cart', 'del_button_value'))
    # 清空商品按钮
    del_all_button = (conf.get('cart', 'del_all_button_name'),
                      conf.get('cart', 'del_all_button_value'))
    # 是否确定
    ascertain_button = (conf.get('cart', 'ascertain_button_name'),
                        conf.get('cart', 'ascertain_button_value'))

    # 检验商品是否存在
    @allure.step('查看购物车商品')
    def assert_goods(self):
        with allure.step('step1：进入购物车页面'):
            self.visit_url(self.url)
        num = self.element_location(self.goods_num).get_attribute('value')
        return num

    # 修改商品数量
    def edit_goods_num(self, num):
        self.visit_url(self.url)
        self.element_location(self.goods_num).clear()
        self.sleep(2)
        self.input(self.goods_num, num)
        return self.element_location(self.goods_num).get_attribute('value')

    # 删除商品
    def del_goods(self):
        self.visit_url(self.url)
        self.click(self.combo_button)
        self.sleep(1)
        self.click(self.ascertain_button)
        self.driver.refresh()
        a_li = self.element_locations(self.goods_info)
        return a_li

    # 删除所有商品
    @allure.step('清空购物车功能')
    def del_all_goods(self):
        with allure.step('step1：进入购物车页面'):
            self.visit_url(self.url)
        with allure.step('step2：点击清空按钮'):
            self.click(self.del_all_button)
            self.sleep(2)
        with allure.step('step3：点击确定按钮'):
            self.click(self.ascertain_button)
            self.sleep(2)
