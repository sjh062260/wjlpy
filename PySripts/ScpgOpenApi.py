#coding=utf-8
#! /usr/bin/env python

# Created on 2016?7?16?
# @author: jiaohui
import time,datetime,hashlib,os
import requests

# import sys
# import io

# ??????
# ????
# HOST = "http://posapi.scpretail.net/"   # openapi ????
# partnerId = "889431914afb9abea427aca9714d4731"
# skey = "suscpgpos"
# mcode = '898330260120001'
# posId = '58932101'
# mcode = '156194'
# posId = 'd28ef8a1'
# posType = 'liandipos'
# ????
# HOST = "http://openapi.dev.wanjianglong.net/"  # openapi????
# partnerId = "ae69da171f58c41b9df7dad9604e8e31"
# skey = "wpos"
# posType = 'wpos'
# mcode = '156225'
# posId = '50888515'
# posType = 'liandipos'
# mcode = '182043'
# posId = 'f7c9567c'


# ??
HOST = "http://sa-third-api.dev.wanjianglong.net/"
# HOST = "http://sa-third-api.sgtnt.scpretail.net/"
# HOST = "http://sa-third-api.sgtnt.scpgroup.com.cn/"

# ????
partnerId = "67e03ba7fc9664ba811d64d9c8a7fe6f"
skey = "liandiPos_hyxyc"
mcode = '156225'
posId = 'bfe4f64b'
posType = 'liandipos'

# partnerId = "814f55dfcbc7ff236fbc46a6b79367fe"
# skey = "wpos"
# mcode = '143112'
# posId = '9ab9475f'
# posType = 'wpos'

# ??mother's care
# partnerId = "67e03ba7fc9664ba811d64d9c8a7fe6f"
# skey = "liandiPos_hyxyc"
# mcode = '156225'
# posId = 'bfe4f64b'
# posType = 'liandipos'

# njxyc ?POS
# posId = 'c3fbdeb4'
# mcode = '154978'
# partnerId = "814f55dfcbc7ff236fbc46a6b79367fe"
# skey = "wpos"
# posType = 'wpos'

# jyxyc ?POS
# posId = '90006603'
# mcode = '141302256990541'
# partnerId = "35a89954073f53c00f9d3701c835909b"
# skey = "liandipos_jyxyc"
# posType = 'liandipos'

#csxyc ?POS
# posId = '9a9bfc41'
# mcode = '156647'
# partnerId = "814f55dfcbc7ff236fbc46a6b79367fe"
# skey = "wpos"
# posType = 'wpos'


# suxyc
# partnerId = "814f55dfcbc7ff236fbc46a6b79367fe"
# skey = "wpos"
# mcode = '143112'
# posId = 'bfe4f64b'
# posType = 'wpos'



# xxyxc
# partnerId = "59f8b87dfbade814691d7ecdca82e50a"
# skey = "WPOS_MSG"
# mcode = '898330156990553'
# posId = '06660174'
# posType = 'wpos'


# partnerId = "59f8b87dfbade814691d7ecdca82e50a"
# skey = "WPOS_MSG"
# mcode = '898330156990553'
# posId = '07770049'
# posType = 'wpos'

# njxyc
# partnerId = "814f55dfcbc7ff236fbc46a6b79367fe"
# skey = "wpos"
# mcode = '154978'
# posId = 'c3fbdeb4'
# posType = 'wpos'


# fsyxc wpos 
# partnerId = "814f55dfcbc7ff236fbc46a6b79367fe"
# skey = "wpos"
# posType = 'wpos'
# mcode = '208349'
# posId = 'ee571303'


# masxyc
# partnerId = "dfe61344b3995bbd24723f134d55cbe3"
# skey = "yspos"
# posType = 'yspos'
# mcode = '898340553110453'
# posId = '84367760'

#sz pos ???
# posId = '864536020085948'
# mcode = ''
# partnerId = "dfe61344b3995bbd24723f134d55cbe3"
# skey = "yspos"
# posType = 'yspos'

#sz A8 ??POS
# posId = '43053015'
# mcode = '898440353114305'
# partnerId = "814f55dfcbc7ff236fbc46a6b79367fe"
# skey = "wpos"
# posType = 'wpos'

#sz ?POS
# posId = '43053017'
# mcode = '898440353114305'
# partnerId = "b4a9188c3c930264d8e96f8332d10da5"
# skey = "WPOS_MSG"
# posType = 'wpos'

