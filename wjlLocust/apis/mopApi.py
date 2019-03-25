#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

from locust import HttpLocust, TaskSet, task
import Queue
import pymysql


class WxWebSiteTasks(TaskSet):
    tenantId = '1055'
    syscode = 'wechat'
    memberIds = []
    cardNos = []
    testMemberIdsQueue = Queue.Queue()
    testCardNosQueue = Queue.Queue()

    # to connect mysql
    conn = pymysql.connect(host='10.10.220.62',port = 3306,user='read_sjh',passwd='46KPFIdlH67L1xRNtmNI',db="sqq_crm",
                         charset='utf8')
    cursor = conn.cursor()
    # sql = "select 'member_id'  from 'member_base_info' where 'tenant_id' = '%s' order by id desc limit 1000"%(tenantId)
    # print(sql)
    try:
        cursor.execute("select member_id,card_no from member_base_info WHERE tenant_id = '1055' order by id desc limit 10000 ")
        results = cursor.fetchall()
        # print(results)
        for row in results:
            # print(row)
            memberIds.append(str(row[0]))
            cardNos.append(str(row[1]))
    except:
        print("Error :unable to fetch data.")
    conn.close()

    for items in memberIds:
        testMemberIdsQueue.put(items)
    for items in cardNos:
        testCardNosQueue.put(items)


    @task(50)
    def testGetUserInfoByMemberId(self):
        try:
            self.memberId = self.testMemberIdsQueue.get()
            print( "to test memberId is :"+self.memberId)
        except Queue.Empty:
            print("memberIds data is empty,tests ended")
            exit(0)
        payload = {
            "tenantId":self.tenantId,
            "memberId":self.memberId,
            "syscode": self.syscode
        }
        with self.client.post('/crm/getUserInfoByMemberId.json',data = payload,catch_response=True) as resp:
            print("to test api is getUserInfoByMemberId")
            try:
                resp_json = resp.json()
                if resp_json['msg'] == "SUCCESS":
                    resp.success()
                else:
                    resp.failure("Got wrong response content!")
            except:
                resp.failure("Got wrong response")
                
        self.testMemberIdsQueue.put(self.memberId)

    @task(35)
    def testGetUserPointByMemberIdAndSync(self):
        try:
            self.memberId = self.testMemberIdsQueue.get()
            print( "to test memberId is :"+self.memberId)
        except Queue.Empty:
            print("memberIds data is empty,tests ended")
            exit(0)
        payload = {
            "tenantId":self.tenantId,
            "memberId":self.memberId,
            "syscode": self.syscode
        }
        with self.client.post('/crm/getUserPointByMemberIdAndSync.json',data = payload,catch_response=True) as resp:
            print("to test api is getUserPointByMemberIdAndSync")
            try:
                resp_json = resp.json()
                if resp_json['msg'] == "SUCCESS":
                    resp.success()
                else:
                    resp.failure("Got wrong response content!")
            except:
                resp.failure("Got wrong response")
        self.testMemberIdsQueue.put(self.memberId)

    # @task(11)
    # def testGetAllStoreMapping(self):
    #     payload = {
    #         "tenantId":self.tenantId,
    #         "syscode": self.syscode
    #     }
    #     with self.client.post('/mapping/getAllStoreMapping.json',data = payload,catch_response=True) as resp:
    #         print("to test api is getAllStoreMapping")
    #         try:
    #             resp_json = resp.json()
    #             if resp_json['msg'] == "SUCCESS":
    #                 resp.success()
    #             else:
    #                 resp.failure("Got wrong response content!")
    #         except:
    #             resp.failure("Got wrong response")


    # @task(5)
    # def testCalcConsumePoint(self):
    #     try:
    #         self.memberId = self.testMemberIdsQueue.get()
    #         print( "to test memberId is :"+self.memberId)
    #     except Queue.Empty:
    #         print("memberIds data is empty,tests ended")
    #         exit(0)
    #     payload = {
    #         "tenantId":self.tenantId,
    #         "syscode": self.syscode,
    #         "money": 300,
    #         "memberId":self.memberId,
    #         "storeId":'1055162500314',
    #         "salecode":''
    #     }
    #     with self.client.post('/crm/calcConsumePoint.json',data = payload,catch_response=True) as resp:
    #         print("to test api is calcConsumePoint")
    #         try:
    #             resp_json = resp.json()
    #             if resp_json['msg'] == "SUCCESS":
    #                 resp.success()
    #             else:
    #                 resp.failure("Got wrong response content!")
    #         except:
    #             resp.failure("Got wrong response")
    #     self.testMemberIdsQueue.put(self.memberId)

    # @task(3)
    # def testGetUserMappingByMemberId(self):
    #     try:
    #         self.memberId = self.testMemberIdsQueue.get()
    #         print( "to test memberId is :"+self.memberId)
    #     except Queue.Empty:
    #         print("memberIds data is empty,tests ended")
    #         exit(0)
    #     payload = {
    #         "memberId":self.memberId,
    #         "tenantId":self.tenantId,
    #         "syscode":self.syscode
    #     }
    #     with self.client.post('/crm/getUserMappingByMemberId.json',data = payload,catch_response=True) as resp:
    #         print("to test api is getUserMappingByMemberId")
    #         try:
    #             resp_json = resp.json()
    #             if resp_json['msg'] == "SUCCESS":
    #                 resp.success()
    #             else:
    #                 resp.failure("Got wrong response content!")
    #         except:
    #             resp.failure("Got wrong response")
    #     self.testMemberIdsQueue.put(self.memberId)

    # @task(3)
    # def testGetMemberIdByCardNo(self):
        # try:
        #     self.cardNo = self.testCardNosQueue.get()
        #     print("to test cardNo is :"+self.cardNo)
        # except Queue.Empty:
        #     print("cardNo is empty.tests ended")
        #     exit(0)
        # payload={
        #     "cardNo":self.cardNo,
        #     "tenantId":self.tenantId,
        #     "syscode":self.syscode
        # }
        # with self.client.post("/api/getMemberIdByCardNo.json",data = payload,catch_response=True) as resp:
        #     print("to test api is getMemberIdByCardNo")
        #     try:
        #         resp_json = resp.json()
        #         if resp_json['msg'] == "SUCCESS":
        #             resp.success()
        #         else:
        #             resp.failure("Got wrong response content!")
        #     except:
        #         resp.failure("Got wrong response")
        # self.testCardNosQueue.put(self.cardNo)

class WxWebSiteUser(HttpLocust):
    task_set = WxWebSiteTasks
    host = 'http://mop.mallshow.net'
    min_wait = 1000
    max_wait = 5000
