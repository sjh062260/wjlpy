#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

from locust import HttpLocust,TaskSet,task
import random
import datetime
import time
import wjlTestLib

class Order(TaskSet):
    tenantId = 9001

    @task
    def getMaxPosNo(self):
        payload = {}
        payload['tenantId'] = self.tenantId
        payload['bit'] = 6
        payload['sysycode'] = 'merchant'
        payload['deviceId'] = '1735CA820557'
        print(payload)
        resp = self.client.post("/biz/order/getMaxPosNo.json", data=payload)
        print(resp)



class OrderUser(HttpLocust):
    task_set =  Order
    host = 'http://order.dev.wanjianglong.net'
    min_wait = 1000
    max_wait = 5000