#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

from locust import HttpLocust,TaskSet,task
# import requests
import re
# import time
import Queue
# from pyquery import PyQuery

class WxWebSiteTasks(TaskSet):

    openIds = ['oF31fwp_fgLQ54127tzWQIwbA5lw', 'oF31fwvBtemLAjq9wqRfH3UK5O9M', 'oF31fwvNG2cWbFMkNwAzM9NkZ8D0',
               'oF31fwmgeOAGHSaTrA0TMrFsVuXI', 'oF31fwuV1kORAgXetgzRDjtBbVdY', 'oF31fwpTXZLVBfronLZDRFOJndAY',
               'oF31fwsjcNuvRM_hgfBLM-uVw6Ko', 'oF31fwoAQh2CHx0gx-fdhJfuscqk', 'oF31fwuqETHsWqKlVJ0w8UJ4zUjA',
               'o54ATt4Z-g5JFpQdDqwkmTdM-R7A','oF31fwvNG2cWbFMkNwAzM9NkZ8D0','oF31fwi-Ok1HXpXWi_7jf980aUcs',
               'oF31fwuV1kORAgXetgzRDjtBbVdY','oF31fwsdUePKEQZyCcCNsW4t4c10','oF31fwqyLV_NCnmAS_H4NaCV-STc',
               'oF31fwpTXZLVBfronLZDRFOJndAY']
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
    def shake_index(self):
        with self.client.get("/games/#/shake/index?gameId=SHAKE9001190310007") as r:
            print (r.status_code)
            print (r.text)




class WxWebSiteUser(HttpLocust):
    task_set =  WxWebSiteTasks
    # host = 'http://mallshow.mallshow.net'
    host = 'http://mktfront.wjl.dev.wanjianglong.net'
    min_wait = 1000
    max_wait = 5000