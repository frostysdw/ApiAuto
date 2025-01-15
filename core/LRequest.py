'''
Author: frostysdw
Date: 2025-01-13 16:22:23
LastEditors: frostysdw
LastEditTime: 2025-01-15 08:36:41
FilePath: \ApiAuto\core\LRequest.py
Description: 
'''

import requests
from core.ReadFiles import check_json
from core.LogConfig import Logger
from conf.pathsConfig import host

class Lrequest:

    log = Logger(__name__).logger

    def send_request(self, uri, method, header, **kwargs):
        try:
            self.log.debug(f"{host}{uri}")
            self.log.debug(header)

            r = requests.request(
                method, f"{host}{uri}", headers=header, **kwargs)
            self.log.debug(r.request.headers)
            self.log.debug(r.request.method)

        except Exception as e:
            self.log.error(f"出现异常接口请求失败，{e}")

        else:
            self.log.info(f"接口请求成功！{uri}")
            if check_json(r.text):
                return r.json()
            else:
                return r



if __name__ == "__main__":
    json_data = {"account": "18292417675", "password": "crmeb@123456"}
    headers = {"Content-Type": "application/json"}
    h = Lrequest().send_request(
        uri="8081/api/front/login", 
        method="post", 
        header=headers, 
        json=json_data)
    print(h)
