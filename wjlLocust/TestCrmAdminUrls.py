#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

from locust import HttpLocust,TaskSet,task
import random
from pyquery import PyQuery
import Queue

class WxWebSiteTasks(TaskSet):

    crm_to_test_urls = ['/member/list.html','/console/index','/tag/list','/tag/listGroup',
                        '/member/wxlist.html','/sams/invite/list.html','/favor/list.html','/gift/exchange',
                        '/grade/list.html','/equity/category_credit_ratio','/selfpoint/list.html',
                        '/pointToCash/list.html','/point/list.html','/point/day_sum_list.html',
                        '/card/list.html','/gift/type','/tenant/config']

    def on_start(self):
        # assume all users arrive at the index page
        self.index_page()
        self.index = 0

    def index_page(self):
        self.login_url = 'http://wjl.passport.dev.wanjianglong.net/login/doLogin.json'
        r = self.client.post(
            url=self.login_url,
            data={"source": "", "username": "admin", "password": "111111", "rc": ""}
        )
        # print (r.content)

    # @task
    # def member_list(self):
    #     self.client.get('/member/list.html')

    # @task
    # def console_index(self):
    #     self.client.get('/console/index')
    #
    # @task
    # def tag_list(self):
    #     self.client.get('/tag/list')
    #
    # @task
    # def tag_listGroup(self):
    #     self.client.get('/tag/listGroup')

    @task
    def load_page(self):
        url  = self.crm_to_test_urls[self.index]
        print('visit url: %s' % url)
        self.client.get(url)
        self.index = (self.index+1)%len(self.crm_to_test_urls)

class WxWebSiteUser(HttpLocust):
    tenantCode = 'wjl'
    host = 'http://crm.%s.dev.wanjianglong.net'%(tenantCode)
    task_set =  WxWebSiteTasks
    # login_host = 'http://%s.passport.dev.wanjianglong.net'%(tenantCode)
    # rpt_host = 'http://rpt.%s.dev.wanjianglong.net'%(tenantCode)
    # mkt_host = 'http://mktadmin.%s.dev.wanjianglong.net'%(tenantCode)
    # wxms_host = 'http://wxms.%s.dev.wanjianglong.net'%(tenantCode)
    min_wait = 1000
    max_wait = 5000