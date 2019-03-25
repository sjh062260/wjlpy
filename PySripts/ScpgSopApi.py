#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

# Created on 2016年7月16日
# @author: jiaohui
import time,datetime,hashlib,os
import requests

# 全局参数定义

# HOST = "http://sop.demo.shangquanquan.com/api"  # sop开发环境
# HOST = "http://sop.scpretail.net/api"  # sop产品环境
HOST = "http://sop.scpgroup.com.cn/api"  # sop产品环境
# 天津多门
# APPID = "ea4fd5ec4bf33a997b1760b5721e027f"
# APPSECRET = "doormen-tj"
# APPID="886f8fbd2523b882098a3fe0b054d39b"  # 天津测试
# APPSECRET="tj6ceng-test"
# APPID = "doormen-xxyxc"  # 西溪测试
# APPSECRET = "e3deb2ebce429926072c86703825cfbf"
# APPID = "de74cfa7727bb73ce0defe4e1eec4a15"
# APPSECRET = "lifang_xxyxc"
# APPID = "344a1a36b37f4bb488e2283a2c1a6dff"
# APPSECRET = "9b94d7a4a7b5e3de97d188ff20e96817"
# APPID = "doormen"     #西安
# APPSECRET = "e3deb2ebce429926072c86703825cfbf"
# APPID = "25c825eb086fa993962dd1e1bae910b4"   
# APPSECRET = "wifi_portal_sz"
# APPID = "46a0770fbfe73a930a3802cca5eb2003"
# APPSECRET = "yepside-nbyxc-test"
# APPID = "46a0770fbfe73a930a3802cca5eb2004"
# APPSECRET = "yepside-xxyxc-test"
# APPID = "doormen"
# APPSECRET = "46a0770fbfe73a930a3802cca5eb2003"
# APPID = "bddedda630412b0fe07e9d315ef9e72f"
# APPSECRET = "aotian-tj"
# APPID="eed97d47504f2de4ddc97b1671dc0360"
# APPSECRET="lingjuliwangluo-test"
# HOST = "http://sop.scpretail.net/api"  # sop产品环境
# APPID="344a1a36b37f4bb488e2283a2c1a6dff"
# APPSECRET="9b94d7a4a7b5e3de97d188ff20e96817"
APPID="886f8fbd2523b882098a3fe0b054d39b"
APPSECRET="tj6ceng-tjyxc"

###  POS
# HOST = http://openapi.dev.wanjianglong.net/
# HOST = http://openapi.scpretail.net/
# skey = test
# partnerId = test


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
    # print(signString)
    sign = hashlib.md5(signString.encode()).hexdigest()
    signedString = paramsstring + 'sign=' + sign
    return signedString
    # return sign


# 会员注册 带openId
def user_register_openId (mobile,openId):
    method = "user.register"
    mobile = mobile
    authcode = "81402"
    openId=openId
    timestamp = get_now_time ()
    params = ["method=" + method, "appId=" + APPID, "mobile=" + mobile, "authcode=" + authcode,"openId="+openId,
              "timestamp=" + str (timestamp)]
    signedString = right_sign (params, APPSECRET)
    print (HOST + '?' + signedString)

# 会员注册
def user_register_mobile (mobile):
    method = "user.register"
    mobile = mobile
    authcode = "81402"
    gender = '1'
    name = 'sjhs'
    birthday = '2017-01-01'
    # openId="suolqeoudlqeuoualaeoq45"
    timestamp = get_now_time ()
    # params = ["method=" + method, "appId=" + APPID, "gender="+gender,"name="+name,"birthday="+birthday,"mobile=" + mobile, "authcode=" + authcode,
    #           "timestamp=" + str (timestamp)]
    params = ["method=" + method, "appId=" + APPID,"mobile=" + mobile, "authcode=" + authcode,"timestamp=" + str(timestamp)]
    signedString = right_sign (params, APPSECRET)
    # params["sign"] = signedString
    # print (HOST + '?' + signedString)
    # params_data = dict(i.split("=") for i in params)
    # params_data["sign"] = signedString
    # r = requests.post(url = HOST,data=params_data)
    # print r.content
    signString = right_sign (params, APPSECRET)
    # print （signString）
    print (HOST + '?' + signedString)
    # params_data = dict(i.split("=") for i in params)
    # params_data["sign"] = signString
    # r = requests.post(url = HOST,data=params_data)
    # print r.content


