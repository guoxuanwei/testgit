import unittest
from HTMLTestReportCN import HTMLTestRunner
# from HTMLTestRunner import HTMLTestRunner
import os
import time
from Connector.SendEmail.sendemail import SendEmail

dirname = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'cema8008')
print(dirname)
suite = unittest.defaultTestLoader.discover(start_dir=dirname, pattern='W*.py')
# runner = unittest.TextTestRunner(verbosity=2)
# runner.run(suite)
report_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'report')
now_time = time.strftime('%Y-%m-%d %H-%M-%S')
now = os.path.join(report_dir, now_time)
os.mkdir(now)
report_name = now + '\\report.html'
print(report_name)
title = 'WMS仓库'
description = '接口冒烟测试'
if not os.path.exists(report_dir):
    os.mkdir(report_dir)
with open(report_name, 'wb') as file:
    runner = HTMLTestRunner(stream=file, title=title,
                            tester='郭宣伟',
                            description=description, verbosity=2)
    runner.run(suite)
send = SendEmail()
send.send_email(report_name)
