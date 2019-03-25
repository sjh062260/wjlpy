#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

from locust import HttpLocust,TaskSet,task
import random
from pyquery import PyQuery
import Queue

class WxMerchantFront(TaskSet):
    # wjlTestOpenId='oVDyijsSyU73wpQzZWuEqm_6XITI'
    base_urls = ['/wx/index.html',
                 '/wx/activity/list.html?theme=schd',
                 '/wx/subject/list.html?actType=jfsc',
                 '/wx/subject/list.html?actType=qyhq',
                 '/wx/member/selfOperatePoint.html',
                 '/wx/feedback/index.html',
                 '/wx/store/recList.html',
                 '/wx/member/memberCenter.html']

    # openIds = ['oVDyijsSyU73wpQzZWuEqm_6XITI']
    # user_data_queue = Queue.Queue()
    # for items in openIds:
    #     user_data_queue.put(items)
    wjlTestOpenId=''

    def on_start(self):
        # assume all users arrive at the index page
        self.index_page()
        self.urls_on_current_page = self.toc_urls

    def index_page(self):
        try:
            # self.wjlTestOpenId = self.user_data_queue.get()
            uri = '/wx/member/memberCenter.html?wjlTestOpenId=' + self.wjlTestOpenId
            print(uri)
            self.to_test_urls = []
            r = self.client.get(uri)
            pq = PyQuery(r.content)
            link_elements = pq('a')
            self.toc_urls = [
                l.attrib["href"] for l in link_elements
            ]
            self.toc_urls = list(set(self.toc_urls+self.base_urls))
            self.user_data_queue.put(self.wjlTestOpenId)
        except Queue.Empty:
            print('openId data is empty, tests ended')
            exit(0)


    @task(1)
    def load_page(self, url=None):
        url = random.choice(self.toc_urls)
        r = self.client.get(url)
        pq = PyQuery(r.content)
        link_elements = pq("a")
        self.urls_on_current_page = [
            l.attrib["href"] for l in link_elements
        ]

    @task(1)
    def load_sub_page(self):
        url = random.choice(self.urls_on_current_page)
        r = self.client.get(url)

class WxWebSiteUser(HttpLocust):
    task_set =  WxMerchantFront
    host = 'http://mallshow.mallshow.net'
    min_wait = 1000
    max_wait = 5000