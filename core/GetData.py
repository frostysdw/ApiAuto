'''
Author: frostysdw
Date: 2025-01-14 11:28:49
LastEditors: frostysdw
LastEditTime: 2025-01-14 14:51:36
FilePath: \ApiAuto\GetData.py
Description: 
'''

import os

from conf.pathsConfig import data_path
from core.ReadFiles import get_test_data



def get_index_data():
    return get_test_data(os.path.join(data_path, 'testdata.xlsx'), 'firstPageAPI')


def get_login_data():
    return get_test_data(os.path.join(data_path, 'testdata.xlsx'), 'login')


if __name__ == '__main__':
    # print(get_index_data())
    for i in get_login_data():
        print(i)
    