# 会员注册-无需注册码
def user_register_mobile_noAuthCode (mobile):
    method = "user.registerNoAuthcode"
    mobile = mobile
    # authcode = ""
    gender = '1'
    # name = 'ces%2bst%2bsr'
    name = '石教会'
    birthday = '2017-01-01'
    # openId="suolqeoudlqeuoualaeoq45"
    timestamp = get_now_time ()
    params = ["method=" + method, "appId=" + APPID, "gender="+gender,"name="+name,"birthday="+birthday,"mobile=" + mobile, 
              "timestamp=" + str (timestamp)]
    signedString = right_sign (params, APPSECRET)
    print (HOST + '?' + signedString)

# 会员查询
def user_query (mobile):
    method = "user.query"
    mobile = mobile
    timestamp = get_now_time ()
    # timestamp = "2016-10-01 10:26:20"
    params = ["method=" + method, "appId=" + APPID, "mobile=" + mobile, "timestamp=" + str (timestamp)]
    signedString = right_sign (params, APPSECRET)
    print (HOST + '?' + signedString)
    # signString = right_sign (params, APPSECRET)
    # params_data = dict(i.split("=") for i in params)
    # params_data["sign"] = signString
    # r = requests.post(url = HOST,data=params_data)
    # print r.content


# 更新会员信息
def user_update ():
    method = "user.update"
    birthday = "1987-12-19"
    cardno = "0130000001344078"
    gender = "2"
    idno = "420281198711214297"
    mobile = "18848159822"
    name = "sjh".encode()
    timestamp = get_now_time ()
    params = ["method=" + method, "appId=" + APPID, "mobile=" + mobile, "timestamp=" + str (timestamp),
              "birthday=" + birthday, "cardno=" + cardno, "gender=" + gender, "idno=" + idno, "name=" + name]
    # params = ["method=" + method, "appId=" + APPID, "mobile=" + mobile, "timestamp=" + str (timestamp),
    #           "birthday=" + birthday, "cardno=" + cardno, "gender=" + gender, "name=" + name]
    signedString = right_sign (params, APPSECRET)
    print (HOST + '?' + signedString)


# 短信验证码
def get_authcode (mobile):
    method = "user.getAuthcode"
    timestamp = get_now_time ()
    # timestamp = "2016-12-13 12:52:12"
    params = ["method=" + method, "appId=" + APPID, "mobile=" + mobile, "timestamp=" + str (timestamp)]
    signedString = right_sign (params, APPSECRET)
    print (HOST + '?' + signedString)


# 会员积分变更
def point_update (mobile,point):
    method = "point.update"
    # mobile = "18627169820"
    timestamp = get_now_time ()
    # point = "600"
    remark = "积分测试"
    params = ["method=" + method, "appId=" + APPID, "mobile=" + mobile,
              "timestamp=" + str (timestamp), "point=" + point, "remark=" + remark]
    signedString = right_sign (params, APPSECRET)
    print (HOST + '?' + signedString)


# 会员登录
def login_check ():
    method = "user.loginCheck"
    mobile = "18627169820"
    authcode = "81402"
    cardno = "307666050737"
    timestamp = get_now_time ()
    params = ["method=" + method, "appId=" + APPID, "mobile=" + mobile, "cardno=" + cardno,
              "authcode=" + authcode, "timestamp=" + str (timestamp)]
    signedString = right_sign (params, APPSECRET)
    print (HOST + '?' + signedString)


# 查询劵详情
def ticket_detail (tickId):
    method = "ticket.detail"
    tickId = tickId
    timestamp = get_now_time ()
    params = ["method=" + method, "appId=" + APPID, "tickId=" + tickId, "timestamp=" + str (timestamp)]
    signedString = right_sign (params, APPSECRET)
    print (HOST + '?' + signedString)

