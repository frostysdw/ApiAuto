'''
Author: frostysdw
Date: 2025-01-14 11:28:49
LastEditors: frostysdw
LastEditTime: 2025-01-14 17:36:00
FilePath: \ApiAuto\core\GetData.py
Description: 
'''

import os

from conf.pathsConfig import data_path
from core.ReadFiles import get_test_data


def get_coupon_save_data():
    return get_test_data(os.path.join(data_path, 'testdata.xlsx'), 'CouponSave')
def get_coupon_receive_data():
    return get_test_data(os.path.join(data_path, 'testdata.xlsx'), 'CouponReceive')
def get_login_data():
    return get_test_data(os.path.join(data_path, 'testdata.xlsx'), 'login')


if __name__ == '__main__':
    # print(get_index_data())
    for i in get_coupon_save_data():
        print(i)
    