'''
Author: frostysdw
Date: 2025-01-13 08:34:55
LastEditors: frostysdw
LastEditTime: 2025-01-14 15:22:48
FilePath: \ApiAuto\conf\pathsConfig.py
Description: 
'''
import os.path
from configparser import ConfigParser

# 项目目录
base_path = os.path.split(os.path.dirname(__file__))[0]
conf = ConfigParser()  # 需要实例化一个ConfigParser对象
# 需要添加上config.ini的路径，不需要open打开，直接给文件路径就读取，也可以指定encoding='utf-8'
conf.read(f'{base_path}\conf\config.ini', encoding='utf-8')
host = conf['windows']['host']  # 读取host的值，字符串格式
# base_path=conf['windows']['base_path']
# #数据文件目录
data_path = os.path.join(base_path, 'data')
# logs日志文件路径
logs_path = os.path.join(base_path, 'result', 'logs')
# 报告日志文件路径-json
report_json_path = os.path.join(base_path, 'result', 'reports', 'json')
# 报告日志文件路径-html
report_html_path = os.path.join(base_path, 'result', 'reports', 'html')
# 测试用例
case_path = os.path.join(base_path,'tests/login')


if __name__ == '__main__':
    print(__file__)
    h = os.path.dirname(__file__)
    print(h)
    x = os.path.split(h)
    print(x)
    print(base_path)

