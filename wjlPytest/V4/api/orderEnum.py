#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

"""
@author:sjh
@time:2018/6/1 11:08
"""

orderMoldEnum = {
    "order": 1,
    "refund": 2
}
orderSourceEnum = {
    "WX": 1,
    "SHZS": 2,
    "PARKING": 3,
    "POS": 4,
    "WOP": 5,
    "OTHER": 6
}
orderStatusEnum = {
    "nopayment": 1,
    "success": 2,
    "close": 3
}
orderTypeEnum = {
    "COUPON": 1,
    "CONSUME": 2,
    "PARKING": 3,
    "SCAN": 4
}