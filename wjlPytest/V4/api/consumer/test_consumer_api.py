#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

"""
@author:sjh
@time:2018/5/25 10:33
"""
import pytest
import requests as rq

class TestConsumer:
    host="https://h5.dev4.wanjianglong.net/wjl"
    group = "/consumer"
    groupId=1200
    tenantId=4021
    activityId = '402118219002301'
    myActivityId= '402118234000101'
    openId = 'oa1P4s-jaWST3zZL1fjy4Qupty4c'
    memberId='12000100000125'
    storeId = '4021181010002'
    articleId = 23
    pageCode = ['category','guid','index','member_center','nav','register','register_success','self_point']
    pageId = 10
    collect_pic = 'http://sqqimg.b0.upaiyun.com/2018/03/22/9ea15f12a6c24939928cdc3d64f7df6222.png'
    couponNo = '4021404830654'
    # themeActivityType = ["ACT_PPYH","ACT_SCHD","ACT_HYHD"]
    # themeActivityState = ["ing","end","pre"]
    #  获取登录cookies
    def login(self):
        resp = rq.get(url=self.host+'/front/wer/#/member?openId='+self.openId)
        return resp.cookies.get_dict()
    #
    def test_themeActivity_list(self):
        print("****** test_themeActivity_list start ******")
        url = self.host+self.group+"/themeActivity/list.json"
        data = {
            "type":"ACT_PPYH",
            "state":"ing",
            "pageNo":1,
            "pageSize":20
        }
        resp = rq.post(url,data=data)
        resp_data = resp.json()["data"]
        try:
            resp_act_state = ((resp_data[0])["extraMap"])["state"]
            assert resp_act_state == 2
        except IndexError:
            return
        assert resp.status_code == 200


    def test_themeActivity_detail(self):
        url = self.host+self.group+"/themeActivity/detail.json"
        data = {"activityId":self.activityId}
        resp = rq.post(url,data=data)
        resp_data = resp.json()["data"]
        assert resp.status_code == 200
        assert resp_data["activity_id"] == self.activityId

    def test_themeActivity_myList(self):
        url = self.host+self.group+"/themeActivity/myList.json"
        data = {"memberId":self.memberId}
        resp = rq.post(url,data=data,cookies=self.login())
        print(resp.text)
        # resp_data = resp.json()["data"]
        assert resp.status_code == 200

    def test_themeActivy_myDetail(self):
        url = self.host+self.group+"/themeActivity/myDetail.json"
        data = {
            "memberId":self.memberId,
            "activityId":self.myActivityId
        }
        resp = rq.post(url,data=data,cookies=self.login())
        print(resp.text)
        assert resp.status_code == 200
    #
    def test_artcicle_getArticleById(self):
        url = self.host+self.group+"/article/getArticleById.json"
        data = {
            "tenantId":self.tenantId,
            "id":self.articleId
        }
        resp = rq.post(url,data=data,cookies=self.login())
        print(resp.text)
        try:
            resp_articleId = (resp.json()["data"])["id"]
            assert resp_articleId == self.articleId
        except IndexError:
            return
        assert resp.status_code == 200

    def test_page_getPageByCode_category(self):
        url = self.host + self.group + "/page/getPageByCode.json"
        data = {
            "tenantId": self.tenantId,
            "code":'category'
        }
        resp = rq.post(url, data=data, cookies=self.login())
        print(resp.text)
        try:
            resp_pageCode = (resp.json()["data"])["online_html"]
            assert len(resp_pageCode) > 0
        except TypeError:
            return
        assert resp.status_code == 200

    def test_page_getPageByCode_index(self):
        url = self.host + self.group + "/page/getPageByCode.json"
        data = {
            "tenantId": self.tenantId,
            "code":'index'
        }
        resp = rq.post(url, data=data, cookies=self.login())
        print(resp.text)
        try:
            resp_pageCode = (resp.json()["data"])["online_html"]
            assert len(resp_pageCode) >0
        except TypeError:
            return
        assert resp.status_code == 200

    def test_page_getPageByCode_guid(self):
        url = self.host + self.group + "/page/getPageByCode.json"
        data = {
            "tenantId": self.tenantId,
            "code":'guid'
        }
        resp = rq.post(url, data=data, cookies=self.login())
        print(resp.text)
        try:
            resp_pageCode = (resp.json()["data"])["online_html"]
            assert len(resp_pageCode) >0
        except TypeError:
            return
        assert resp.status_code == 200

    def test_page_getPageByCode_memberCenter(self):
        url = self.host + self.group + "/page/getPageByCode.json"
        data = {
            "tenantId": self.tenantId,
            "code":'member_center'
        }
        resp = rq.post(url, data=data, cookies=self.login())
        print(resp.text)
        try:
            resp_pageCode = (resp.json()["data"])["online_html"]
            assert len(resp_pageCode) >0
        except TypeError:
            return
        assert resp.status_code == 200

    def test_page_getPageByCode_nav(self):
        url = self.host + self.group + "/page/getPageByCode.json"
        data = {
            "tenantId": self.tenantId,
            "code":'nav'
        }
        resp = rq.post(url, data=data, cookies=self.login())
        print(resp.text)
        try:
            resp_pageCode = (resp.json()["data"])["online_html"]
            assert len(resp_pageCode) >0
        except TypeError:
            return
        assert resp.status_code == 200

    def test_page_getPageByCode_selfPoint(self):
        url = self.host + self.group + "/page/getPageByCode.json"
        data = {
            "tenantId": self.tenantId,
            "code":'self_point'
        }
        resp = rq.post(url, data=data, cookies=self.login())
        print(resp.text)
        try:
            resp_pageCode = (resp.json()["data"])["online_html"]
            assert len(resp_pageCode) >0
        except TypeError:
            return
        assert resp.status_code == 200

    def test_page_getPageByCode_register(self):
        url = self.host + self.group + "/page/getPageByCode.json"
        data = {
            "tenantId": self.tenantId,
            "code":'register'
        }
        resp = rq.post(url, data=data, cookies=self.login())
        print(resp.text)
        try:
            resp_pageCode = (resp.json()["data"])["online_html"]
            assert len(resp_pageCode) >0
        except TypeError:
            return
        assert resp.status_code == 200

    def test_page_getPageById(self):
        url = self.host + self.group + "/page/getPageById.json"
        data = {
            "tenantId": self.tenantId,
            "id":self.pageId,
            "preview":1
        }
        resp = rq.post(url, data=data, cookies=self.login())
        print(resp.text)
        try:
            resp_pageCode = (resp.json()["data"])["online_html"]
            assert len(resp_pageCode) >0
        except TypeError:
            return
        assert resp.status_code == 200

    def test_collect_collect(self):
        url = self.host+self.group+'/collect/collect.json'
        data = {
            "storeId":self.storeId,
            "title":"test",
            "picUrl":self.collect_pic
        }
        resp = rq.post(url, data=data, cookies=self.login())
        print(resp.text)
        try:
            resp_pageCode = (resp.json()["data"])["online_html"]
            assert len(resp_pageCode) >0
        except TypeError:
            return
        assert resp.status_code == 200


    # def test_coupon_index(self):
    #     return
    #
    # def test_coupon_download(self):
    #     return
    #
    # def test_coupon_detail(self):
    #     return
    #
    def test_myCoupon_list_unUsed(self):
        url = self.host+self.group+'/myCoupon/list.json'
        data = {
            "status":1,
            "pageNo":1,
            "pageSize":10
        }
        resp = rq.post(url, data=data, cookies=self.login())
        print(resp.text)
        try:
            resp_pageCode = (resp.json()["data"])["online_html"]
            assert len(resp_pageCode) >0
        except TypeError:
            return
        assert resp.status_code == 200
    #
    def test_myCoupon_detail(self):
        url = self.host+self.group+'/myCoupon/list.json'
        data = {
            "storeId":self.storeId,
            "title":"test",
            "picUrl":self.collect_pic
        }
        resp = rq.post(url, data=data, cookies=self.login())
        print(resp.text)
        try:
            resp_pageCode = (resp.json()["data"])["online_html"]
            assert len(resp_pageCode) >0
        except TypeError:
            return
        assert resp.status_code == 200
    #
    # def test_collection_list(self):
    #     return
    #
    # # memberController
    # def test_member_memberInfo(self):
    #     return
    # def test_member_getByOpenId(self):
    #     return
    # def test_member_modify(self):
    #     return
    #
    # def test_member_unbindWx(self):
    #     return
    #
    # def test_member_signData(self):
    #     return
    # def test_member_sign(self):
    #     return
    # def test_member_changeMobile(self):
    #     return
    #
    # def test_memberGrade_list(self):
    #     return
    #
    # def test_register_sendValidateCode(self):
    #     return
    #
    # def test_register_checkCode(self):
    #     return
    #
    # def test_register_getPerfectRegisterConfig(self):
    #     return
    #
    # def test_register_getCompletionRegisterConfig(self):
    #     return
    #
    # def test_register_getactivityRegisterConfig(self):
    #     return
    #
    # def test_register_register(self):
    #     return
    #
    # # order
    # def test_order_myList(self):
    #     return
    #
    # def test_order_detail(self):
    #     return
    #
    # def test_order_deleteOrder(self):
    #     return
    #
    # def test_order_refund(self):
    #     return
    #
    # # point
    # def test_point_list(self):
    #     return
    #
    # def test_point_total(self):
    #     return
    #
    # def test_pointMall_list(self):
    #     return
    #
    # def test_pointMall_detail(self):
    #     return
    #
    # def test_pointMall_exChanege(self):
    #     return
    #
    # def test_selfPoint_getPhotoPointConfig(self):
    #     return
    # def test_selfPoint_photoPointUpload(self):
    #     return
    # def test_selfPoint_recordList(self):
    #     return
    #
    # # category  and store
    # def test_category_list(self):
    #     return
    # def test_category_detail(self):
    #     return
    # def test_store_list(self):
    #     return
    # def test_store_detail(self):
    #     return
    # def test_store_hot(self):
    #     return
    # def test_store_build(self):
    #     return
    # def test_store_myList(self):
    #     return
    #
    # # subjectAct
    # def test_subjectAct_list(self):
    #     return
    # def test_subjectAct_detail(self):
    #     return
    #

if __name__ == '__main__':
    pytest.main("-s test_consumer.py")
