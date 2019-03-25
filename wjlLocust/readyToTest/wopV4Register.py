#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

from locust import HttpLocust,TaskSet,task
import random
import datetime
import time
import wjlTestLib
from _random import Random

class Wop(TaskSet):

    appId = 'q6SAeFd9Sn-2jsbPzPGzOA'
    secret = 'c7cc0d9bda0f42d887f1e4ead6e12574'
    tenantId = "4021"
    groupId = '1200'
    reqMode = '0101'
    
    payload = {
        "appId":appId,
        "tenantId":tenantId,
        "groupId":groupId,
        "reqMode":reqMode,
        "timestamp":wjlTestLib.get_timestamp()
        }

    def bindMember(self,memberId,openId,bindType):
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        timestamp = wjlTestLib.get_timestamp()
        payload = self.payload.copy()
        data = str({
            "memberId":memberId,
            "bindType":bindType,
            "bindValue":openId})
        payload["data"] = data
        payload["sign"] = wjlTestLib.random_string(26)
        print("memberId:"+memberId,"    openId:"+openId)
        resp = self.client.post("/member/bindMember",data=payload,headers=headers)
        print(resp.text)

    @task(10)
    def register(self):
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        timestamp = wjlTestLib.get_timestamp()
        mobile = wjlTestLib.random_phonenumber()
        payload = self.payload.copy()
        data = str({
            "mobile":mobile,
            "authCode":"888999",
            "nickName":"test"})
        payload["data"] = data
        payload["sign"] = wjlTestLib.random_string(26)
        resp = self.client.post("/member/register",data=payload,headers=headers)
        print(resp.text)
        memberId = ((resp.json()).get("data"))["member_id"]
        openId = wjlTestLib.random_string(28)
        self.bindMember(memberId,openId,1)







class WopUser(HttpLocust):
    task_set =  Wop
    # host = 'http://wop.mallshow.net'
    host = 'https://open.dev4.wanjianglong.net'
    # host = 'http://wopv2.dev.wanjianglong.net'
    min_wait = 1000
    max_wait = 5000
