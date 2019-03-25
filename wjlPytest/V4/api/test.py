#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

"""
@author:sjh
@time:2018/6/2 12:00
"""
import requests
import pytest
import time, hashlib
# import wjlTestLib
# from api import wopV4Lib
import wopV4Lib

TIMEFORMAT = "%Y-%m-%d %H:%M:%S"


appId = '1fs4y6iz'
appsecret = '6kddr2b6pqqnqzdglxjonu25'
groupId = 1012
tenantId = 4031
reqMode = '0101'
# timestamp = wopV4Lib.get_timestamp()
timestamp = '2019-03-12 17:56:08'
data = {
    "orderType": "2",
    "orderChannel": "103",
    "orderSource": "15",
    "totalFee": 1,
    "outOrderNo": "20190304164400003",
    "storeId": "198",
    "memberId": "10080100158515",
    "actTotalFee": 1,
    "payStatus": "2",
    "payMethod": "3",
    "createTime": "2019-03-04 11:21:33",
    "updateTime": "2019-03-04 12:19:25",
    "payTime": "2019-03-04 11:21:33",
    "posNo": "01",
    "details": "",
    "memberCreditValue": "",
    "remark": "test"}
# params = {"appId":appId,"groupId":groupId,"tenantId":tenantId,"reqMode":reqMode,"timestamp":timestamp,"data":data}
params = {"appId":appId,"groupId":groupId,"tenantId":tenantId,"reqMode":reqMode,"timestamp":timestamp}
t = wopV4Lib.right_sign(params,appsecret)



