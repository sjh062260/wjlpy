#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

from locust import HttpLocust,TaskSet,task
import random
from pyquery import PyQuery
import Queue
import wjlTestLib


class Wop(TaskSet):
    def on_start(self):
        print("****** start ******")
    @task
    def registe(self):
        mobile = wjlTestLib.random_phonenumber()
        payload = {
            'tenantId': '1006',
            'passwd': '',
            'channel_category': '',
            'source': 'WIFI_PORTAL',
            'channel_sid': '',
            'invite_mid': '',
            'syscode': 'wifi',
            'channel_type': '',
            'mobile': mobile,
            "channel_type": "17"
        }
        resp = self.client.post('/member/register.json',data = payload)
        # print(resp.text)

class WxWebSiteUser(HttpLocust):
    task_set =  Wop
    host = 'http://api.crm.sqq.inner'
    min_wait = 1000
    max_wait = 5000