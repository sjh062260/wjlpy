#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

import requests
import time
import re

'''
 检查商管urls 的可访问性；
 通过列出主url ，收集此页面所有url , 依次访问，检测结果
 “入参”：
       广场代码，比如mallshow；
       主url: urls.txt, 以行区分url；
"返回"：
        具体url地址，返回状态，耗费时间；
'''

def urlsParse(urlsFile,tenantCode):
   
    '''
    解析urls.txt,提取url
    返回urls 列表
    '''
    with open(urlsFile,'r') as f:
        urls = f.readlines()
        tenant_urls = []
        for line in urls:
            url = line.replace('*',tenantCode)
            tenant_urls.append(url.strip('\n'))
    # print (tenant_urls)
    return tenant_urls



def url_Collect(baseUrls,tenantCode):
    '''
    urls: urls 列表,待收集url列表
    all_links : 返回所有urls 页面下的link ,
    '''
    mallshow_login_url = 'http://mallshow.passport.mallshow.net/login/doLogin.json'
    all_links = []
    # 登录
    with requests.session() as s:
        login_url = mallshow_login_url.replace('http://mallshow','http://'+tenantCode)
        s.post(
            url = login_url,
            data={"source":"","username":"admin","password":"wjl&20171016","rc":""}
        )
        
        for line in baseUrls:
            try:
                website = s.get(url = line,timeout=5)
                # print (website.links)
                urls = re.findall(r'href="http.*html',website.text)
                urls = list(set(urls))
                all_links = all_links + urls
            except requests.exceptions.ConnectTimeout:
                pass
        all_links = list(set(all_links))
    # for line in all_links:
    #     line = line.strip('href="')
    for i in range(len(all_links)):
        all_links[i] = all_links[i][6:]
    # print (all_links)
    # print (all_links)
    all_links.sort()
    return all_links

def test_get_url(urls,tenantCode):
#     测试具体url 
#     返回测试结果
    testResults=[]
    mallshow_login_url = 'http://mallshow.passport.mallshow.net/login/doLogin.json'
    with requests.session() as s:
        login_url = mallshow_login_url   
        s.post(
            url = login_url,
            data={"source":"","username":"admin","password":"wjl&20171016","rc":""}
        )
        for line in urls:
            result = {}
            result["url"] = line
            result["tenant"] = tenantCode 
            try:
                time1 = time.time()
                resp = s.get(url = line,timeout=5)
                time2 = time.time()
                respTime = time2-time1
                respStatusCode = resp.status_code
                result["time"] = respTime
                result["statusCode"] = respStatusCode
                result["resultMsg"] = "Success"
            except requests.exceptions.ConnectTimeout:
                result["resultMsg"] = "Connection Timeout"
                result["time"]  = 5
                result["statusCode"] = 504
            testResults.append(result)
    # print (testResults)
    testResults.sort(key=lambda x:x['time'],reverse=True)
    return testResults


if __name__ == '__main__':
    urlsFilePath = 'G:/sqq/test/ats/urlsCheck/urls/urls.txt'
    tenantCode = 'mallshow'
    baseUrls = urlsParse(urlsFilePath,tenantCode)
    # baseUrls = ["http://crm.mallshow.mallshow.net/member/list.html","http://mktadmin.mallshow.mallshow.net/biz/coupon/list.html"]
    toTestUrls = url_Collect(baseUrls,tenantCode)
    testResults = test_get_url(toTestUrls,tenantCode)
    for line in testResults:
        print (line)
