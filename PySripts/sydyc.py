# _*_ coding:GBK _*_
# ! /usr/bin/env python
__author__ = 'Administrator'

import re

project1 = r'C:/Users/Administrator/Desktop/project-2017050201.log'
project2 = r'C:/Users/Administrator/Desktop/project-2017050202.log'
with open(project1, 'r') as f:
    log_str_lines1 = f.read()
with open(project2, 'r') as f:
    log_str_lines2 = f.read()
log_str_lines = log_str_lines1+log_str_lines2
createOrder_pattern = r'/biz/order/createOrder.json tenantId=1091.*out_order_no=(.+?)\|store_id'
createOrder_list = re.findall(createOrder_pattern,log_str_lines)
print (createOrder_list)
print("*********************************************")
paySuc_pattern = r'/biz/order/successOutPayCallback.json tenantId=1091.*pay_no=(.+?)\|batch_no'
paySuc_list = re.findall(paySuc_pattern,log_str_lines)
print(paySuc_list)
# plateNo = list(set(index_mac))
# print plateNo_list