# 根据手机号查询已有券信息
def queryTicketByMobile (mobile):
    method = "crm.queryTicketByMobile"
    # mobile = mobile
    timestamp = get_now_time ()
    params = ["method=" + method, "appId=" + APPID, "mobile=" + mobile, "timestamp=" + str (timestamp)]
    signedString = right_sign (params, APPSECRET)
    print (HOST + '?' + signedString)


# 购买优惠券
def ticket_buy (mobile,tickId):
    # tickId = "77841161104171849280582"
    # mobile = "18627169820"
    remark = "test"
    timestamp = get_now_time ()
    method = "ticket.buy"
    params = ["method=" + method, "appId=" + APPID, "tickId=" + tickId, "remark=" + remark, "mobile=" + mobile,
              "timestamp=" + str (timestamp)]
    signedString = right_sign (params, APPSECRET)
    # signedString = "1801"
    print (HOST + '?' + signedString)

# 核销优惠券
def ticket_used (storeId,tickNo):
    timestamp = get_now_time ()
    method = "appApi.appCheckUseTick"
    params = ["method=" + method, "appId=" + APPID, "tickNo=" + tickNo, "storeId=" + storeId, "timestamp=" + str (timestamp)]
    signedString = right_sign (params, APPSECRET)
    # signedString = "1801"
    print (HOST + '?' + signedString)

# 注册发劵
def regAndSend (mobile,tickId):
    # tickId = "91741161028181335736251"  # 西安未央
    # tickId = "77841161104171849280582" # XIXI
    # tickId = "56441161103230912527665"
    # tickId = "77841170330170111827490"
    # 56441161103230912527665，77841161101151938004161
    # 77841161109203730621084，77841161110194247608148
    # 41541161110000839187765
    # 77841161110183630482789
    # mobile = "18627169820"
    remark = "test"
    name ="test"
    timestamp = get_now_time ()
    method = "ticket.regAndSend"
    birthday = '1987-12-21'
    gender = 2
    params = ["method=" + method, "birthday=" + birthday, "gender=" + str(gender), "appId=" + APPID,
              "tickId=" + tickId, "mobile=" + mobile,"name="+name,
              "timestamp=" + str(timestamp)]
    signedString = right_sign (params, APPSECRET)
    print (HOST + '?' + signedString)

# 抽奖码
def point_check_code ():
    code = "111111"
    method = "point.checkCode"
    timestamp = get_now_time ()
    params = ["method=" + method, "code=" + code, "appId=" + APPID, "timestamp=" + str (timestamp)]
    signedString = right_sign (params, APPSECRET)
    print (HOST + '?' + signedString)

def ticket_pointList (minPoint,maxPoint):
    method = "ticket.pointList"
    timestamp = get_now_time ()
    params = ["method=" + method, "minPoint=" + minPoint,"maxPoint="+maxPoint, "appId=" + APPID, "timestamp=" + str (timestamp)]
    signedString = right_sign (params, APPSECRET)
    print (HOST + '?' + signedString)

def crm_recognizeMember ():
    posType = "yspos"
    method = "crm.recognizeMember"
    timestamp = get_now_time ()
    posId = "bfe4f64b"
    mcode = "143112"
    mobile = "18627169820"
    params = ["method=" + method, "posId=" + posId,"posType="+posType,"mcode="+mcode,"mobile="+mobile, "appId=" + APPID, "timestamp=" + str (timestamp)]
    signedString = right_sign (params, APPSECRET)
    print (HOST + '?' + signedString)

# 字典表配置的品牌优惠标签活动
def brandDiscount():
    method = 'tenant.brandDiscount'
    num = '99999'
    start = '1'
    timestamp = get_now_time()
    params = ["method=" + method, "num=" + num,"start="+start,"timestamp=" + str (timestamp),"appId=" + APPID]
    signedString = right_sign (params, APPSECRET)
    print (HOST + '?' + signedString)

def tenantActivity():
    method = 'tenant.tenantActivity'
    num = '99999'
    start = '1'
    timestamp = get_now_time()
    params = ["method=" + method, "num=" + num,"start="+start,"timestamp=" + str (timestamp),"appId=" + APPID]
    signedString = right_sign (params, APPSECRET)
    print (HOST + '?' + signedString)

