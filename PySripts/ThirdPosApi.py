#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

# Created on 2016年7月16日
# @author: jiaohui
import time,datetime,hashlib,requests,os

# 全局参数定义
# APPID = "scpg"
APPID="wpos"
# APPSECRET = "ddea51a82c826fd84d9d53e81bfe8a28"
APPSECRET="ae69da171f58c41b9df7dad9604e8e31"
HOST = "http://sop.scpretail.net/api"  # sop产品环境
# HOST = "http://sop.demo.shangquanquan.com/api"  # sop开发环境
TIMEFORMAT = "%Y-%m-%d %H:%M:%S"


# 获取当前时间
def get_now_time ():
    nowTime = time.strftime (TIMEFORMAT)
    return nowTime

# 通过params 和signKey生成正确的sign
def right_sign (params, key):
    params = params
    params.sort ()
    appSecrect = key
    paramsstring = ''
    for line in params:
        paramsstring = paramsstring + line + '&'
    signString = paramsstring + 'appSecret=' + appSecrect
    sign = hashlib.md5(signString.encode('utf-8')).hexdigest()
    signedString = paramsstring + 'sign=' + sign
    return signedString
