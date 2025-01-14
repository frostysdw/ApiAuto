'''
Author: frostysdw
Date: 2025-01-14 15:21:44
LastEditors: frostysdw
LastEditTime: 2025-01-14 15:21:50
FilePath: \ApiAuto\main.py
Description: 
'''
# 执行所有测试用例的入口
import os

import pytest
from conf.pathsConfig import report_json_path, report_html_path, case_path

if __name__ == '__main__':
	pytest.main([f"{case_path}", "-svx", "--alluredir", report_json_path])
	os.system(f"allure generate {report_json_path} -o {report_html_path} --clean")
