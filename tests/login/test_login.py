'''
Author: frostysdw
Date: 2025-01-14 14:22:07
LastEditors: frostysdw
LastEditTime: 2025-01-14 15:05:33
FilePath: \ApiAuto\tests\login\test_login.py
Description: 
'''


import allure
import pytest

from api.loginAPI import LoginAPI
from core.GetData import get_login_data


@allure.feature("登录模块接口")
class Test_Login:

	@pytest.mark.parametrize("title,uri,byType,data,res", get_login_data())
	@allure.story("登录接口测试")
	@allure.description("对登录中的接口进行测试")
	@allure.title("{title}")
	def test_login(self, title, uri, byType, data, res):
		loginApi = LoginAPI()
		# print(data)
		r = loginApi.login(data, needToken=False)
		# print(r)
		print("\n", res)
		assert r["code"] == int(res)
