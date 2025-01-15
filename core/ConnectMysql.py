'''
Author: frostysdw
Date: 2025-01-12 17:22:07
LastEditors: frostysdw
LastEditTime: 2025-01-14 19:11:18
FilePath: \ApiAuto\ConnectMysql.py
Description: 
'''

import mysql.connector
import logging
from core.LogConfig import Logger

def connect_mysql():
    log = Logger(__name__, logging.INFO, logging.DEBUG)
    try:
        # 建立数据库连接
        connection = mysql.connector.connect(
            host='192.168.220.200',  # 数据库主机地址
            user='root',  # 数据库用户名
            password='123456',  # 数据库密码
            database='crmeb'  # 数据库名称
        )
        log.logger.info("连接成功")  # 连接成功提示
        try:
            # 创建游标对象
            cursor = connection.cursor()
            # 定义查询语句
            query = "SELECT count(*) FROM eb_store_coupon"
            # 执行查询
            cursor.execute(query)
            # 获取所有记录列表
            records = cursor.fetchall()
            result_str = str(records[0][0]) if records else "No records found"
            log.logger.info("获取最后添加的优惠券id:%s", result_str)
        finally:
            # 关闭游标和连接
            if connection.is_connected():
                cursor.close()
                connection.close()
                log.logger.info("关闭连接")
        return(result_str)
    except mysql.connector.Error as e:
        log.logger.error("连接失败: %s", e)


if __name__ == '__main__':  
    h = connect_mysql()
    print(h)