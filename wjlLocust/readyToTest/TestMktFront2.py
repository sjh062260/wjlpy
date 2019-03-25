#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

from locust import HttpLocust,TaskSet,task
# import requests
import re
# import time
import queue
# from pyquery import PyQuery

class WxWebSiteTasks(TaskSet):

    openIds = ['oF31fwmd6eE5y81lQ--Jiqd2A1jk', 'oF31fwsGAwwowJGQ6KME5cB15ORE', 'oF31fwqKaoUnGJMQoHA3osCbrrb8',
               'oF31fwlRDx_IXGO9WigNsi91OLKA', 'oF31fwnkdfftHjIic2z2SGVkpxRg', 'oF31fwiWvaDQj0LGcOuWgb7RgItI',
               'oF31fwtsIJcHYg_tZoPTH-FtI14Q', 'oF31fwjQQt0mbHqVwf9GFakkOO2Y']
    user_data_queue = queue.Queue()
    for items in openIds:
        user_data_queue.put(items)

    def on_start(self):
        try:
            self.wjlTestOpenId = self.user_data_queue.get()
            uri = '/wx/member/memberCenter.html?wjlTestOpenId=' + self.wjlTestOpenId
            print(uri)
            r = self.client.get(uri)
            self.user_data_queue.put(self.wjlTestOpenId)
        except queue.Empty:
            print('openId data is empty, tests ended')
            exit(0)

#     @task
#     def jctg(self):
#         with self.client.get('/wx/subject/list.html?activityId=100618106000101') as resp:
# #            pq = PyQuery(resp.text)
# #            print(pq.attr("div","data-url"))
#             pq = re.findall("couponId=(.*)\"",resp.text)
#             # print(pq)
#         with self.client.get("/wx/subject/submitOrder.json?count=1&toCashPoint=0&pointToCashFee=0&activityId=100618106000101&couponId=1006181060001&act_type=tg") as r:
#             print (r.status_code)
#             print (r.text)

    @task
    def jfsc(self):
        with self.client.get('/wx/subject/list.html?actType=jfsc') as resp:
#            pq = PyQuery(resp.text)
#            print(pq.attr("div","data-url"))
            pq = re.findall("couponId=(.*)\"",resp.text)
            # print(pq)
        with self.client.get("/wx/subject/exchange.json?activityId=100617144000301&couponId=1006183340004&count=1") as r:
            print (r.status_code)
            print (r.text)
        with self.client.get("/wx/subject/exchange.json?activityId=100617144000301&couponId=1006183350001&count=1") as r:
            print (r.status_code)
            print (r.text)
        with self.client.get("/wx/subject/exchange.json?activityId=100617144000301&couponId=1006183350002&count=1") as r:
            print (r.status_code)
            print (r.text)
        with self.client.get("/wx/subject/exchange.json?activityId=100617144000301&couponId=1006183350003&count=1") as r:
            print (r.status_code)
            print (r.text)
        with self.client.get("/wx/subject/exchange.json?activityId=100617144000301&couponId=1006183350004&count=1") as r:
            print (r.status_code)
            print (r.text)
        with self.client.get("/wx/subject/exchange.json?activityId=100617144000301&couponId=1006183350005&count=1") as r:
            print (r.status_code)
            print (r.text)
        with self.client.get("/wx/subject/exchange.json?activityId=100617144000301&couponId=1006183350006&count=1") as r:
            print (r.status_code)
            print (r.text)
        with self.client.get("/wx/subject/exchange.json?activityId=100617144000301&couponId=1006183350007&count=1") as r:
            print (r.status_code)
            print (r.text)
        with self.client.get("/wx/subject/exchange.json?activityId=100617144000301&couponId=1006183350008&count=1") as r:
            print (r.status_code)
            print (r.text)
        with self.client.get("/wx/subject/exchange.json?activityId=100617144000301&couponId=1006183350009&count=1") as r:
            print (r.status_code)
            print (r.text)



class WxWebSiteUser(HttpLocust):
    task_set =  WxWebSiteTasks
    host = 'http://mallshow.mallshow.net'
    min_wait = 1000
    max_wait = 5000