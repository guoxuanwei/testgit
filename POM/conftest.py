import os
from time import sleep
import pytest
from selenium import webdriver
import allure
from base_page.basepage import BasePage
from page_object.login_page import LoginPage


@pytest.fixture(scope='session', autouse=True)
# @pytest.fixture(scope='session')
def browser():
    """
    全局定义浏览器驱动
    """
    global driver
    # 使用编写的脚本开启浏览器debug模式,调试时可注释
    # os.popen(r"E:\chrome.bat")
    # 实践证明，不可用。。
    # os.system(r'chrome.exe --remote-debugging-port=9222')
    sleep(3)
    # 复用已有浏览器，方便调试
    # options = webdriver.ChromeOptions()
    # options.debugger_address = '127.0.0.1:9222'
    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome()
    with allure.step('打开浏览器'):
        print("成功打开浏览器")

    # 隐式等待10秒
    driver.implicitly_wait(10)
    # 用例执行，返回driver
    yield driver
    # 用例后置，关闭浏览器
    with allure.step('关闭浏览器'):
        driver.quit()
    # driver.close()
    # os.system('taskkill /im chromedriver.exe /F')
    # os.system('taskkill /im chrome.exe /F')
    print("test end!")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        # 成功用例不需处理，去掉
        # extra.append(pytest_html.extras.url("http://www.example.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            with allure.step("添加失败截图"):
                allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)


# 登录
# @pytest.fixture(scope='session', autouse=True)
# @allure.step('登录')
# def login_function(browser):
#     lp = BasePage(driver=driver)
#     lp.visit_url('http://39.98.138.157/shopxo/public/index.php?s=/index/user/logininfo.html')
#     lp.input(('xpath', '//input[contains(@name,"accounts")]'), 'guoxuanwei222')
#     lp.input(('xpath', '//input[contains(@name,"pwd")]'), 'guoxuanwei222')
#     lp.click(('xpath', '//button[contains(text(),"登录")]'))
@allure.step('登录操作')
@pytest.fixture(scope='session', autouse=True)
def login_function(browser):
    lg = LoginPage(browser)
    lg.login('guoxuanwei222', 'guoxuanwei222')
