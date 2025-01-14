'''
Author: frostysdw
Date: 2025-01-14 16:30:36
LastEditors: frostysdw
LastEditTime: 2025-01-14 19:48:11
FilePath: \ApiAuto\tests\coupon\conftest.py
Description: 
'''

import os
import pytest
from api.loginAPI import LoginAPI
from conf.pathsConfig import report_json_path, report_html_path


# 获取含有token的header
@pytest.fixture(scope='session')
def get_token():
	data = '{"account": "18292417675", "password": "crmeb@123456"}'
	token = LoginAPI().login(data)
	yield token
	print("生成报告")
