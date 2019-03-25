#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

import re
import pytest
import requests
import time
import pytest_benchmark

class TestOrderApi:
    host = 'http://wop.mallshow.net'
    tenantId = '1006'
    appId = 'hCPAYwPwSm2spDFc_QGg9A'
    appSecret = '12c3dcbe5c674b82a70a1ecfc1de5ab0'
    mobile = '18627169820'

    def getToken():
        s = requests.get(url=host+'/token',
                         params={"grant_type":"client_credential","appid":appId,"secret":appSecret})
        accessToken = s.json()["access_token"]
        print(accessToken)

    accessToken = getToken()
    comParams = {"tenantId": tenantId, "verison": "1.0", "accessToken": accessToken}

    def test_getparkinfo():
        url = '/system/getparkinfo'
        comParams["data"] = {"mobile":mobile}
        s = requests.post(url=host+url,data=comParams)
        assert (s.status_code == 200)
        assert (s.json()['msg']=='请求成功')