# gdyxc pos ???
# posId = '08880021'
# mcode = '898330158129035'
# partnerId = "dfe61344b3995bbd24723f134d55cbe3"
# skey = "yspos"
# posType = 'yspos'


# sdxyc pos ???
# posId = '84713339'
# mcode = '8215880569100ZQ'
# partnerId = "dfe61344b3995bbd24723f134d55cbe3"
# skey = "yspos"
# posType = 'yspos'


# posId = '33273508'
# mcode = '898330254510610'
# partnerId = "e2ee6a949a03fab193091ed2b092e058"
# skey = "liandiPos"
# posType = 'liandiPos'

TIMEFORMAT = "%Y-%m-%d %H:%M:%S"


# ??????
def get_now_time ():
    nowTime = time.strftime (TIMEFORMAT)
    return nowTime

# ??params ?signKey?????sign
def right_sign (params):
    params = params
    params.sort ()
    paramsstring = ''
    for line in params:
        paramsstring = paramsstring + line + '&'
    signString = paramsstring + 'skey=' + skey
    # sign = hashlib.md5(signString.encode('utf-8')).hexdigest()
    sign = hashlib.md5(signString.encode()).hexdigest()
    signedString = paramsstring + 'sign=' + sign
    return signedString

def signString (params):
    params = params
    params.sort ()
    paramsstring = ''
    for line in params:
        paramsstring = paramsstring + line + '&'
    signString = paramsstring + 'skey=' + skey
    # sign = hashlib.md5(signString.encode('utf-8')).hexdigest()
    sign = hashlib.md5(signString.encode()).hexdigest()
    return sign

# ?????
def queryTicketByMobile(mobile):
    # mobile = mobile
    timestamp = get_now_time()
    params = ["posType=" + posType, "partnerId=" + partnerId,  "posId=" + posId,"mcode="+mcode,"mobile="+mobile,"timestamp=" + str (timestamp)]
    signedString = right_sign (params)
    url = 'third/crm/queryTicketByMobile'
    print (HOST + url+'?' + signedString)

# ????
def recognizeMember():
    # mobile = mobile
    timestamp = get_now_time()
    params = ["posType=" + posType, "partnerId=" + partnerId,  "posId=" + posId,"mcode="+mcode,"timestamp=" + str (timestamp)]
    signedString = right_sign (params)
    url = 'third/crm/recognizeMember'
    print (HOST + url+'?' + signedString)

# ???
def tickInfo(tickNo):
    tickNo = tickNo
    timestamp = get_now_time()
    params = ["posType=" + posType, "partnerId=" + partnerId, "tickNo=" + tickNo, "posId=" + posId,"mcode="+mcode,"timestamp=" + str (timestamp)]
    signedString = right_sign (params)
    url = 'third/crm/tickInfo'
    print (HOST + url+'?' + signedString)


# ???????
def expendCoupon(tickNo):
    tickNo = tickNo
    timestamp = get_now_time()
    params = ["posType=" + posType, "partnerId=" + partnerId, "tickNo=" + tickNo, "posId=" + posId,"mcode="+mcode,"timestamp=" + str (timestamp)]
    signedString = right_sign (params)
    url = 'third/crm/expendCoupon'
    print (HOST + url+'?' + signedString)


# ????
def cancel(type,originalOrderNo,refundAmount):
    type = type
    originalOrderNo = originalOrderNo
    refundAmount = refundAmount
    timestamp = get_now_time()
    params = ["posType=" + posType, "partnerId=" + partnerId, "type=" + type,"originalOrderNo=" + originalOrderNo, "refundAmount=" + refundAmount,  "posId=" + posId,"mcode="+mcode,"timestamp=" + str (timestamp)]
    sign = signString(params)
    signedString = right_sign (params)
    url = 'third/crm/cancel'
    print (HOST + url+'?' + signedString)
    playload = {"posType":posType,"partnerId":partnerId,"type":type,"originalOrderNo":originalOrderNo,"refundAmount":refundAmount,"mcode":mcode,"posId":posId,"timestamp":str (timestamp),"sign":sign}
    url = HOST + url
    r = requests.post(url,data=playload)
    print(r.content)


