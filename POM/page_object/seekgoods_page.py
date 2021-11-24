import allure
from base_page.basepage import BasePage
import os
import configparser
from selenium import webdriver


class SeekGoodsPage(BasePage):
    conf = configparser.ConfigParser()
    dir_name = os.path.join(os.path.dirname(__file__), 'page_conf')
    conf.read(dir_name + '/conf.ini', encoding='utf-8')
    url = conf.get('seek_goods', 'url')
    seek_url = conf.get('seek_goods', 'url')
    input_name = conf.get('seek_goods', 'input_box_name')
    input_value = conf.get('seek_goods', 'input_box_value')
    input_box = (input_name, input_value)
    seek_button_name = conf.get('seek_goods', 'seek_button_name')
    seek_button_value = conf.get('seek_goods', 'seek_button_value')
    seek_button = (seek_button_name, seek_button_value)
    click_goods_name = conf.get('seek_goods', 'click_goods_name')
    click_goods_value = conf.get('seek_goods', 'click_goods_value')
    click_goods = (click_goods_name, click_goods_value)

    @allure.step('查询商品')
    def seek_goods(self, text):
        with allure.step('进入搜索商品页'):
            self.visit_url(self.url)

        with allure.step('输入商品：'):
            self.input(self.input_box, text)

        with allure.step('点击搜索按钮'):
            self.click(self.seek_button)
        with allure.step('点击商品，进入商品详情页'):
            self.click(self.click_goods)
            self.switch_hand(1)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    sp = SeekGoodsPage(driver)
    sp.seek_goods('苹果')
    sp.sleep(3)
    ass = sp.driver.title
    print(ass)
