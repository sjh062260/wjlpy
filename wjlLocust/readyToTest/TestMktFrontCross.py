#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

from locust import HttpLocust,TaskSet,task
# import requests
import re
# import time
import Queue
from pyquery import PyQuery

class WxWebSiteTasks(TaskSet):

    memberIds = ['100615258000001','100615258000004','100615258000010','100616176000001','100616215000002',
    '100616249000001','100616251000002']
    user_data_queue = Queue.Queue()
    for items in memberIds:
        user_data_queue.put(items)

    # def on_start(self):
    #     try:
    #         self.wjlTestOpenId = self.user_data_queue.get()
    #         uri = '/wx/member/memberCenter.html?wjlTestOpenId=' + self.wjlTestOpenId
    #         print(uri)
    #         r = self.client.get(uri)
    #         self.user_data_queue.put(self.wjlTestOpenId)
    #     except Queue.Empty:
    #         print('openId data is empty, tests ended')
    #         exit(0)

    @task
    def testcrossinfo(self):
        try:
            self.memberId = self.user_data_queue.get()
            uri = '/testcross/info?tenantId=1006&memberId='+self.memberId+'&activityId=1006180950001'
            print(uri)
            # with self.client.get(uri) as r:
            #     print (r.status_code)
            #     print (r.text)

            r = self.client.get(uri)
            print (r.status_code)
            print (r.text)
            self.user_data_queue.put(self.memberId)
        except Queue.Empty:
            print('memberId data is empty, tests ended')
            exit(0)




class WxWebSiteUser(HttpLocust):
    task_set =  WxWebSiteTasks
    host = 'http://mktfront.mallshow.mallshow.net'
    min_wait = 1000
    max_wait = 5000