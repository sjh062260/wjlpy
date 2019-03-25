#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

from locust import HttpLocust,TaskSet,task
# import requests
import re
# import time
import Queue
from pyquery import PyQuery

class WxWebSiteTasks(TaskSet):

    openIds = ['oVDyijor9IBis20gdQ0p2-XiRq0k', 'oVDyijoOaZ3kD8tN4eBFD-a8fxHY', 'oVDyijlEwVWbliJAgQ2yDSTITnQU',
               'oVDyijk21-vqRwwnSIhXNgd3JTQ0', 'oVDyijssVGUyZtuHuAtzRVvI6ABA', 'oVDyijukG40pTv-OkeCqgOKyY8_g',
               'oVDyijpMa2Fd9_xhc-oJyFjE0cEk', 'oVDyijsSyU73wpQzZWuEqm_6XITI', 'oVDyijlFQqpKoPKUZM-FfUuzAKxc',
               'oVDyijhc-INHWPt4MQSmQhyjE568','oVDyijsedKjO5kR_gAPeGxKzvcG0','oVDyijpMa2Fd9_xhc-oJyFjE0c07','oVDyijilqKAZGLhdtJZmS9BeYgRM',
               'oVDyijl8tfp9pkYtZGpt6Y_HmT54','oVDyijiEuYHSdhzv5jTycg_iLy-k','oVDyijk81SaiAElnV64ZOOoYS7Wg',
               'oVDyijj-lGS3PNA1eO0dFaMl2GTw','oVDyijg8WUa6UCmBzCQ4A9C7Qy3c','oVDyijkqi1C8TU1Pqi9YIx1nwf-g',
               'oVDyijuRh2I46kiEh6sAbL6OrB0Q','oHqfrw58amiPuVRQ-5qMQftnO1RR','oVDyijpb6fIoOzq026IgtEpJnr40',
               'oVDyijsK08c_aom6e4psYcf6Bs8w','oVDyijiLak73R2b4ht1qEDV9wAF0','oVDyijj-lGS3PNA1eO0dFaMl2GTw55',
               'oVDyijvZPG9j5E2sm04iKTcLYzbU','oVDyijkoZRqO7P1y1m2JFiTQV-_o','oVDyijkSSlW5ycSRpQNE1NhPvdaU']

    user_data_queue = Queue.Queue()
    for items in openIds:
        user_data_queue.put(items)

    def on_start(self):
        try:
            self.wjlTestOpenId = self.user_data_queue.get()
            uri = '/wx/member/memberCenter.html?wjlTestOpenId=' + self.wjlTestOpenId
            print(uri)
            r = self.client.get(uri)
            self.user_data_queue.put(self.wjlTestOpenId)
        except Queue.Empty:
            print('openId data is empty, tests ended')
            exit(0)

    @task
    def jctg(self):
        with self.client.get('/wx/subject/list.html?activityId=900118106000201') as resp:
#            pq = PyQuery(resp.text)
#            print(pq.attr("div","data-url"))
            pq = re.findall("couponId=(.*)\"",resp.text)
            print(pq)
        with self.client.get("/wx/subject/submitOrder.json?count=1&toCashPoint=0&pointToCashFee=0&activityId=900118106000201&couponId=9001181060002&act_type=tg") as r:
            print (r.status_code)
            print (r.text)




class WxWebSiteUser(HttpLocust):
    task_set =  WxWebSiteTasks
    host = 'https://m.mallcoo.cn'
    min_wait = 1000
    max_wait = 5000