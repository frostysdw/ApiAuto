'''
Author: frostysdw
Date: 2025-01-14 14:23:11
LastEditors: frostysdw
LastEditTime: 2025-01-14 16:38:35
FilePath: \ApiAuto\loginAPI.py
Description: 
'''


import json
from core.LRequest import Lrequest


class LoginAPI(Lrequest):

    def login(self, data, uri="8081/api/front/login", method='POST',  needToken=True):
        loginHeader = {
            "Content-Type": "application/json;charset=UTF-8"}
        r = self.send_request(uri, method, loginHeader, data=data)
        if needToken == True:
            return r["data"]["token"]
        else:
            return r


if __name__ == '__main__':
    login = LoginAPI()
    data = '{"account": "18292417675", "password": "crmeb@123456"}'
    # data_json = json.dumps(data)
    print(data)
    # print(data_json)
    h = login.login(data, needToken=False)
    h_data = json.dumps(h, indent=4, ensure_ascii=False)
    print(h)
