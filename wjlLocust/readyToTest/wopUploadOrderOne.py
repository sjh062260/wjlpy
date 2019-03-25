#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

from locust import HttpLocust,TaskSet,task
import random
import datetime
import time
import wjlTestLib

class Wop(TaskSet):
    appid = 'SYDYC_FZ_TEST'
    secret = 'd16f46cbbcced110da53a805fe50b9c1'
    tenantId = "9001"
    mobile = "18571651296"
    storeId = "9001181140002"
    memberId = "900118268000001"


    def getToken(self):
        payload = {"grant_type":"client_credential","appid":self.appid,"secret":self.secret}
        resp = self.client.get('/token?grant_type=client_credential&appid=%s&secret=%s'%(self.appid,self.secret))
        access_token = resp.json()["access_token"]
        # print ("access_token :"+access_token)
        return str(access_token)

    def comData(self):
        comdata = {"version": "1.0","tenantId":self.tenantId,"accessToken":self.getToken()}
        return comdata

    # @task
    # def getParkInfo(self):
    #     headers = {'content-type': 'application/x-www-form-urlencoded'}
    #     payload = self.comData()
    #     data = str({"mobile":self.mobile})
    #     payload["data"] = data
    #     resp = self.client.post("/system/getparkinfo",data=payload)
    #     # print(resp.text)

    # @task(10)
    # def uploadOrder_Member(self):
    #     headers = {'content-type': 'application/x-www-form-urlencoded'}
    #     payload = self.comData()
    #     outOrderNo = wjlTestLib.random_outorderno()
    #     timestamp = wjlTestLib.get_timestamp()
    #     fee = wjlTestLib.get_fee()
    #     data = str({"outOrderNo":outOrderNo,
    #                 "storeId":self.storeId,
    #                 "memberId":self.memberId,
    #                 "orderType":2,
    #                 "status":2,
    #                 "couponNo":"",
    #                 "couponPrefFee":"",
    #                 "totalFee":fee,
    #                 "actTotalFee":fee,
    #                 "orderSource":4,
    #                 "createTime":timestamp,
    #                 "updateTime":timestamp,
    #                 "orderChannel":10,
    #                 "payMethod":1,
    #                 "payTime":timestamp
    #                 })
    #     payload["data"] = data
    #     resp = self.client.post("/order/uploadOrder",data=payload)
    #     print(resp.text)

    @task(10)
    def uploadOrder_NotMember(self):
        for i in range(10):
            headers = {'content-type': 'application/x-www-form-urlencoded'}
            payload = self.comData()
            outOrderNo = wjlTestLib.random_outorderno()
            timestamp = wjlTestLib.get_timestamp()
            fee = wjlTestLib.get_fee()
            data = str({"outOrderNo":outOrderNo,
                        "storeId":self.storeId,
                        "memberId":'',
                        "orderType":2,
                        "status":2,
                        "couponNo":"",
                        "couponPrefFee":"",
                        "totalFee":fee,
                        "actTotalFee":fee,
                        "orderSource":4,
                        "createTime":timestamp,
                        "updateTime":timestamp,
                        "orderChannel":10,
                        "payMethod":1,
                        "payTime":timestamp
                        })
            payload["data"] = data
            resp = self.client.post("/order/uploadOrder",data=payload)
            print(resp.text)
        # @task(1)
    # def uploadOrderByStoreOutCodeAndRefund(self):
    #     headers = {'content-type': 'application/x-www-form-urlencoded'}
    #     payload = self.comData()
    #     outOrderNo = wjlTestLib.random_outorderno()
    #     timestamp = wjlTestLib.get_timestamp()
    #     fee = wjlTestLib.get_fee()
    #     data = str(
    #         {"outOrderNo": outOrderNo,
    #                 "storeOutCode": self.storeOutCode,
    #                 "crmUserId": self.crmUserId,
    #                 "orderType": 2,
    #                 "status": 2,
    #                 "couponNo": "",
    #                 "couponPrefFee": "",
    #                 "totalFee": fee,
    #                 "actTotalFee": fee,
    #                 "orderSource": 4,
    #                 "createTime": timestamp,
    #                 "updateTime": timestamp,
    #                 "orderChannel": 10,
    #                 "payMethod": 1,
    #                 "payTime": timestamp
    #                 })
    #     payload["data"] = data
    #     resp = self.client.post("/order/uploadOrderByStoreOutCode", data=payload)
    #     print(resp.text)
    #     refundNo = 'f'.join(outOrderNo)
    #     data_refund = str(
    #         {
    #             "outOrderNo": outOrderNo,
    #             "refundNo":refundNo,
    #             "remark":"缺钱了就要退",
    #             "type":2,
    #             "status":5,
    #             "createTime": timestamp,
    #             "updateTime": timestamp
    #         }        )
    #     payload_refund = self.comData()
    #     payload_refund["data"] = data_refund
    #     resp = self.client.post("/order/thirdRefundSync",data = payload_refund)
    #     print(resp.text)



class WopUser(HttpLocust):
    task_set =  Wop
    # host = 'http://wop.mallshow.net'
    host = 'http://wopv2.dev.wanjianglong.net'
    min_wait = 1000
    max_wait = 50000