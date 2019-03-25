#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

from locust import HttpLocust,TaskSet,task
import requests
import re
import time
import Queue


class WxWebSiteTasks(TaskSet):

    openIds = ['oF31fwp_fgLQ54127tzWQIwbA5lw', 'oF31fwvBtemLAjq9wqRfH3UK5O9M', 'oF31fwvNG2cWbFMkNwAzM9NkZ8D0',
               'oF31fwmgeOAGHSaTrA0TMrFsVuXI', 'oF31fwuV1kORAgXetgzRDjtBbVdY', 'oF31fwpTXZLVBfronLZDRFOJndAY',
               'oF31fwsjcNuvRM_hgfBLM-uVw6Ko', 'oF31fwoAQh2CHx0gx-fdhJfuscqk', 'oF31fwuqETHsWqKlVJ0w8UJ4zUjA']

    user_data_queue = Queue.Queue()
    for items in openIds:
        user_data_queue.put(items)

    def on_start(self):
        try:
            self.wjlTestOpenId = self.user_data_queue.get()
            uri = '/wx/member/memberCenter.html?wjlTestOpenId=' + self.wjlTestOpenId
            print(uri)
            r = self.client.get(uri)
            self.user_data_queue.put(self.wjlTestOpenId)
        except Queue.Empty:
            print('openId data is empty, tests ended')
            exit(0)

    @task
    def memberCenter(self):
        self.client.get('/wx/member/memberCenter.html')

    @task
    def memberCard(self):
        self.client.get('/wx/member/card.html')
    @task
    def wxIndex(self):
        self.client.get('/wx/index.html')

    @task
    def selfOperatePoint(self):
        self.client.get('/wx/member/selfOperatePoint.html')

    @task
    def jfsc(self):
        self.client.get('/wx/subject/list.html?actType=jfsc')

    @task
    def schd(self):
        self.client.get('/wx/activity/list.html?theme=schd')

    @task
    def hyqy(self):
        self.client.get('/wx/cms/page.html?1=1&code=hhqy')

    @task
    def feedback(self):
        self.client.get('/wx/feedback/index.html')

    @task
    def mylist(self):
        self.client.get('/wx/favor/mylist.html')

    @task
    def myCouponList(self):
        self.client.get('/wx/mycoupon/list.html')

    @task
    def parkIndex(self):
        self.client.get('/parking/parking/fee/index.html')

    @task
    def parkIndex(self):
        self.client.get('/parking/parking/fee/isIn.json?carNo=鄂A88888')

    @task
    def storeList(self):
        self.client.get('/wx/store/list.html')

    # @task
    # def activityList(self):
    #     self.client.get('/wx/activity/list.html')

    @task
    def myIntegralList(self):
        self.client.get('/wx/member/myIntegralList.html')

class WxWebSiteUser(HttpLocust):
    task_set =  WxWebSiteTasks
    host = 'http://mallshow.mallshow.net'
    min_wait = 1000
    max_wait = 5000