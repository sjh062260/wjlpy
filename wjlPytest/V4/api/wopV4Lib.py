#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

"""
@author:sjh
@time:2018/6/8 14:28
"""
import requests
import time, hashlib
import copy
from random import choice
from datetime import datetime
import random

TIMEFORMAT = "%Y-%m-%d %H:%M:%S"

def get_random_phonenumber():
    area_num = ['134', '135', '136', '137', '138', '139', '150', '151', '152', '158', '159', '157', '182', '187',
                 '188',
                 '147', '130', '131', '132', '155', '156', '185', '186', '133', '153', '180', '189']
    num_start = choice(area_num)
    seed = "1234567890"
    sa = []
    for i in range(8):
        sa.append(choice(seed))
    last_number = ''.join(sa)
    phone_number = num_start+last_number
    return phone_number

def get_random_outorderno():
    time.sleep(1)
    now = datetime.now()
    s = datetime.strftime(now,"%Y%m%d%H%M%S")
    seed = "1234567890"
    sa = []
    for i in range(4):
        sa.append(choice(seed))
    last_number = ''.join(sa)
    outOrderNo = s+last_number
    # print outOrderNo
    return outOrderNo

def get_timestamp():
    time.sleep(1)
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def get_fee():
    return random.randrange(100,100000,100)

def right_sign(params, appsecret):
    if type(params) == dict:
        paramsList = []
        for item in params.keys():
            paramsList.append("%s=%s" % (item, params[item]))
    else:
        paramsList = params
    paramsList.sort()
    paramsstring = ''
    for line in paramsList:
        paramsstring = paramsstring + line + '&'
    toSignString = paramsstring + appsecret
    print(toSignString)
    sign = hashlib.md5(toSignString.encode()).hexdigest()
    print(sign)
    print(paramsstring+"sign="+sign)
    return sign


def sendSMSVerifyCode(host,comParams,appSecret,mobile):
    url = host+"/msg/sendSMSVerifyCode"
    paramsData = copy.copy(comParams)
    paramsData["timestamp"] = get_timestamp()
    mobile = mobile
    data = {
        "mobile":mobile
    }
    paramsData["data"] = str(data)
    sign = right_sign(paramsData,appSecret)
    paramsData["sign"] = sign
    resp = requests.post(url,data=paramsData)
    resp_data = resp.json()
    code = resp_data.get("data").get("code")
    return code

def getMemberInfo_Mobile(host,comParams,appSecret,mobile):
    url = host+"/member/getMemberInfo"
    paramsData = copy.copy(comParams)
    paramsData["timestamp"] = get_timestamp()
    data = {
        "queryType":2,
        "queryValue":mobile
    }
    paramsData["data"] = str(data)
    sign = right_sign(paramsData,appSecret)
    paramsData["sign"] = sign
    # print(params)
    resp = requests.post(url,data=paramsData)
    print(resp.text)
    resp_data = resp.json()
    member_id = resp_data.get("data").get("member_id")
    return member_id

def getMemberPoint_MemberId(host,comParams,appSecret,memberId):
    url = host+"/member/getMemberInfo"
    paramsData = copy.copy(comParams)
    paramsData["timestamp"] = get_timestamp()
    data = {
        "queryType":1,
        "queryValue":memberId
    }
    paramsData["data"] = str(data)
    sign = right_sign(paramsData,appSecret)
    paramsData["sign"] = sign
    # print(params)
    resp = requests.post(url,data=paramsData)
    print(resp.text)
    resp_data = resp.json()
    point = resp_data.get("data").get("point")
    return point

def downloadCoupon(host,comParams,appSecret,memberId,couponId):
    url = host+"/coupon/downloadCoupon"
    paramsData = copy.copy(comParams)
    paramsData["timestamp"] = get_timestamp()
    data = {
        "couponId":couponId,
        "memberId":memberId,
        "flowNo":get_random_outorderno(),
        "num":1
        }
    paramsData["data"] = str(data)
    sign = right_sign(paramsData,appSecret)
    paramsData["sign"] = sign
    print(paramsData)
    resp = requests.post(url,data=paramsData)
    print(resp.text)
    try:
        couponNo = ((resp.json()).get("data")[0]).get("coupon_no")
    except:
        couponNo = "111"
    return couponNo

def getTenantInfo(host,comParams,appSecret):
    url = host+"/mall/getTenantInfo"
    paramsData = copy.copy(comParams)
    paramsData["timestamp"] = get_timestamp()
    # print(params)
    sign = right_sign(paramsData,appSecret)
    paramsData["sign"] = sign
    # print(paramsData)
    resp = requests.post(url,data=paramsData)
    # print(resp.elapsed.microseconds/1000000)
    print(resp.json())

def createOrder(host,comParams,appSecret,orderData):
    url = host+"/order/getOrderInfo"
    paramsData = copy.copy(comParams)
    paramsData["timestamp"] = get_timestamp()
    data = orderData
    paramsData["data"] = str(data)
    sign = right_sign(paramsData,appSecret)
    paramsData["sign"] = sign
    resp = requests.post(url,data=paramsData)
    print(resp.text)

if __name__ == '__main__':
    host = "http://open.alldragon.com"
    group_id = '1001'
    tenant_id = '4001'
    # appId = 'qr52w63d'
    # appSecret = 'fz2t0tlcbqww9oyr0sbuvng5'
    appId = '9tg7fb0o'
    appSecret = '4hpaiconih532ldhj0tj1udx'
    storeId = '4001181020294'
    memberIds = {
        "normal_mobile": "18571651296",
        "normal_memberId": "10010118103000004"
    }
    couponIds = {
        "online_couponId": "4001181580002",
        "autodown_couponId": "4001181580001"
    }
    parking = {
        "parkCodeA": "A",
        "parkCodeB": "B",
        "plateNo": "鄂A88888",
        "inPlace": "软件园中路",
        "outPlace": "南湖大道",
        "enterTime": str(time.strftime(TIMEFORMAT, time.localtime(time.time() - 8 * 60 * 60)))
    }
    openIds = ['oa1P4s6BsPHoh_N3Enzu3P5Yii2M', 'oa1P4szB7aYNhoh5et28zYJz_yeg']
    timestamp = get_timestamp()

    comParams = {
        "appId": appId,
        "groupId": group_id,
        "tenantId": tenant_id,
        "reqMode": "01",
        "timestamp": timestamp
    }
    registe_mobile = get_random_outorderno()
    couponNo = downloadCoupon(host,comParams,appSecret,memberIds.get("normal_memberId"),couponIds.get("autodown_couponId"))
    getTenantInfo(host,comParams,appSecret)
