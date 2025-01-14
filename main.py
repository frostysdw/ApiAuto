'''
Author: frostysdw
Date: 2025-01-14 15:21:44
LastEditors: frostysdw
LastEditTime: 2025-01-14 19:54:42
FilePath: \ApiAuto\main.py
Description: 
'''


# 执行所有测试用例的入口
import os

import pytest
from conf.pathsConfig import report_json_path, report_html_path, pytest_args

if __name__ == '__main__':
	# 使用pytest.main()运行测试
	pytest.main(pytest_args)
	# 使用os.system生成Allure报告
	os.system(f"allure generate {report_json_path} -o {report_html_path} --clean")
	print(f"Allure报告已生成并保存到: {report_html_path}")
    
