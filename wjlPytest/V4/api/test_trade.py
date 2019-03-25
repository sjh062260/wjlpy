#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

"""
@author:sjh
@time:2018/5/25 10:35
"""
import pytest
import requests
import orderEnum

class TestTrade:


    trade_host="http://192.168.122.116:8603/trade"
    groupId="1001"
    tenantId="4002"
    storeId = "4021181010001"
    memberId= "12000118150000001"
    # orderMoldEnum = {
    #     "order":1,
    #     "refund":2
    # }
    # orderSourceEnum = {
    #     "WX":1,
    #     "SHZS":2,
    #     "PARKING":3,
    #     "POS":4,
    #     "WOP":5,
    #     "OTHER":6
    # }
    # orderStatusEnum = {
    #     "nopayment":1,
    #     "success":2,
    #     "close":3
    # }
    # orderTypeEnum = {
    #     "COUPON":1,
    #     "CONSUME":2,
    #     "PARKING":3,
    #     "SCAN":4
    # }




    def test_create_order(self):
        # 创建订单
        orderParam = {
            "group_id" : self.groupId,
            "tenant_id":self.tenantId,
            "store_id":self.storeId,
            "member_id":self.memberId,
            "order_type":2,
            "order_channel":9,
            "total_fee":2000,
            "act_total_fee":2000,
            "member_credit_value":20
        }
        url = self.trade_host+"/OrderClient/createOrder"
        payload = orderParam
        print(payload)
        # resp = requests.post(url,data=payload)
        resp = requests.get(url,params=payload)
        print(resp.text)
        assert resp.status_code == 200


    # def test_upload_order(self):
    #     #上传订单
    #     return
    def test_findbyNo(self):
        # 查询订单
        url = self.trade_host+ '/OrderClient/findByNo'
        payload ={
            "groupId":self.groupId,
            "tenantId":self.tenantId,
            "no":"23213",
            "queryKeyType":"ORDER_NO"
        }
        resp = requests.post(url,data = payload)
        print(resp.text)
        assert resp.status_code == 200
    #     return
    # def test_findListByNos(self):
    #     #批量查询订单
    #     return
    # def test_findDetailByNo(self):
    #     #查询详情
    #     return
    # def test_findMaxOutOrderNo(self):
    #     # 查询最大外部单号
    #     return
    # def test_findOrderPage(self):
    #     #分页查询订单
    #     return
    # def test_findOrderList(self):
    #     #查询订单列表
    #     return
    # def test_isFirstOrder(self):
    #     #判断是否首单
    #     return
    # def test_closeOrder(self):
    #     #关闭订单
    #     return
    # def test_deleteOrder(self):
    #     # 逻辑删除订单
    #     return
    # def test_pay(self):
    #     #交易支付
    #     return
    # def test_paySuccessCallBack(self):
    #     #支付成功回调
    #     return
    # def test_refund(self):
    #     #退单
    #     return
    # def test_refundSuccessCallBack(self):
    #     #退款成功回调
    #     return
    # def test_findRefundPager(self):
    #     #分页查询退款单
    #     return
    # def test_findRefundList(self):
    #     #查询退款单列表
    #     return
    # def test_findDetailByNo(self):
    #     #查询退款详情
    #     return
    # def test_findUploadSaleData(self):
    #     #查询销售上报数据
    #     return
    # def test_findUploadDateList(self):
    #     #获取店铺上报时间集合
    #     return
    # def test_getOrderSatistics(self):
    #     #订单统计
    #     return

if __name__ == '__main__':
    pytest.main("-s test_trade.py")