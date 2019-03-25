#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

# Created on 2016年11月29日
# @author: jiaohui
import requests

host = "http://wx.xxyxc.demo.shangquanquan.com"
def WxMsgSend(openId,msgCode):
    api_url = "/wechat/signature/sendTemplateMsgByOpenId"

