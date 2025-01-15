'''
Author: frostysdw
Date: 2025-01-14 16:45:05
LastEditors: frostysdw
LastEditTime: 2025-01-14 16:59:24
FilePath: \ApiAuto\api\couponAPI.py
Description: 
'''


from core.LRequest import Lrequest


class CouponAPI(Lrequest):
	# 添加优惠券
	def Coupon_Save(self, uri, method, header, data):
		return self.send_request(uri, method, header, data=data)

	# 领取优惠券
	def Coupon_Receive(self, uri, method, header, data):
		return self.send_request(uri, method, header, data=data)
