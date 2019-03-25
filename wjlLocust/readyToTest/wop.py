#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

from locust import HttpLocust,TaskSet,task
import random
import datetime
import time
import wjlTestLib

class Wop(TaskSet):
    appid = 'hCPAYwPwSm2spDFc_QGg9A'
    secret = '12c3dcbe5c674b82a70a1ecfc1de5ab0'
    tenantId = "1006"
    mobile = "18627169820"
    storeOutCode = "112233"
    crmUserId = ""


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

    @task(10)
    def uploadOrderByStoreOutCode(self):
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        payload = self.comData()
        outOrderNo = wjlTestLib.random_outorderno()
        timestamp = wjlTestLib.get_timestamp()
        fee = wjlTestLib.get_fee()
        data = str({"outOrderNo":outOrderNo,
                    "storeOutCode":self.storeOutCode,
                    "crmUserId":self.crmUserId,
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
        resp = self.client.post("/order/uploadOrderByStoreOutCode",data=payload)
        print(resp.text)
    @task(1)
    def uploadOrderByStoreOutCodeAndRefund(self):
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        payload = self.comData()
        outOrderNo = wjlTestLib.random_outorderno()
        timestamp = wjlTestLib.get_timestamp()
        fee = wjlTestLib.get_fee()
        data = str(
            {"outOrderNo": outOrderNo,
                    "storeOutCode": self.storeOutCode,
                    "crmUserId": self.crmUserId,
                    "orderType": 2,
                    "status": 2,
                    "couponNo": "",
                    "couponPrefFee": "",
                    "totalFee": fee,
                    "actTotalFee": fee,
                    "orderSource": 4,
                    "createTime": timestamp,
                    "updateTime": timestamp,
                    "orderChannel": 10,
                    "payMethod": 1,
                    "payTime": timestamp
                    })
        payload["data"] = data
        resp = self.client.post("/order/uploadOrderByStoreOutCode", data=payload)
        print(resp.text)
        refundNo = 'f'.join(outOrderNo)
        data_refund = str(
            {
                "outOrderNo": outOrderNo,
                "refundNo":refundNo,
                "remark":"缺钱了就要退",
                "type":2,
                "status":5,
                "createTime": timestamp,
                "updateTime": timestamp
            }        )
        payload_refund = self.comData()
        payload_refund["data"] = data_refund
        resp = self.client.post("/order/thirdRefundSync",data = payload_refund)
        print(resp.text)



class WopUser(HttpLocust):
    task_set =  Wop
    host = 'http://wop.mallshow.net'
    min_wait = 1000
    max_wait = 5000