#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

# Created on 2016年7月16日
# @author: jiaohui
import time,datetime,hashlib,os


HOST = "http://sop.scpretail.net/api"  # sop产品环境
APPID="8507fbbbadf3711848d183f0b8c11a"
APPSECRET="d3e4d2c8-5e99-467d-a26f-d84b9361c3b9"

TIMEFORMAT = "%Y-%m-%d %H:%M:%S"


# 获取当前时间
def get_now_time ():
    # nowTime = time.strftime (TIMEFORMAT)
    nowTime = "%d"%(time.time()*1000)
    return nowTime

# 通过params 和signKey生成正确的sign
def right_sign (params, key):
    params = params
    params.sort ()
    appSecrect = key
    paramsstring = ''
    for line in params:
        paramsstring = paramsstring + line + '&'
    signString = paramsstring + 'apiSecret=' + appSecrect
    print(signString)
    sign = hashlib.md5(signString.encode('utf-8')).hexdigest()
    signedString = paramsstring + 'sign=' + sign
    return signedString


# 会员注册 带openId
def queryMemberInfo (mobile):
    method = "queryMemberInfo"
    mobile = mobile
    timestamp = get_now_time ()
    params = ["method=" + method, "apiKey=" + APPID, "mobile=" + mobile, "timestamp=" +timestamp]
    signedString = right_sign (params, APPSECRET)
    print (HOST + '?' + signedString)

#
def bindCard(cardno,mobile,openid,name,idno):
    method = "bindCard"
    timestamp = get_now_time()
    params = ["method="+method,"apiKey="+APPID,"timestamp="+timestamp,"cardno="+cardno,"mobile="+mobile,"openid="+openid,"name="+name,"idno="+idno]
    signedString = right_sign(params,APPSECRET)
    print(HOST + '?' + signedString)

def updateMemberInfo(mobile,birthday,openid,uid,name,idno):
    method = "updateMemberInfo"
    timestamp = get_now_time()
    mobile = mobile
    birthday = birthday
    openid = openid
    uid = uid
    name = name
    idno = idno
    params = ["method=" + method, "apiKey=" + APPID, "birthday=" + birthday, "mobile=" + mobile, "openid=" + openid,
              "name=" + name, "idno=" + idno,"uid="+uid,"timestamp="+timestamp]
    signedString = right_sign(params,APPSECRET)
    print(HOST + '?' + signedString)

def creditChange(tenantId,uid,point,desc):
    method = "creditChangeForbidden"
    desc = desc
    point = point
    tenantId = tenantId
    timestamp = get_now_time()
    uid = uid
    params = ["method=" + method, "apiKey=" + APPID, "desc=" + desc, "point=" + point, "tenantId=" + tenantId,
              "uid="+uid,"timestamp="+timestamp]
    signedString = right_sign(params,APPSECRET)
    print(HOST + '?' + signedString)

def queryCreditChange(uid,startTime,mobile):
    method = "queryCreditChange"
    timestamp = get_now_time()
    start = '0'
    num = '10'
    uid = uid
    startTime = startTime
    mobile = mobile
    version = '1.0'
    params = ["method=" + method, "apiKey=" + APPID, "start=" + start, "num=" + num, "uid=" + uid,
              "startTime="+startTime,"timestamp="+timestamp,"version="+version,"mobile="+mobile]
    signedString = right_sign(params,APPSECRET)
    print(HOST + '?' + signedString)

if __name__ == "__main__":
    # t = get_now_time()
    # print(t)
    # queryMemberInfo(mobile='18627169820')
    # bindCard(cardno="307666050737",mobile="18627169820",openid="oL_QPxKwItY3bHDQRVkGC-3bGF3A",name="sjh",idno="420181198712214298")
    # updateMemberInfo(mobile="18627169820",birthday="1987-12-21",openid="oL_QPxKwItY3bHDQRVkGC-3bGF3A",uid="137834",name="sjh",idno="420181198712214298")
    creditChange(tenantId="12",uid= "137834",point='1',desc="test")
    # queryCreditChange(uid="137834",startTime="2016-11-02",mobile="18627169820")