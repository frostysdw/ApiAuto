'''
Author: frostysdw
Date: 2025-01-13 08:44:25
LastEditors: frostysdw
LastEditTime: 2025-01-14 11:31:45
FilePath: \ApiAuto\core\ReadFiles.py
Description: 
'''


import json
import pandas as pd
import logging
from core.LogConfig import Logger


log = Logger(__name__, logging.INFO, logging.DEBUG)

def get_test_data(filename, sheetname):
    """
    从指定的Excel文件和工作表中获取测试数据。

    参数:
    filename -- Excel文件的名称。
    sheetname -- 工作表的名称。

    返回:
    包含工作表数据的列表，每行数据作为一个元组。
    如果文件读取或sheet获取失败,将返回空列表。
    """
    # 初始化一个空列表来存储数据
    datas_list = []
    try:
        # 使用pandas读取Excel文件中的指定工作表
        df = pd.read_excel(filename, sheet_name=sheetname)
        # 将DataFrame转换为列表，每行数据作为一个元组
        datas_list = [tuple(row) for row in df.values]
    except Exception as e:
        # 打印失败的日志
        log.logger.debug(f"获取sheet文件失败{filename}:{sheetname}:{e}")
    else:
        # 打印成功的日志
        log.logger.info(f"获取sheet文件成功{datas_list}")
        return datas_list


def check_json(data):
    """
    检查输入的数据是否为JSON格式。

    此函数尝试将输入的数据转换为JSON格式字符串,如果转换过程中发生异常,
    则说明数据不是有效的JSON格式,函数将记录错误日志并返回False; 如果转换成功,
    则记录成功日志并返回True。

    参数:
    - data: 待检查的数据。

    返回值:
    - True: 如果数据是有效的JSON格式。
    - False: 如果数据不是有效的JSON格式。
    """
    try:
        # 尝试将数据转换为JSON格式字符串
        json.dumps(data, indent=4, ensure_ascii=False)
    except Exception as e:
        # 如果发生异常，记录错误日志并返回False
        log.logger.debug(f"非json格式数据!{e}")
        return False
    else:
        # 如果转换成功，记录成功日志并返回True
        log.logger.info("返回值是json格式数据")
        return True
