#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

# Created on 2016年6月9日
# @author: jiaohui
import time,datetime,hashlib

# 获取当前时间
def getNowTime():
    TIMEFORMAT = "%Y-%m-%d %H:%M:%S"
    nowTime = time.strftime(TIMEFORMAT)
    return nowTime

# 通过params 和signKey生成正确的sign
def rightSign(params,key):
    paramsList = params
    paramsList.sort()
    skey = key
    paramsString = ''
    for line in paramsList:
        paramsString = paramsString+line+"&"
    signString = paramsString + "skey=" + skey
    sign = hashlib.md5(signString.encode()).hexdigest()
    signedString = paramsString + "sign="+sign
    return signedString

def sign(params,key):
    paramsList = params
    paramsList.sort()
    skey = key
    paramsString = ''
    for line in paramsList:
        paramsString = paramsString+line+"&"
    signString = paramsString + "skey=" + skey
    # sign = hashlib.md5(signString.encode('utf-8')).hexdigest()
    sign = hashlib.md5(signString).hexdigest()
    # signedString = paramsString + "sign="+sign
    return sign