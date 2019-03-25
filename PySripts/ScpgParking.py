#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

# Created on 2016年6月9日
# @author: jiaohui
import time,datetime,hashlib
# import requests


# 全局参数定义

# 停车场
# skey = "parking"
# appSecret = "parking_aike"
# skey = "jieshunParking"
skey = "scpgParking"
# skey = "sqqParking"
# host = "http://wx.xxyxc.demo.shangquanquan.com"  # 停车缴费开发环境
# host = "http://api.park.dev.wanjianglong.net"  # V3 开发环境
# host = "http://xxyxc.dev.wanjianglong.net/parking"
# host = "http://xxyxc.dev.wanjianglong.net"
# host = "http://172.16.27.58:8080"
# host = "http://wx.nbyxc.scpretail.net"  # 宁波印象城
# host = "http://wx.xayxc.scpretail.net"  # 西安印象城
# host = "http://wx.njxyc.scpretail.net"  # 南京印象城
# host = "http://xayxc.sgtnt.scpgroup.com.cn/parking"  # xxyxc印象城
# host = "http://gdyxc.sgtnt.scpgroup.com.cn"  # xxyxc印象城
# host = "http://gdyxc.sgtnt.scpgroup.com.cn/parking"  # xxyxc印象城
# host = "http://gdyxc.sgtnt.scpgroup.com.cn"  # xxyxc印象城

host = "http://xayxc.sgtnt.scpgroup.com.cn/parking"  # xxyxc印象城
# host = "http://xayxc.mallshow.net/parking"  # gdyxc mallshow
# host = "http://mallshow.sgtnt.scpgroup.com.cn/parking"  # xxyxc印象城
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
    sign = hashlib.md5(signString.encode('utf-8')).hexdigest()
    # signedString = paramsString + "sign="+sign
    return sign

def query_car(carNo):
    carNo = carNo
    api = r'/parking/api/query'
    timestamp = getNowTime()
    # timestamp = "2016-10-09 13:38:17"
    paramslist = ["carNo=" + carNo, "timestamp=" + str(timestamp)]
    signedString = rightSign(paramslist, skey)
    print(host + api + "?" + signedString)


def query_card(cardNo):
    cardNo = cardNo
    api = r'/parking/api/query'
    timestamp = getNowTime()
    # timestamp = queryTime
    paramslist = ["cardNo=" + cardNo, "timestamp=" + str(timestamp)]
    signedString = rightSign(paramslist, skey)
    print(host + api + "?" + signedString)


def car_in(carNo, startTime):
    carNo = carNo
    api = r'/parking/api/in'
    timestamp = getNowTime()
    # timestamp = '2016-11-28 15:57:36'
    startTime = startTime
    paramslist = ["carNo=" + carNo, "startTime=" + startTime, "timestamp=" + str(timestamp)]
    signedString = rightSign(paramslist, skey)
    print(host + api + "?" + signedString)


def card_in(cardNo, startTime):
    cardNo = cardNo
    api = r'/parking/api/in'
    timestamp = getNowTime()
    startTime = startTime
    paramslist = ["cardNo=" + cardNo, "startTime=" + startTime, "timestamp=" + str(timestamp)]
    signedString = rightSign(paramslist, skey)
    print(host + api + "?" + signedString)


def car_out(carNo):
    carNo = carNo
    api = r'/parking/api/out'
    timestamp = getNowTime()
    # timestamp = r'2016-11-15 23:25:45'
    paramslist = ["carNo=" + carNo, "timestamp=" + str(timestamp)]
    # paramslist = ["carNo=" + carNo, "timestamp=" + '2016-09-09 18:59:18']
    signedString = rightSign(paramslist, skey)
    print(host + api + "?" + signedString)


def force_out(carNo):
    carNo = carNo
    api = r'/parking/api/out'
    timestamp = getNowTime()
    # timestamp = r'2017-02-15 14:10:21'
    paramslist = ["carNo=" + carNo, "timestamp=" + str(timestamp),"force="+"true"]
    # paramslist = ["carNo=" + carNo, "timestamp=" + '2016-09-09 18:59:18']
    signedString = rightSign(paramslist, skey)
    print(host + api + "?" + signedString)

# def card_out(cardNo):

#     cardNo = cardNo
#     api = r'/parking/api/out'
#     # timestamp = getNowTime()
#     timestamp = '2016-10-05 21:22:45'
#     paramslist = ["cardNo=" + cardNo, "timestamp=" + str(timestamp)]
#     signedString = rightSign(paramslist, skey)
#     print(host + api + "?" + signedString)


def pay(carNo, startTime, money):
    carNo = carNo
    payWay = '6'
    api = r'/parking/api/pay'
    timestamp = getNowTime()
    # timestamp = '2018-06-10 18:24:39'
    startTime = startTime
    # payTime = '2018-12-26 10:24:39'
    payTime = timestamp
    money = money
    paramslist = ["startTime=" + startTime, "payTime=" + payTime, "money=" + str(money), "carNo=" + carNo,
                  "timestamp=" + str(timestamp),'payWay='+payWay]
    # paramslist = ["startTime=" + startTime, "payTime=" + payTime, "money=" + str(money), "carNo=" + carNo,
    #               "timestamp=" + str(timestamp)]
    signedString = rightSign(paramslist, skey)
    print(host + api + "?" + signedString)



if __name__ == "__main__":
    # carNo = r'陕AR06U3'
    payTime = getNowTime()
    carNo = r'鄂A888Y2'
    # carNo = '鄂A88AB7'
    # startTime = r'2017-02-23 23:28:48'
    startTime = r'2019-03-18 10:07:16'
    # timestamp = r'2016-10-05 21:22:47'
    money = 500
    car_in(carNo,startTime)
    query_car(carNo)
    pay(carNo,startTime,money)
    car_out(carNo)
    # force_out(carNo)
    # card_in(cardNo,startTime)
    # query_card(cardNo)
    # card_out(cardNo)
    # sqq_car_in(carNo,startTime)
    # sqq_query_car(carNo)
    # sqq_pay(carNo,startTime,money)
    # sqq_car_out(carNo)
    # sqq_force_out(carNo)


    # sign(tosign=sfsfsf,skey=sss)