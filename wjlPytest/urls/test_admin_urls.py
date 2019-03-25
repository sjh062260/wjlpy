#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

import requests
from urlparse import urljoin
import pytest
import time
import re

class UrlCheck(object):
    def __init__(self,base_url):
        self.base_url = base_url
        self.username = 'admin'
        self.password = 'wjl&20171016'
        self.session = requests.session()

    def login(self,username,password):
        url = urljoin(self.base_url,'login/doLogin.json')
        data ={ "source":"","username":"admin","password":self.password,"rc":""}
        response = self.session.post(url,data=data).json()
        print('\n*****************************************')
        print(u'\n1、请求url: \n%s' % url)
        print(u'\n2、请求头信息:')
        print(self.session.headers)
        print(u'\n3、请求参数:')
        print(data)
        print(u'\n4、响应:')
        print(response)
        return response

    def get_cookies(self,username,password):
        url = urljoin(self.base_url,'login/doLogin.json')
        data ={ "source":"","username":"admin","password":self.password,"rc":""}
        return requests.post(url,data=data).cookies


class TestUrlsCheck():
    def test_member_list(self):




