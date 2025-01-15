'''
Author: frostysdw
Date: 2025-01-14 16:43:25
LastEditors: frostysdw
LastEditTime: 2025-01-14 19:16:12
FilePath: \ApiAuto\tests\coupon\test_coupon.py
Description: 
'''


# encoding=utf-8
import json
import allure
import pytest

from api.couponAPI import CouponAPI
from core.ConnectMysql import connect_mysql
from core.GetData import get_coupon_save_data, get_coupon_receive_data


@allure.epic("接口测试")
@allure.feature("优惠券模块接口")
class Test_Coupon:

    @pytest.mark.parametrize("title,uri,byType,data,res", get_coupon_save_data())
    @allure.story("优惠券添加接口测试")
    @allure.description("对优惠券的接口进行测试")
    @allure.title("{title}")
    def test_coupon_save(self, title, uri, byType, data, res):
        print("\n-----------")
        coupon = CouponAPI()
        # 后端需直接获取token 
        token = "939299718928478dbc85956a69dd9299"
        header = {
            "Content-Type": "application/json;charset=UTF-8",
            "authori-zation": token}
        r = coupon.Coupon_Save(uri, byType, header, data)
        # print(r)
        assert r["code"] == int(res)

    
    @pytest.mark.parametrize("title,uri,byType,data,res", get_coupon_receive_data())
    @allure.story("优惠券领取接口测试")
    @allure.description("对优惠券的接口进行测试")
    @allure.title("{title}")
    def test_coupon_receive(self, title, uri, byType, data, res, get_token):
        print("\n-----------")
        coupon = CouponAPI()
        data_dict = json.loads(data)
        coupon_Id = connect_mysql()
        data_dict.update({"couponId": coupon_Id})
        data_json = json.dumps(data_dict)
        # print(data_json)
        header = {
            "Content-Type": "application/json;charset=UTF-8",
            "authori-zation": get_token}
        r = coupon.Coupon_Receive(
            uri, byType, header, data_json)
        # print(r)
        assert r["code"] == int(res)
