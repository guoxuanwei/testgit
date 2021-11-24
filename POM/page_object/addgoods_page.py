import allure

from base_page.basepage import BasePage
import os
import configparser
from selenium import webdriver


class AddGoodsPage(BasePage):
    conf = configparser.ConfigParser()
    dir_name = os.path.join(os.path.dirname(__file__), 'page_conf')
    conf.read(dir_name + '/conf.ini', encoding='utf-8')
    url = conf.get('add_goods', 'url')
    # 套餐按钮
    combo_button = (conf.get('add_goods', 'combo_button_name'),
                    conf.get('add_goods', 'combo_button_value'))
    # 颜色按钮
    colour_button_ = (conf.get('add_goods', 'colour_button_name'),
                      conf.get('add_goods', 'colour_button_value'))
    # 容量按钮
    capacity_button = (conf.get('add_goods', 'capacity_button_name'),
                       conf.get('add_goods', 'capacity_button_value'))
    # 数量输入框
    num_input = (conf.get('add_goods', 'num_input_name'),
                 conf.get('add_goods', 'num_input_value'))
    # 加入购物车按钮
    add_button = (conf.get('add_goods', 'add_button_name'),
                  conf.get('add_goods', 'add_button_value'))

    @allure.step('添加商品到购物车功能')
    def add_cart(self, num):
        with allure.step('step1：进入商品详情页'):
            self.visit_url(self.url)
        with allure.step('step2：选择商品套餐'):
            self.click(self.combo_button)
            self.sleep(1)
        with allure.step('step3：选择商品颜色'):
            self.click(self.colour_button_)
            self.sleep(1)
        with allure.step('step4：选择商品容量'):
            self.click(self.capacity_button)
            self.sleep(1)
        with allure.step('step5：选择商品数量'):
            self.element_location(self.num_input).clear()
            self.sleep(2)
            self.input(self.num_input, num)
            self.sleep(1)
        with allure.step('step6：点击加入购物车按钮'):
            self.click(self.add_button)
        return num


if __name__ == '__main__':
    driver = webdriver.Chrome()
    ap = AddGoodsPage(driver)
    ap.add_cart(5)
