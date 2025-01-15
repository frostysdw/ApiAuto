'''
Author: frostysdw
Date: 2025-01-13 08:44:49
LastEditors: frostysdw
LastEditTime: 2025-01-15 09:15:14
FilePath: \ApiAuto\core\LogConfig.py
Description: 
'''


import logging
import os.path
import time
from conf.pathsConfig import logs_path


class Logger(object):
   def __init__(self, name, cmdlevel=logging.INFO, fileLevel=logging.DEBUG):
        """
        初始化Logger类
        :param name: 日志器的名称
        :param cmdlevel: 控制台日志级别,默认为INFO
        :param fileLevel: 文件日志级别,默认为DEBUG
        """
        # 定义一个记录器
        self.logger = logging.Logger(name)
        # 定义日志等级
        self.logger.setLevel(fileLevel)
        # 设置日志输出格式及内容
        format_str = "%(asctime)s-%(filename)s[line:%(lineno)s]-%(levelname)s:%(message)s"
        # 设置成日志格式
        format_log = logging.Formatter(format_str)
        # 设置日志文件名及路径
        cur_time = time.strftime("%Y-%m-%d")
        # logFaile=logs_path+cur_time+'.log'
        logFaile = os.path.join(logs_path, f'{cur_time}.log')
        # 获取文件处理
        fh = logging.FileHandler(logFaile, encoding='utf-8')
        fh.setFormatter(format_log)
        # 将文件处理加入记录器
        self.logger.addHandler(fh)