# ????
def submitOrder_post(order,tickNo,externalCoupons):
    tickNo = tickNo
    order = order
    externalCoupons = externalCoupons
    timestamp = get_now_time()
    params = ["posType=" + posType, "partnerId=" + partnerId, "tickNo=" + tickNo, "order="+order,"posId=" + posId,"mcode="+mcode,"externalCoupons="+externalCoupons,"timestamp=" + str (timestamp)]
    # params = ["posType=" + posType, "partnerId=" + partnerId, "tickNo=" + "", "order="+order,"posId=" + posId,"mcode="+mcode,"externalCoupons="+"","timestamp=" + str (timestamp)]
    sign = signString(params)
    signedString = right_sign (params)
    url = 'third/crm/submitOrder'
    print (HOST + url+'?' + signedString)
    # playload = {"posType":posType,"partnerId":partnerId,"tickNo":tickNo,"order":order,"posId":posId,"mcode":mcode,"externalCoupons":externalCoupons,"timestamp":str (timestamp),"sign":sign}
    # url = HOST + url
    # r = requests.post(url,data=playload)
    # print(r.text).decode('utf-8').encode('cp936') 



# ??????
def tradeNotify(orderNo,isSuccess,payMethod,terminalNo,buyerId,payAmount):
    orderNo = orderNo
    isSuccess = isSuccess
    payMethod = payMethod
    terminalNo = terminalNo
    buyerId = buyerId
    payAmount = payAmount
    # thirdTradeNo = thirdTradeNo
    timestamp = get_now_time()
    # params = ["posType=" + posType, "partnerId=" + partnerId, "isSuccess=" + isSuccess,"payMethod="+ payMethod,"terminalNo="+terminalNo,"buyerId="+buyerId,"payAmount="+payAmount,"orderNo="+orderNo,"posId=" + posId,"mcode="+mcode,"timestamp=" + str (timestamp),"thirdTradeNo="+thirdTradeNo]
    params = ["posType=" + posType, "partnerId=" + partnerId, "isSuccess=" + isSuccess,"payMethod="+ payMethod,"terminalNo="+terminalNo,"buyerId="+buyerId,"payAmount="+payAmount,"orderNo="+orderNo,"posId=" + posId,"mcode="+mcode,"timestamp=" + str (timestamp)]
    signedString = right_sign (params)
    sign = signString(params)
    url = 'third/crm/tradeNotify'
    print (HOST + url+'?' + signedString)
    # playload = {"posType":posType,"partnerId":partnerId, "isSuccess":isSuccess,"thirdTradeNo":thirdTradeNo,"payMethod":payMethod,"terminalNo":terminalNo,"buyerId":buyerId,"payAmount":payAmount,"orderNo":orderNo,"posId":posId,"mcode":mcode,"timestamp":str (timestamp),"sign":sign}
    playload = {"posType":posType,"partnerId":partnerId, "isSuccess":isSuccess,"terminalNo":terminalNo,"payMethod":payMethod,"buyerId":buyerId,"payAmount":payAmount,"orderNo":orderNo,"posId":posId,"mcode":mcode,"timestamp":str (timestamp),"sign":sign}
    url = HOST + url
    # r = requests.get(url,params = playload)
    # print(r.url)
    # print(r.content)
    r = requests.post(url,data=playload)
    # print(r.url)
    print(r.content)

# ????????
def mktInfo(orderNo):
    orderNo = orderNo
    timestamp = get_now_time()
    params = ["posType=" + posType, "partnerId=" + partnerId, "orderNo=" + orderNo, "posId=" + posId,"mcode="+mcode,"timestamp=" + str (timestamp)]
    signedString = right_sign (params)
    url = 'third/crm/mktInfo'
    print (HOST + url+'?' + signedString)

# ????
def getPreUrl():
    timestamp = get_now_time()
    params = ["posType=" + posType, "partnerId=" + partnerId,  "posId=" + posId,"mcode="+mcode,"timestamp=" + str (timestamp)]
    signedString = right_sign (params)
    url = 'third/crm/getPreUrl'
    print (HOST + url+'?' + signedString)

def updateThirdTradeNo(orderNo,thirdTradeNo):
    orderNo = orderNo
    thirdTradeNo = thirdTradeNo
    timestamp = get_now_time()
    params = ["posType=" + posType, "partnerId=" + partnerId,  "posId=" + posId,"mcode="+mcode,"timestamp=" + str (timestamp),"orderNo="+orderNo,"thirdTradeNo="+thirdTradeNo]
    signedString = right_sign(params)
    url = 'third/crm/updateThirdTradeNo'
    print(HOST+url+'?'+signedString)



