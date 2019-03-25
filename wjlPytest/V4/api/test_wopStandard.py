#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

"""
@author:sjh
@time:2018/6/2 12:00
"""
import requests
import pytest
import time, hashlib
import wjlTestLib
# from api import wopV4Lib
import wopV4Lib

TIMEFORMAT = "%Y-%m-%d %H:%M:%S"


def get_now_time():
    nowTime = time.strftime(TIMEFORMAT)
    return str(nowTime)

class TestWopStandard:
    host = "https://open.dev4.wanjianglong.net"
    group_id = '1008'
    tenant_id = '4018'
    appId = '3jlzawqq'
    appSecret = 'fmmpzwfdy1xq881raexhe6nw'
    # appId='5ejszzr3'
    # appSecret = 'l87vec365y4vevg6jkfpjf1y'
    storeId = '1090171090007'
    memberIds = {
        "normal_mobile":"17152713118",
        "normal_memberId":"12000118157000004",
        "crmUid":"2025664"
    }
    couponIds = {
        "online_couponId":"4021181580003",
        "autodown_couponId":"4021181580005"
    }
    parking = {
        "parkCodeA":"A",
        "parkCodeB":"B",
        "plateNo":"鄂A88888",
        "inPlace":"软件园中路",
        "outPlace":"南湖大道",
        "enterTime":str(time.strftime(TIMEFORMAT,time.localtime(time.time()-8*60*60)))
    }
    openIds = ['osAL-til7iQncz-BtxkEFehdtdDw','oa1P4s1aMzyX820eqXR60oHdMkEI']
    timestamp = get_now_time()
    comParams = {
        "appId": appId,
        "groupId": group_id,
        "tenantId": tenant_id,
        "reqMode": '0101',
        "timestamp": timestamp,
    }
    # registe_mobile = wopV4Lib.get_random_phonenumber()
    # outOrderNo = wopV4Lib.get_random_outorderno()
    # couponNo = wopV4Lib.downloadCoupon(host,comParams,appSecret,memberIds.get("normal_memberId"),couponIds.get("autodown_couponId"))

    # def test_getTenantInfo(self):
    #     print("******** getTenantInfo start ********")
    #     url = self.host+"/mall/getTenantInfo"
    #     params = copy.copy(self.comParams)
    #     params["timestamp"] = get_now_time()
    #     sign = wopV4Lib.right_sign(params,self.appSecret)
    #     params["sign"] = sign
    #     resp = requests.post(url,data=params)
    #     print(resp.json())
    #     assert resp.status_code == 200
    #     assert self.tenant_id in resp.text
    #     assert (resp.elapsed.microseconds/1000000)<2
    #
    # def test_getCategoryList(self):
    #     print("******** getCategoryList start ********")
    #     url = self.host+"/mall/getCategoryList"
    #     params = copy.copy(self.comParams)
    #     params["timestamp"] = get_now_time()
    #     sign = wopV4Lib.right_sign(params,self.appSecret)
    #     params["sign"] = sign
    #     resp = requests.post(url,data=params)
    #     print(resp.text)
    #     assert resp.status_code == 200
    #     assert self.tenant_id in resp.text
    #     assert (resp.elapsed.microseconds/1000000)<2
    #
    # def test_getStoreList(self):
    #     print("******** getStoreList start ********")
    #     url = self.host+"/mall/getStoreList"
    #     params = copy.copy(self.comParams)
    #     params["timestamp"] = get_now_time()
    #     sign = wopV4Lib.right_sign(params,self.appSecret)
    #     params["sign"] = sign
    #     resp = requests.post(url,data=params)
    #     print(resp.json())
    #     assert resp.status_code == 200
    #     assert self.tenant_id in resp.text
    #     assert (resp.elapsed.microseconds/1000000)<2
    #
    # def test_getStoreInfo(self):
    #     print("******** getStoreInfo start ********")
    #     url = self.host+"/mall/getStoreInfo"
    #     params = copy.copy(self.comParams)
    #     params["timestamp"] = get_now_time()
    #     data = {
    #         "storeId":self.storeId
    #     }
    #     params["data"] = str(data)
    #     sign = wopV4Lib.right_sign(params,self.appSecret)
    #     params["sign"] = sign
    #     resp = requests.post(url,data=params)
    #     print(resp.text)
    #     assert resp.status_code == 200
    #     assert self.storeId in resp.text
    #     assert (resp.elapsed.microseconds/1000000)<2
    #
    # def test_getGradeList(self):
    #     print("******** getGradeList start ********")
    #     url = self.host+"/member/getGradeList"
    #     params = copy.copy(self.comParams)
    #     params["timestamp"] = get_now_time()
    #     sign = wopV4Lib.right_sign(params,self.appSecret)
    #     params["sign"] = sign
    #     resp = requests.post(url,data=params)
    #     print(resp.text)
    #     assert resp.status_code == 200
    #     assert "code" in resp.text
    #     assert (resp.elapsed.microseconds/1000000)<2

    def test_getMemberInfo_Mobile(self):
        print("******** getMemberInfo start ********")
        url = self.host+"/member/getMemberInfo"
        params = self.comParams
        # params["timestamp"] = get_now_time()
        params["timestamp"] = '2018-10-11 17:22:43'
        data = {
            "queryType":5,
            "queryValue":self.memberIds.get("crmUid")
        }
        params["data"] = str(data)
        sign = wopV4Lib.right_sign(params,self.appSecret)
        params["sign"] = sign
        print(params)
        resp = requests.post(url,data=params)
        print(resp.text)
        assert resp.status_code == 200
        assert self.memberIds.get("normal_mobile") in resp.text
        assert (resp.elapsed.microseconds/1000000)<2

    # def test_getMemberInfo_MemberId(self):
    #     print("******** getMemberInfo start ********")
    #     url = self.host+"/member/getMemberInfo"
    #     params = copy.copy(self.comParams)
    #     params["timestamp"] = get_now_time()
    #     data = {
    #         "queryType":1,
    #         "queryValue":self.memberIds.get("normal_memberId")
    #     }
    #     params["data"] = str(data)
    #     sign = wopV4Lib.right_sign(params,self.appSecret)
    #     params["sign"] = sign
    #     # print(params)
    #     resp = requests.post(url,data=params)
    #     print(resp.text)
    #     assert resp.status_code == 200
    #     assert self.memberIds.get("normal_memberId") in resp.text
    #     assert (resp.elapsed.microseconds/1000000)<2
    #
    # #
    # def test_sendSMSVerifyCode(self):
    #     print("******** sendSMSVerifyCode start ********")
    #     url = self.host+"/msg/sendSMSVerifyCode"
    #     params = copy.copy(self.comParams)
    #     params["timestamp"] = get_now_time()
    #     mobile = self.memberIds.get("normal_mobile")
    #     data = {
    #         "mobile":mobile
    #     }
    #     params["data"] = str(data)
    #     sign = wopV4Lib.right_sign(params,self.appSecret)
    #     params["sign"] = sign
    #     resp = requests.post(url,data=params)
    #     resp_data = resp.json()
    #     code = resp_data.get("data").get("code")
    #     return code
    #     # print(code)
    #     assert resp.status_code == 200
    #     assert len(code) == 6
    #     assert (resp.elapsed.microseconds/1000000)<2
    #
    #
    # def test_register(self):
    #     print("******** register start ********")
    #     url = self.host+"/member/register"
    #     params = copy.copy(self.comParams)
    #     params["timestamp"] = get_now_time()
    #     registe_code = wopV4Lib.sendSMSVerifyCode(self.host,self.comParams,self.appSecret,self.registe_mobile)
    #     data = {
    #         "mobile":self.registe_mobile,
    #         "authCode":registe_code
    #     }
    #     params["data"] = str(data)
    #     sign = wopV4Lib.right_sign(params,self.appSecret)
    #     params["sign"] = sign
    #     resp = requests.post(url,data=params)
    #     print(resp.text)
    #     assert resp.status_code == 200
    #     # assert self.memberIds.get("normal_memberId") in resp.text
    #     assert (resp.elapsed.microseconds/1000000)<2
    #
    # def test_modify(self):
    #     print("******** modify start ********")
    #     url = self.host+"/member/modify"
    #     params = copy.copy(self.comParams)
    #     params["timestamp"] = get_now_time()
    #     data = {
    #         "memberId":wopV4Lib.getMemberInfo_Mobile(self.host,self.comParams,self.appSecret,self.registe_mobile),
    #         "nickName":"sjh",
    #         "realName":"时间懊悔",
    #         "headPic":"http://thirdwx.qlogo.cn/mmopen/qbCfqcice6mBLL0rXxiayia503txxCl4FTSvuPiaoF3aJv7TicJDJRNKBG9A9yWX8VEmEve3T2u6eZXfQXTGNdBvZkoCqNSkHfrMl/132",
    #         "sex":1,
    #         "birthday":"1987-12-21",
    #         "idCardType":0,
    #         "idCardNo":"420281108712214298",
    #         "address":"武汉"
    #     }
    #     params["data"] = str(data)
    #     sign = wopV4Lib.right_sign(params,self.appSecret)
    #     params["sign"] = sign
    #     resp = requests.post(url,data=params)
    #     print(resp.text)
    #     assert resp.status_code == 200
    #     # assert self.memberIds.get("normal_memberId") in resp.text
    #     assert (resp.elapsed.microseconds/1000000)<2
    #
    # def test_getFansInfo(self):
    #     print("******** getFansInfo start ********")
    #     url = self.host+"/member/getFansInfo"
    #     params = copy.copy(self.comParams)
    #     params["timestamp"] = get_now_time()
    #     for op in self.openIds:
    #         data = {
    #             "openId":op
    #         }
    #         params["data"] = str(data)
    #         sign = wopV4Lib.right_sign(params,self.appSecret)
    #         params["sign"] = sign
    #         # print(params)
    #         resp = requests.post(url,data=params)
    #         print(resp.text)
    #         assert resp.status_code == 200
    #         assert op in resp.text
    #         assert (resp.elapsed.microseconds/1000000)<2
    #
    # def test_getPointFlow(self):
    #     print("******** getPointFlow start ********")
    #     url = self.host+"/point/getPointFlow"
    #     params = copy.copy(self.comParams)
    #     params["timestamp"] = get_now_time()
    #     data = {
    #         "memberId":self.memberIds.get("normal_memberId"),
    #         "pageNo":1,
    #         "pageSize":10,
    #         "startDate":"",
    #         "endDate":""
    #     }
    #     params["data"] = str(data)
    #     sign = wopV4Lib.right_sign(params,self.appSecret)
    #     params["sign"] = sign
    #     # print(params)
    #     resp = requests.post(url,data=params)
    #     print(resp.text)
    #     assert resp.status_code == 200
    #     assert self.memberIds.get("normal_memberId") in resp.text
    #     assert (resp.elapsed.microseconds/1000000)<2
    #
    #
    # def test_addPoint(self):
    #     print("******** addPoint start ********")
    #     url = self.host+"/point/addPoint"
    #     pointBefore = wopV4Lib.getMemberPoint_MemberId(self.host,self.comParams,self.appSecret,self.memberIds.get("normal_memberId"))
    #     pointAddValue = 20
    #     params = copy.copy(self.comParams)
    #     params["timestamp"] = get_now_time()
    #     data = {
    #         "memberId":self.memberIds.get("normal_memberId"),
    #         "pointNo":"point"+wopV4Lib.get_random_outorderno(),
    #         "point":pointAddValue,
    #         "storeId":self.storeId,
    #         "consumption":200,
    #         "pointType":"04",
    #         "pointCategory":3003,
    #         "pointChannel":104,
    #         "pointDesc":"补录地点为:卡哇伊;补录店铺位置编号:B105-1、2;操作人:admin;消费金额:123;小票日期:20180412;票号:123132;积分:20"
    #     }
    #     params["data"] = str(data)
    #     sign = wopV4Lib.right_sign(params,self.appSecret)
    #     params["sign"] = sign
    #     # print(params)
    #     resp = requests.post(url,data=params)
    #     print(resp.text)
    #     pointAfter = wopV4Lib.getMemberPoint_MemberId(self.host, self.comParams, self.appSecret,
    #                                                   self.memberIds.get("normal_memberId"))
    #     assert resp.status_code == 200
    #     assert pointAddValue == (pointAfter-pointBefore)
    #     assert (resp.elapsed.microseconds/1000000)<2
    #
    # def test_reducePoint(self):
    #     print("******** reducePoint start ********")
    #     url = self.host+"/point/reducePoint"
    #     pointBefore = wopV4Lib.getMemberPoint_MemberId(self.host,self.comParams,self.appSecret,self.memberIds.get("normal_memberId"))
    #     pointAddValue = 20
    #     params = copy.copy(self.comParams)
    #     params["timestamp"] = get_now_time()
    #     data = {
    #         "memberId":self.memberIds.get("normal_memberId"),
    #         "pointNo":"point"+wopV4Lib.get_random_outorderno(),
    #         "point":pointAddValue,
    #         # "storeId":self.storeId,
    #         # "consumption":200,
    #         "pointType":"05",
    #         "pointCategory":1009,
    #         "pointChannel":104,
    #         "pointDesc":"扣除测试"
    #     }
    #     params["data"] = str(data)
    #     sign = wopV4Lib.right_sign(params,self.appSecret)
    #     params["sign"] = sign
    #     # print(params)
    #     resp = requests.post(url,data=params)
    #     print(resp.text)
    #     pointAfter = wopV4Lib.getMemberPoint_MemberId(self.host, self.comParams, self.appSecret,
    #                                                   self.memberIds.get("normal_memberId"))
    #     assert resp.status_code == 200
    #     assert pointAddValue == (pointBefore-pointAfter)
    #     assert (resp.elapsed.microseconds/1000000)<2
    #
    # def test_getCouponInfo(self):
    #     print("******** getCouponInfo start ********")
    #     url = self.host+"/coupon/getCouponInfo"
    #     params = copy.copy(self.comParams)
    #     params["timestamp"] = get_now_time()
    #     data = {
    #         "couponId":self.couponIds.get("online_couponId"),
    #     }
    #     params["data"] = str(data)
    #     sign = wopV4Lib.right_sign(params,self.appSecret)
    #     params["sign"] = sign
    #     # print(params)
    #     resp = requests.post(url,data=params)
    #     print(resp.text)
    #     assert resp.status_code == 200
    #     assert self.couponIds.get("online_couponId") in resp.text
    #     assert (resp.elapsed.microseconds/1000000)<2
    #
    # def test_downloadCoupon(self):
    #     print("******** downloadCoupon start ********")
    #     url = self.host+"/coupon/downloadCoupon"
    #     params = copy.copy(self.comParams)
    #     params["timestamp"] = get_now_time()
    #     data = {
    #         "couponId":self.couponIds.get("autodown_couponId"),
    #         "memberId":self.memberIds.get("normal_memberId"),
    #         "flowNo":wopV4Lib.get_random_outorderno(),
    #         "num":1
    #     }
    #     params["data"] = str(data)
    #     sign = wopV4Lib.right_sign(params,self.appSecret)
    #     params["sign"] = sign
    #     # print(params)
    #     resp = requests.post(url,data=params)
    #     print(resp.text)
    #     assert resp.status_code == 200
    #     assert self.couponIds.get("autodown_couponId") in resp.text
    #     assert (resp.elapsed.microseconds/1000000)<2
    #
    # def test_getCouponPackageList(self):
    #     print("******** getCouponPackageList start ********")
    #     url = self.host+"/coupon/getCouponPackageList"
    #     params = copy.copy(self.comParams)
    #     params["timestamp"] = get_now_time()
    #     data = {
    #         "memberId":self.memberIds.get("normal_memberId"),
    #         "state":1,
    #         "pageNo":1,
    #         "pageSize":10
    #     }
    #     params["data"] = str(data)
    #     sign = wopV4Lib.right_sign(params,self.appSecret)
    #     params["sign"] = sign
    #     # print(params)
    #     resp = requests.post(url,data=params)
    #     print(resp.text)
    #     couponTotalCount = ((resp.json()).get("data")).get("totalCount")
    #     assert resp.status_code == 200
    #     assert self.couponIds.get("autodown_couponId") in resp.text
    #     assert "totalCount" in resp.text
    #     assert couponTotalCount > 0
    #     assert (resp.elapsed.microseconds/1000000)<2
    #
    # def test_getAvaliableCouponPackageList(self):
    #     print("******** getAvaliableCouponPackageList start ********")
    #     url = self.host+"/coupon/getAvaliableCouponPackageList"
    #     params = copy.copy(self.comParams)
    #     params["timestamp"] = get_now_time()
    #     data = {
    #         "memberId":self.memberIds.get("normal_memberId"),
    #         "storeId":self.storeId,
    #         "pageNo":1,
    #         "pageSize":10,
    #         "couponType":"DJQ"
    #     }
    #     params["data"] = str(data)
    #     sign = wopV4Lib.right_sign(params,self.appSecret)
    #     params["sign"] = sign
    #     # print(params)
    #     resp = requests.post(url,data=params)
    #     print(resp.text)
    #     couponTotalCount = ((resp.json()).get("data")).get("totalCount")
    #     assert resp.status_code == 200
    #     assert self.couponIds.get("autodown_couponId") in resp.text
    #     assert "totalCount" in resp.text
    #     assert couponTotalCount > 0
    #     assert (resp.elapsed.microseconds/1000000)<2
    #
    # def test_checkUseCoupon(self):
    #     print("******** checkUseCoupon start ********")
    #     url = self.host+"/coupon/checkUseCoupon"
    #     params = copy.copy(self.comParams)
    #     params["timestamp"] = get_now_time()
    #     data = {
    #         "couponNo":self.couponNo,
    #         "storeId":self.storeId,
    #     }
    #     params["data"] = str(data)
    #     sign = wopV4Lib.right_sign(params,self.appSecret)
    #     params["sign"] = sign
    #     # print(params)
    #     resp = requests.post(url,data=params)
    #     print(resp.text)
    #     assert resp.status_code == 200
    #     assert (resp.json()).get("msg") == "SUCCESS"
    #     assert (resp.elapsed.microseconds/1000000)<2
    #
    # def test_useCoupon(self):
    #     print("******** useCoupon start ********")
    #     url = self.host+"/coupon/useCoupon"
    #     params = copy.copy(self.comParams)
    #     params["timestamp"] = get_now_time()
    #     data = {
    #         "couponNo":self.couponNo,
    #         "storeId":self.storeId,
    #     }
    #     params["data"] = str(data)
    #     sign = wopV4Lib.right_sign(params,self.appSecret)
    #     params["sign"] = sign
    #     # print(params)
    #     resp = requests.post(url,data=params)
    #     print(resp.text)
    #     assert resp.status_code == 200
    #     assert (resp.json()).get("msg") == "SUCCESS"
    #     assert (resp.elapsed.microseconds/1000000)<2
    #
    # # TODO
    # def test_invalidatedCoupon(self):
    #     print("******** invalidatedCoupon start ********")
    #     url = self.host+"/coupon/invalidatedCoupon"
    #     toInvalidateCouponNo = wopV4Lib.downloadCoupon(self.host,self.comParams,self.appSecret,
    #                                                    self.memberIds.get("normal_memberId"),self.couponIds.get("autodown_couponId"))
    #     params = copy.copy(self.comParams)
    #     params["timestamp"] = get_now_time()
    #     data = {
    #         "couponNo":toInvalidateCouponNo,
    #     }
    #     params["data"] = str(data)
    #     sign = wopV4Lib.right_sign(params,self.appSecret)
    #     params["sign"] = sign
    #     # print(params)
    #     resp = requests.post(url,data=params)
    #     print(resp.text)
    #     assert resp.status_code == 200
    #     assert (resp.elapsed.microseconds/1000000)<2
    #
    # def test_enterNotify(self):
    #     print("******** enterNotify start ********")
    #     url = self.host+"/parking/enterNotify"
    #     params = copy.copy(self.comParams)
    #     params["timestamp"] = get_now_time()
    #     data = {
    #         "parkCode":self.parking.get("parkCodeA"),
    #         "plateNo":self.parking.get("plateNo"),
    #         "inPlace":self.parking.get("inPlace"),
    #         "enterTime":self.parking.get("enterTime"),
    #     }
    #     params["data"] = str(data)
    #     sign = wopV4Lib.right_sign(params,self.appSecret)
    #     params["sign"] = sign
    #     # print(params)
    #     resp = requests.post(url,data=params)
    #     print(resp.text)
    #     assert resp.status_code == 200
    #     assert (resp.elapsed.microseconds/1000000)<2
    #
    # def test_exitNotify(self):
    #     print("******** exitNotify start ********")
    #     url = self.host+"/parking/exitNotify"
    #     params = copy.copy(self.comParams)
    #     params["timestamp"] = get_now_time()
    #     data = {
    #         "parkCode":self.parking.get("parkCodeA"),
    #         "plateNo":self.parking.get("plateNo"),
    #         "outTime":self.timestamp,
    #         "flowNo":wopV4Lib.get_random_outorderno()
    #     }
    #     params["data"] = str(data)
    #     sign = wopV4Lib.right_sign(params,self.appSecret)
    #     params["sign"] = sign
    #     # print(params)
    #     resp = requests.post(url,data=params)
    #     print(resp.text)
    #     assert resp.status_code == 200
    #     assert (resp.elapsed.microseconds/1000000)<2
    #
    # def test_createOrder (self):
    #     print("******** createOrder start ********")
    #     url = self.host + "/order/createOrder"
    #     params = copy.copy(self.comParams)
    #     params["timestamp"] = get_now_time()
    #     data = {
    #         "tickNo": "",
    #         "outOrderNo": self.outOrderNo,
    #         "storeId": self.storeId,
    #         "memberId": self.memberIds.get("normal_memberId"),
    #         "orderType": 2,
    #         "orderChannel": 9,
    #         "orderSource": 4,
    #         "couponNo": "",
    #         "toCashPoint": "",
    #         "pointToCashFee": "",
    #         "couponPrefFee": "",
    #         "activityPrefFee": "",
    #         "memberPrefFee": "",
    #         "totalFee": 3000,
    #         "actTotalFee": 3000,
    #         "memberCreditValue": 30,
    #         "outCouponInfo": "",
    #         "remark": "",
    #         "cashierId": "fage",
    #         "salesCode": "",
    #         "posNo": "k209",
    #         "refundStatus": 1
    #     }
    #     params["data"] = str(data)
    #     sign = wopV4Lib.right_sign(params, self.appSecret)
    #     params["sign"] = sign
    #     # print(params)
    #     resp = requests.post(url, data=params)
    #     print(resp.text)
    #     assert resp.status_code == 200
    #     assert (resp.elapsed.microseconds / 1000000) < 2
    #
    # def test_payCallbackNotify(self):
    #     print("******** payCallbackNotify start ********")
    #     url = self.host + "/order/payCallbackNotify"
    #     params = copy.copy(self.comParams)
    #     params["timestamp"] = get_now_time()
    #     data = {
    #         "outOrderNo": self.outOrderNo,
    #         "status": 2,
    #         "payMethod": 4,
    #         "totalFee": 3000,
    #         "buyerId": "209",
    #         "buyerName": "parcel",
    #         "batchNo": "",
    #         "authNo": "",
    #         "refNo": "",
    #         "tradeTime": self.timestamp
    #     }
    #     params["data"] = str(data)
    #     sign = wopV4Lib.right_sign(params, self.appSecret)
    #     params["sign"] = sign
    #     resp = requests.post(url, data=params)
    #     print(resp.text)
    #     assert resp.status_code == 200
    #     assert (resp.elapsed.microseconds / 1000000) < 2
    #
    # def test_closeOrder(self):
    #     print("******** closeOrder start ********")
    #     url = self.host + "/order/closeOrder"
    #     params = copy.copy(self.comParams)
    #     params["timestamp"] = get_now_time()
    #     outOrderNo = wopV4Lib.get_random_outorderno()
    #     orderData = {
    #         "tickNo": "",
    #         "outOrderNo": outOrderNo,
    #         "storeId": self.storeId,
    #         "memberId": self.memberIds.get("normal_memberId"),
    #         "orderType": 2,
    #         "orderChannel": 9,
    #         "orderSource": 4,
    #         "couponNo": "",
    #         "toCashPoint": "",
    #         "pointToCashFee": "",
    #         "couponPrefFee": "",
    #         "activityPrefFee": "",
    #         "memberPrefFee": "",
    #         "totalFee": 3000,
    #         "actTotalFee": 3000,
    #         "memberCreditValue": 30,
    #         "outCouponInfo": "",
    #         "remark": "",
    #         "cashierId": "fage",
    #         "salesCode": "",
    #         "posNo": "k209",
    #         "refundStatus": 1
    #     }
    #     wopV4Lib.createOrder(self.host,self.comParams,self.appSecret,orderData)
    #     data = {
    #         "outOrderNo":outOrderNo
    #     }
    #     params["data"] = str(data)
    #     sign = wopV4Lib.right_sign(params, self.appSecret)
    #     params["sign"] = sign
    #     # print(params)
    #     resp = requests.post(url, data=params)
    #     print(resp.text)
    #     assert resp.status_code == 200
    #     assert (resp.elapsed.microseconds / 1000000) < 2
    #
    # def test_syncOrder(self):
    #     print("******** syncOrder start ********")
    #     url = self.host + "/order/syncOrder"
    #     params = copy.copy(self.comParams)
    #     params["timestamp"] = get_now_time()
    #     outOrderNo = wopV4Lib.get_random_outorderno()
    #     orderData = {
    #         "tickNo": "",
    #         "outOrderNo": outOrderNo,
    #         "storeId": self.storeId,
    #         "memberId": self.memberIds.get("normal_memberId"),
    #         "orderType": 2,
    #         "orderChannel": 9,
    #         "orderSource": 4,
    #         "payMethod": 4,
    #         "couponNo": "",
    #         "toCashPoint": None,
    #         "pointToCashFee": None,
    #         "couponPrefFee": None,
    #         "activityPrefFee": None,
    #         "memberPrefFee": None,
    #         "totalFee": 3000,
    #         "actTotalFee": 2700,
    #         "memberCreditValue": 30,
    #         "outCouponInfo": "",
    #         "remark": "",
    #         "cashierId": "fage",
    #         "salesCode": "",
    #         "posNo": "k209",
    #         "payChannelPrefFee": 1,
    #         "payStatus": 1,
    #         "buyerId": "209",
    #         "buyerName": "parcel",
    #         "unionBatchNo": "",
    #         "unionAuthNo": "",
    #         "unionRefNo": "",
    #         "unionTradeTime": "2018-06-02 13:59:09",
    #         "creatTime": "2018-06-02 13:59:09",
    #         "payTime": "2018-06-02 13:59:09",
    #         "updateTime": "2018-06-02 13:59:09",
    #         "isCheckCoupon": False,
    #         "IsAddPoint": False,
    #         "isSendWxMsg": False
    #     }
    #     params["data"] = str(orderData)
    #     sign = wopV4Lib.right_sign(params, self.appSecret)
    #     params["sign"] = sign
    #     resp = requests.post(url, data=params)
    #     print(resp.text)
    #     assert resp.status_code == 200
    #     assert (resp.elapsed.microseconds / 1000000) < 2
    #
    # def test_syncRefund(self):
    #     print("******** syncRefund start ********")
    #     url = self.host + "/order/syncRefund"
    #     params = copy.copy(self.comParams)
    #     params["timestamp"] = get_now_time()
    #     outOrderNo = wopV4Lib.get_random_outorderno()
    #     orderData = {
    #         "outOrderNo": outOrderNo,
    #         "refundNo":
    #         "orderDetailCode": "",
    #         "quantity": 1,
    #         "refundFee": 20000,
    #         "memberCreditValue": 900,
    #         "toRebackPoint": 500,
    #         "toCashPoint": 400,
    #         "cashierId": "209",
    #         "remark": "nothing",
    #         "posNo": "test123"
    #     }
    #     params["data"] = str(orderData)
    #     sign = wopV4Lib.right_sign(params, self.appSecret)
    #     params["sign"] = sign
    #     resp = requests.post(url, data=params)
    #     print(resp.text)
    #     assert resp.status_code == 200
    #     assert (resp.elapsed.microseconds / 1000000) < 2

if __name__ == '__main__':
    # pytest.main("-s test_wopStandardAlldragon.py")
    pytest.main("-v test_wopStandard.py --html=report/sampleReport.html")
