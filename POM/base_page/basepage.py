'''

常用关键字类

'''
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


# 打开浏览器

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)
        # self.driver.maximize_window()

    # 访问地址
    def visit_url(self, text):
        # self.driver.set_page_load_timeout(10)
        try:
            self.driver.get(text)
        except Exception as e:
            print(f'访问超时{e}')

    # 元素定位
    def element_location(self, loc):
        return self.driver.find_element(*loc)

    # 定位多个元素返回list
    def element_locations(self, loc):
        locs = self.driver.find_elements(*loc)
        return locs

        # 输入操作

    def input(self, loc, text):
        self.element_location(loc).send_keys(text)

    # 点击操作
    def click(self, loc):
        self.element_location(loc).click()

    def clear(self, loc):
        self.element_location(loc).clear()

    # 文本断言
    def assert_text(self, loc, expect):
        try:
            data = self.element_location(loc).text
            assert expect == data
            return True
        except:
            return False

    # 属性断言
    def assert_property(self, loc, text, expect):
        try:
            data = self.element_location(loc).get_property(text)
            assert expect == data
            return True
        except:
            return False

    # 显式等待
    def display_wait(self, loc):
        return WebDriverWait(self.driver, 10, 0.5).until(
            lambda el: self.element_location(loc), message='显示等待查找失败')

    # 进入frame页
    def switch_frame(self, loc):
        frame = self.element_location(loc)
        self.driver.switch_to.frame(frame)

    # 退出frame页
    def close_frame(self):
        self.driver.switch_to.default_content()

    # 获取所有句柄页
    def get_handles(self):
        handles = self.driver.window_handles
        return handles

    # 切换句柄页
    def switch_hand(self, num):
        all_handles = self.get_handles()
        self.driver.switch_to.window(all_handles[num])

    # 关闭句柄页
    def close_handle(self):
        self.driver.close()

    # 刷新当前窗口
    def refresh_window(self):
        self.driver.refresh()

    # 强制等待
    def sleep(self, text):
        sleep(text)

    # 鼠标悬停
    def hover(self, loc):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.element_location(loc)).perform()

    # 关闭浏览器
    def quit(self):
        self.driver.quit()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    bp = BasePage(driver)
    bp.visit_url('https://www.baidu.com')
    # tup = ('xpath', '//input[@name="wd"]')
    # bp.input(tup, '33')
    li = bp.element_locations(('link text', 'a'))
    print(li)
    bp.sleep(5)
    # tup1 = ('xpath', '//input[@id="su"]')
    # bp.click(tup1)
    # bp.element_location(tup).clear()
    # bp.sleep(5)
    # bp.quit()