if __name__ == "__main__":
    # print(time.ctime())
    start = time.ctime()
    # queryTicketByMobile(mobile='18627169820')
    # tickInfo(tickNo= '187494333806294')
    # expendCoupon(tickNo='123331064687909')
    # recognizeMember()
    # ????
    # tickNo = '[2018014230000002]'
    tickNo = '[]'
    # tickNo = 'null'
    # order  = '{"totalFee":"40000","orderNo":"201802260016","actTotalFee":"40000","memberId":"51800000118058000005","telephone":"16524217654","couponDiscValue":"0","state":"2","payMethod":"1"}'
    # order  = '{"totalFee":"100","orderNo":"2018020400007","actTotalFee":"100","memberId":"","telephone":"","couponDiscValue":"0","state":"2","payMethod":"2"}'
    # order  = '{"totalFee":"1000","orderNo":"20180313000003","actTotalFee":"1000","memberId":"","telephone":"","couponDiscValue":"0","state":"2","payMethod":"1"}'
    # order  = '{"totalFee":"10000","orderNo":"201803130000037","actTotalFee":"10000","memberId":"","telephone":"","couponDiscValue":"0","state":"2","payMethod":"1"}'
    # ??
    # order  = '{"totalFee":"10000","orderNo":"201803200000001","actTotalFee":"10000","memberId":"51800000118079000130","telephone":"18627169820","couponDiscValue":"0","state":"2","payMethod":"1"}'
    order  = '{"totalFee":"100","orderNo":"20180918000006","actTotalFee":"100","memberId":"","telephone":"","couponDiscValue":"0","state":"1","payMethod":"1"}'
    # ???????9
    # order  = '{"totalFee":"10000","orderNo":"20180209000008","actTotalFee":"10000","memberId":"","telephone":"","couponDiscValue":"0","state":"2","payMethod":"01"}'
    # order  = '{"totalFee":"1000","orderNo":"20180205000007","actTotalFee":"1000","memberId":"51800000118036000003","telephone":"18627169820","couponDiscValue":"0","state":"1","payMethod":"01"}'
    # order  = '{"totalFee":"1000","orderNo":"2018010510510001","actTotalFee":"1000","memberId":"","telephone":"","couponDiscValue":"","state":"2","payMethod":"1"}'
    # order  = '{"totalFee":"19900","orderNo":"843677602017090800001","actTotalFee":"100","memberId":"51800000117241000002","telephone":"","couponDiscValue":"0","state":"1","payMethod":"1"}'
    # order  = '{"totalFee":"1","orderNo":"332735082017092500002","actTotalFee":"1","memberId":"","telephone":"","couponDiscValue":"0","state":"1","payMethod":"9","thirdTradeNo":"P332735082017092500002"}'
    # order  = '{"totalFee":"9900","orderNo":"60001562250204","actTotalFee":"9900","telephone":"18627169820","couponDiscValue":"0","state":"1","payMethod":"2"}'
    # order  = '{"totalFee":"10000","orderNo":"60001562250121","actTotalFee":"10000","couponDiscValue":"0","state":"1",memberId:"77811170103163210304293"}'
    # "totalFee":"9900",
    # externalCoupons = '[{"couponCode":"100146240","dealTitle":"???5??","dealValue":500,"count":2,"totalValue":1000,"channel":1},{"couponCode":"100146241","dealTitle":"???10???","dealValue":1000,"count":1,"totalValue":1000,"channel":2}]'
    externalCoupons = '[]'
    submitOrder_post(order,tickNo,externalCoupons)

    # ??????
    # tradeNotify(orderNo='201802260009',isSuccess='true',payAmount='40000',payMethod='01',terminalNo='2018022600009',buyerId='')
    # tradeNotify(orderNo='2017122700013236',isSuccess='true',payAmount='4000',payMethod='12',terminalNo='100014311220170808003000005',buyerId='47011160420095124906437')
    # tradeNotify(orderNo='201712270001323',isSuccess='true',payAmount='4000',payMethod='9',terminalNo='1000143112201708083200000005',buyerId='47011160420095124906437',thirdTradeNo='P2017082900003204')
    # for i in range(10):
    #     print get_now_time()
    #     tradeNotify(orderNo='60001562250129',isSuccess='true',payAmount='5000',payMethod='3',terminalNo='133567',buyerId='77811170103163210304293')

    # ????
    type = '3'
    originalOrderNo = '201803200000005'
    refundAmount = '1000'
    time1 = time.time()
    # cancel(type,originalOrderNo,refundAmount)
    time2 = time.time()
    print(time2-time1)
    # getPreUrl()
    # mktInfo(orderNo = '201708062235006')
    orderNo = '20171020000002'
    thirdTradeNo = 'T20171020000003'
    # updateThirdTradeNo(orderNo,thirdTradeNo)
    
