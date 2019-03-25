#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

# create by sjh @2017-12-18
# test all links with locust

from locust import HttpLocust,TaskSet,task
import re
import time
import requests

urlsFile = 'G:/sqq/test/ats/urlsCheck/urls/urls.txt'
tenantCode = 'mallshow'

class WebsiteTasks(TaskSet):
    self.login_url = 'http://'+tenantCode+'.passport.mallshow.net/login/doLogin.json'
    self.tenantCode = tenantCode
    self.urlsFile = urlsFile

    def urlsParse(self):
    # 解析urls.txt,提取url
    # 返回urls 列表
        with open(self.urlsFile,'r') as f:
            self.urls = f.readlines()
            self.tenant_urls = []
            for line in self.urls:
                self.url = line.replace('*',self.tenantCode)
                self.tenant_urls.append(self.url.strip('\n'))
        return self.tenant_urls

    def url_Collect(self):    
        # urls: urls 列表,待收集url列表
        # all_links : 返回所有urls 页面下的link     
        self.all_links = []
        with requests.session() as s:
            self.client.post(
                url = self.login_url,
                data={"source":"","username":"admin","password":"wjl&20171016","rc":""}
            )        
            for line in self.baseUrls:
                try:
                    website = self.client.get(url = line,timeout=5)
                    # print (website.links)
                    self.urls = re.findall(r'href="http.*html',website.text)
                    self.urls = list(set(urls))
                    self.all_links = self.all_links + self.urls
                except requests.exceptions.ConnectTimeout:
                    pass
            self.all_links = list(set(self.all_links))
        for i in range(len(self.all_links)):
            self.all_links[i] = self.all_links[i][6:]
        return self.all_links

    def on_start(self):
        self.client.post(self.login_url,{{"source":"","username":"admin","password":"wjl&20171016","rc":""}})


    @ task
    def test_Urls_Check(self,urls):
        for url in urls:
            self.client.get(url)


class WebsiteUser(HttpLocust):
    # task_set = WebsiteTasks
    baseUrls = WebsiteTasks.urlsParse(urlsFile)
    all_links = WebsiteTasks.url_Collect(baseUrls)
    task_set = WebsiteTasks.test_Urls_Check(urls=all_links)