def memberActivity():
    method = 'tenant.memberActivity'
    num = '99999'
    start = '1'
    timestamp = get_now_time()
    params = ["method=" + method, "num=" + num,"start="+start,"timestamp=" + str (timestamp),"appId=" + APPID]
    signedString = right_sign (params, APPSECRET)
    print (HOST + '?' + signedString)

def memberDiscount():
    method = 'tenant.memberDiscount'
    num = '99999'
    start = '1'
    timestamp = get_now_time()
    params = ["method=" + method, "num=" + num,"start="+start,"timestamp=" + str (timestamp),"appId=" + APPID]
    signedString = right_sign (params, APPSECRET)
    print (HOST + '?' + signedString)

def storeList():
    method = 'tenant.storeList'
    num = '99'
    start = '1'
    timestamp = get_now_time()
    params = ["method=" + method, "num=" + num,"start="+start,"timestamp=" + str (timestamp),"appId=" + APPID]
    signedString = right_sign (params, APPSECRET)
    print (HOST + '?' + signedString)
    resp = requests.get(url=HOST,params = signedString)
    print(resp.text)


def activityRegStaNotify():
    method = 'activity.regStaNotify'
    first = '通知内容：制作完成'
    subject = '活动名称'
    openId = 'oa1P4s-jaWST3zZL1fjy4Qupty4c'
    url = 'http://wx.xxyxc.demo.shangquanquan.com/g/weixin/link/withOpenIdAndMobile?url=http://xxx.com/7/app/./index.php?i=3@c=entry@incity_openid=1@do=Index@m=incity_kumamon'
    time = get_now_time()
    timestamp = get_now_time()
    remark = '活动备注'
    params = ["method=" + method,"remark=" + remark,"time=" + time,"openId=" + openId, "url=" + url,"first=" + first,"subject="+subject,"timestamp=" + str (timestamp),"appId=" + APPID]
    signedString = right_sign (params, APPSECRET)
    print (HOST + '?' + signedString)
    

def change(tenantId,value):
    method = "/change"
    tenantId = tenantId
    value = value
    timestamp = get_now_time()
    params = ["tenantId="+tenantId,"value="+value,"appId=" + APPID,"timestamp=" + str (timestamp)]
    signedString = right_sign(params,APPSECRET)
    print(HOST+method+"?"+signedString)






if __name__ == "__main__":
    # user_register_mobile(mobile="15601586255")
    # user_register_openId(mobile="18848159822",openId="162740sfsue73s1sjda82s014s")
    # user_register_mobile_noAuthCode(mobile = '18619241431')
    # user_query (mobile="18627169820")
    # user_query (mobile="18627169820")
    # user_query (mobile="13389282551")
    # queryTicketByMobile(mobile = '18627169820')
    # user_update ()
    # get_authcode (mobile = '18627169820')
    # point_update (mobile='18627169820',point='13')
    # point_update (mobile='18627169820',point='13.345')
#    point_update (mobile='18627169820',point='13.86')
#    point_update (mobile='18627169820',point='378')
#    point_update (mobile='18627169820',point='-13')
#    point_update (mobile='18627169820',point='-13.345')
#    point_update (mobile='18627169820',point='-13.86')
#    point_update (mobile='18627169820',point='-378')
    # login_check ()
    # ticket_detail (tickId = '77841161221155705001948')
    # ticket_buy (mobile = '18627169820',tickId = '77841180118233545679545')
    # ticket_buy (mobile = '18607227615',tickId = '77841170104140345248948')
    # point_check_code ()
    # crm_recognizeMember()
    # regAndSend(mobile = '18633333334',tickId = '77841170815211115790075')
    # ticket_pointList(minPoint='',maxPoint='50')
    # brandDiscount()
    # memberDiscount()
    # tenantActivity()
    # memberActivity()
    storeList()
    # activityRegStaNotify()
    # ticket_used(tickNo='127729264746219',storeId ='77831161121111739212624')
    # queryTicketByMobile(mobile = '18627169820')
    # change(tenantId = "518000001",value = '2')