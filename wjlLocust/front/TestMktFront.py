#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

from locust import HttpLocust,TaskSet,task
# import requests
import re
# import time
import Queue
from pyquery import PyQuery

class WxWebSiteTasks(TaskSet):

    openIds = ['oVDyijkQ9c5LdyIb6uRubbLt4oQM', 'oVDyijsRuOtx4AsrPesh8AjZ4gIk', 'oVDyijpmFHhKUoT_oqJvig-ZaZKs',
               'oVDyijsedKjO5kR_gAPeGxKzvcG0', 'oVDyijnkT-4wEChrr9ssMKOCEZrE', 'oVDyijpMa2Fd9_xhc-oJyFjE0cEk',
               'oVDyijkG4NKQ_Dky6N-RcptvNhH4', 'oVDyijlVG_cpFB247UGIVVcHF6F8']

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
    def jctg(self):
        with self.client.get('/wx/subject/list.html?actType=jfsc') as resp:
#            pq = PyQuery(resp.text)
#            print(pq.attr("div","data-url"))
            pq = re.findall("couponId=(.*)\"",resp.text)
            print(pq)
        with self.client.get("/wx/subject/exchange.json?activityId=900118331000201&couponId=9001183340001&count=1") as r:
            print (r.status_code)
            print (r.text)




class WxWebSiteUser(HttpLocust):
    task_set =  WxWebSiteTasks
    host = 'http://wjl.dev.wanjianglong.net'
    min_wait = 1000
    max_wait = 5000