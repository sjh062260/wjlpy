# _*_ coding:utf-8 _*_
# ! /usr/bin/env python
__author__ = 'Administrator'

import re
import collections

def ngSplit(lines):
    i = 0
    request = []
    time_count = url_count = resp_time = {}
    lines = lines
    for line in lines:
        # print(line)
        http_req = line.split("```")
        # print(http_req)
        timerow = http_req[0].split (":")
        hm = timerow [1] + ":" + timerow [2]  # 获取小时和分钟做为key
        tenant = http_req[3]
        req_url = http_req[4]
        respose_code = http_req[6]
        respose_time = http_req[7]
        request.append((hm,tenant,req_url,respose_code,respose_time))
        # if hm in time_count:
        #     time_count[hm] = time_count[hm]+1
        # else:
        #     time_count[hm] = 1
        # # if tenant_host in tenant.keys:
        # #     tenant[tenant_host] = tenant[tenant_host]+1
        # # elseif:
        # #     tenant[tenant_host] = 1
        # if req_url in url_count:
        #     url_count[req_url] = url_count[req_url]+1
        # else:
        #     url_count[req_url] = 1
        # if respose_time in resp_time:
        #     resp_time[respose_time] = resp_time[respose_time]+1
        # else:
        #     resp_time[respose_time] = 1
        # print(hm,req_url,respose_time)
    return request
if __name__ == "__main__":
    with open(r'G:\scpg_wx_ng\wx-yxc-access_20161001.log','r',encoding='utf-8') as f:
        f1 = f.readlines()
    with open(r'G:\scpg_wx_ng\wx-yxc-access_20161001_02.log', 'r', encoding='utf-8') as f:
        f2 = f.readlines()
    f1 = f1+f2
    del f2
    # s = ['"01/Oct/2016:00:00:06 +0800"```"10.158.247.12"```"GET"```"wx.suyxc.scpretail.net"```"/j/member/card"```"-"```"200"```"1.005"```"-"```"114.216.12.242, 101.226.68.141"```"Mozilla/5.0 (Linux; Android 5.0.2; MI 2 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile MQQBrowser/6.2 TBS/036558 Safari/537.36 MicroMessenger/6.3.25.861 NetType/WIFI Language/zh_CN"```"-"```"-"```"otMPXjgPaGWcJKqFMQt1AGMSUEWI"```"26711160421203325305328"```"1.004"```"-"```"']

    ngSplit(f1)
    s = ngSplit(f1)
    s.sort()
    time_list = url_list = resp_time = []
    for i in s:
        # print(i)
        # time_list.append(i[0])
        # url_list.append(i[2])
        # resp_time.append(i[4])
        t = i[4].split('"')
        response_time = float(t[1])
        # print(response_time)
        if response_time>0.5:
            print(i)
    # print(resp_time)
    # Time_set = list(set(time_list))
    # Time_set.sort()
    # Url_list = list(set(url_list))
    # resp_time = list(set(resp_time))
        # for item in Time_set:
    #     print("%s has %d requests:"%(item,time_list.count(item)))
    # try:
    # for item in Url_list:
        # print("最多请求URL: %s,次数: %s"%(item,url_list.count(item)))

    # for item in resp_time:
    #     print("URL响应时间: %s,次数: %s"%(item,resp_time.count(item)))