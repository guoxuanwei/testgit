from base_page.basepage import BasePage
import configparser
import os
from selenium import webdriver
from time import sleep
import allure


class LoginPage(BasePage):
    conf = configparser.ConfigParser()
    dir_name = os.path.join(os.path.dirname(__file__), 'page_conf')
    conf.read(dir_name + '/conf.ini', encoding='utf-8')
    url = conf.get('login', 'url')
    username_name = conf.get('login', 'user_name')
    username_value = conf.get('login', 'user_value')
    username = (username_name, username_value)
    password_name = conf.get('login', 'user_name')
    password_value = conf.get('login', 'password_value')
    password = (password_name, password_value)
    login_name_1 = conf.get('login', 'login_name')
    login_value_1 = conf.get('login', 'login_value')
    login_button_1 = (login_name_1, login_value_1)
    login_name_2 = conf.get('login', 'login_button_name')
    login_value_2 = conf.get('login', 'login_button_value')
    login_button_2 = (login_name_2, login_value_2)

    @allure.step('登录功能')
    def login(self, username, password):
        with allure.step('step1:浏览器打开系统地址'):
            self.visit_url(self.url)
        with allure.step('step2:点击登陆按钮进入登录页面'):
            self.click(self.login_button_1)
        with allure.step('step3:输入用户名'):
            self.input(self.username, username)
            sleep(1)
        with allure.step('step4:输入密码'):
            self.input(self.password, password)
            sleep(1)
        with allure.step('step5:点击登录按钮进行登录'):
            self.click(self.login_button_2)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    lp = LoginPage(driver)
    username = 'guoxuanwei222'
    password = 'guoxuanwei222'
    lp.login(username, password)
    sleep(3)
    lp.quit()
