#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

from locust import HttpLocust,TaskSet,task

class UserBehavior(TaskSet):
    def login(self):
        for openId in openIds:
            self.client.get("/g/weixin/member/card?openId=%s"%openId,name = "/g/weixin/member/card?openId=[openId]")


class WebsiteUser(HttpLocust):
    openIds = []
    with open(r'F:\AutoTest\apache-jmeter-2.13\bin\scpretail\DATA_CONFIG\xxyxcOpenId.txt',mode='r',encoding='utf-8') as f:
        lines =f.readlines()
    for line in lines:
        openIds.append(line.strip('\n'))
    task_set = UserBehavior
    host = "http://wx.xxyxc.demo.shangquanquan.com"
    min_wait = 5000
    max_wait = 9000
    

