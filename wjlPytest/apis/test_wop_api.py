#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

import re
import requests
import time
import wopV4Lib

host = 'https://open.dev4.wanjianglong.net/v3'
tenantId = '4021'
appId = 'sjmr1465'
appSecret = 'kousmu57hbnvr3psshsc2cyh'
mobile = '18571651296'
couponNo = '4021197619129'
storeId='1090171090009'
salesCode='10000063'
posNo = '50631179'

outOrderNoToCreate=wopV4Lib.get_random_outorderno()
tradeTime =wopV4Lib.get_timestamp()

comData={
    "version":"1.0",
    "tenantId":tenantId,
    "accessToken":"accessToken"
}

def get_accessToken():
    url = host+"/accessToken"
    params = {
        "grant_type":"client_credential",
        "appid":appId,
        "secret":appSecret
    }
    resp = requests.post(url,data=params)
    print(resp.text)
    token = resp.json()["access_token"]
    comData["accessToken"] = token
    print(comData)



def query_member_detail():
    # url = host+"/getMemberInfo"
    params = comData.copy()
    params["data"] = {"mobile":mobile}
    res = requests.post(
        url="https://open.dev4.wanjianglong.net/v3/getMemberInfo", data=params)
    print(res.url)
    print(res.text)


# def qeury_coupon_detail():
#     url = host+"/coupon/detail"
#     params = comData.copy()
#     params["data"] = {"couponNo":couponNo}
#     res = requests.post(url,data=params)
#     print(res.text)

def quuery_store_coupon():
    url = host+"/storeUsabeList"
    params = comData.copy()
    params["data"] = {
        "mobile":mobile,
        "storeId":storeId
    }
    res = requests.post(url,data=params)
    print(res.text)

def create_order():
    url = host+"/createOrder"
    params = comData.copy()
    params["data"] = {
        "orderType":2,
        "orderSource":4,
        "totalFee":1000,
        "actTotalFee":1000,
        "salesCode":salesCode,
        "posNo":posNo,
        "storeId":storeId,
        "outOrderNo":outOrderNoToCreate,
        "orderChannel":10,
        "couponPreFee":0,
        "status":2,
        "memberId":''
    }
    res = requests.post(url,data=params)
    print(res.text)

def success_pay_callback():
    url = host+"/payCallbackNotify"
    params = comData.copy()
    params["data"] = {
        "payNo":"P"+outOrderNoToCreate,
        "tradeTime":tradeTime,
        "payTime":tradeTime,
        "createTime":tradeTime,
        "payMethod":3,
        "tradeFee":1000,
        "updateTime":tradeTime,
        "ref_no":"",
        "buyerId":"",
        "outOrderNo":outOrderNoToCreate,
        "auth_no":"",
        "status":2
    }
    res = requests.post(url,data=params)
    print(res.text)

def refund_order():
    url = host+"/syncRefund"
    params = comData.copy()
    params["data"] = {
        "refundNo":"F"+outOrderNoToCreate,
        "createTime":tradeTime,
        "updateTime":tradeTime,
        "isRefundHandle":1,
        "type":2,
        "outOrderNo":outOrderNoToCreate,
        "status":5,
    }
    res = requests.post(url,data=params)
    print(res.text)

# def close_order():
#     url = host+"/member/detail"
#     params = comData.copy()
#     params["data"] = {"mobile":mobile}
#     res = requests.post(url,data=params)
#     print(res.text)


if __name__ == '__main__':
    # get_accessToken()
    query_member_detail()
    # quuery_store_coupon()
