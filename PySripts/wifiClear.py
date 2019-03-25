#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

# Created on 2016年7月16日
# @author: jiaohui
import time,datetime,hashlib,requests,os


def clearFreePortalFlag(wifihost,usermac):
    playload = {"usermac":usermac}
    api = "/portal/clearFreePortalFlag"
    url = wifihost +api
    r = requests.post(url,data=playload)
    # print(r)
    print(r.content)

def midwareOffLine(midwarehost,userip,basId):
    playload = {"userIp":userip,"basId":basId}
    api = "/offline"
    url = midwarehost +api
    r = requests.post(url,data=playload)
    r.encoding = 'GB1312'
    data = r.text
    print(data)

def clearFreeCredit(wifihost,usermac):
    playload = {"usermac":usermac}
    api = "/portal/clearFreeCredit"
    url = wifihost +api
    r = requests.post(url,data=playload)
    print(r.content)
    

if __name__ == "__main__":
    # wifihost = "http://wifi.bdcsgc.mallshow.net"80-71-7A-45-AA-91
    # midwarehost = "http://portal.midware.mallshow.net"
    # wifihost = "http://graywifi.mallshow.mallshow.net"
    # midwarehost = "http://grayportal.midware.mallshow.net"
    # huawei honor 6
    # usermac = '80-71-7A-45-AA-91'
    # userip = '172.16.200.85'
    # basId = "10101"
    # clearFreePortalFlag(wifihost="http://wifi.reco.mallshow.mallshow.net",usermac="80-71-7A-45-AA-91")
    # midwareOffLine(midwarehost="http://portal.reco.midware.mallshow.net",userip="172.16.200.159",basId="9001")
    # midwareOffLine(midwarehost="http://portal.midware.dev.wanjianglong.net", userip="172.16.200.244", basId="10101")
    # clearFreeCredit(wifihost="http://wifi.reco.mallshow.mallshow.net",usermac="80-71-7A-45-AA-91")

    # clearFreePortalFlag(wifihost="http://wifi.wjl.dev.wanjianglong.net",usermac="90-F0-52-01-46-14")
    # midwareOffLine(midwarehost="http://portal.midware.mallshow.net",userip="172.16.200.85",basId="9001")
    # midwareOffLine(midwarehost="http://portal.midware.dev.wanjianglong.net", userip="172.16.200.16", basId="9001")
    # clearFreeCredit(wifihost="http://wifi.wjl.dev.wanjianglong.net",usermac="90-F0-52-01-46-14")


    # clearFreePortalFlag(wifihost="http://graywifi.mallshow.mallshow.net",usermac="70-8A-09-9D-64-19")
    # midwareOffLine(midwarehost="http://portal.midware.mallshow.net",userip="172.16.200.73",basId="1006")
    # midwareOffLine(midwarehost="http://portal.midware.mallshow.net", userip="172.16.200.228", basId="1006")
    # clearFreeCredit(wifihost="http://graywifi.mallshow.mallshow.net",usermac="70-8A-09-9D-64-19")


    # clearFreePortalFlag(wifihost="http://graywifi.mallshow.mallshow.net",usermac="90-F0-52-01-46-14")
    # midwareOffLine(midwarehost="http://portal.midware.mallshow.net", userip="172.16.200.16", basId="1006")
    # clearFreeCredit(wifihost="http://graywifi.mallshow.mallshow.net",usermac="90-F0-52-01-46-14")

    # clearFreePortalFlag(wifihost="http://graywifi.mallshow.mallshow.net",usermac="A4-5E-60-06-B1-7E")
    # midwareOffLine(midwarehost="http://portal.midware.mallshow.net", userip="172.16.200.113", basId="1006")
    # clearFreeCredit(wifihost="http://graywifi.mallshow.mallshow.net",usermac="A4-5E-60-06-B1-7E")

    # clearFreePortalFlag(wifihost="http://wifi.mallshow.mallshow.net",usermac="10-2A-B3-11-13-D5")
    # clearFreeCredit(wifihost="http://wifi.mallshow.mallshow.net",usermac="10-2A-B3-11-13-D5")
    # clearFreePortalFlag(wifihost="http://wifi.mallshow.mallshow.net",usermac="90-F0-52-01-46-14")
    # clearFreeCredit(wifihost="http://wifi.mallshow.mallshow.net",usermac="90-F0-52-01-46-14")
    # clearFreePortalFlag(wifihost="http://wifi.mallshow.mallshow.net",usermac="7C-50-49-6C-74-45")
    # clearFreeCredit(wifihost="http://wifi.mallshow.mallshow.net",usermac="7C-50-49-6C-74-45")
    # clearFreePortalFlag(wifihost="http://wifi.mallshow.mallshow.net",usermac="48-3B-38-87-59-62")
    # clearFreeCredit(wifihost="http://wifi.mallshow.mallshow.net",usermac="48-3B-38-87-59-62")

    clearFreePortalFlag(wifihost="http://graywifi.hdfzsj.mallshow.net",usermac="e0-94-67-6f-9a-a0")
    midwareOffLine(midwarehost="http://grayportal.midware.mallshow.net",userip="172.168.3.194",basId="1132")
    clearFreeCredit(wifihost="http://graywifi.hdfzsj.mallshow.net",usermac="e0-94-67-6f-9a-a0")

    clearFreePortalFlag(wifihost="http://graywifi.hdfzsj.mallshow.net",usermac="70-8a-09-18-81-59")
    midwareOffLine(midwarehost="http://grayportal.midware.mallshow.net",userip="172.168.4.89",basId="1132")
    clearFreeCredit(wifihost="http://graywifi.hdfzsj.mallshow.net",usermac="70-8a-09-18-81-59")

    clearFreePortalFlag(wifihost="http://graywifi.hdfzsj.mallshow.net",usermac="70-8a-09-18-81-59")
    midwareOffLine(midwarehost="http://grayportal.midware.mallshow.net",userip="172.168.8.85",basId="1132")
    clearFreeCredit(wifihost="http://graywifi.hdfzsj.mallshow.net",usermac="70-8a-09-18-81-59")