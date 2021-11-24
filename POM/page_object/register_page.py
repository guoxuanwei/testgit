from base_page.basepage import BasePage
import configparser
import os
from time import sleep
from selenium import webdriver


class RegisterPage(BasePage):
    conf = configparser.ConfigParser()
    dir_name = os.path.join(os.path.dirname(__file__), 'page_conf')
    conf.read(dir_name + '/conf.ini', encoding='utf-8')
    url = conf.get('register', 'url')
    username = (conf.get('register', 'user_name'),
                conf.get('register', 'user_value'))
    password = (conf.get('register', 'user_name'),
                conf.get('register', 'password_value'))
    agree = (conf.get('register', 'agree_name'),
             conf.get('register', 'agree_value'))
    register_button = (conf.get('register', 'register_name'),
                       conf.get('register', 'register_value'))

    def register(self, username, password):
        self.visit_url(self.url)
        self.input(self.username, username)
        sleep(1)
        self.input(self.password, password)
        sleep(1)
        self.click(self.agree)
        sleep(1)
        self.click(self.register_button)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    rp = RegisterPage(driver=driver)
    rp.register('test666', 'test666')

