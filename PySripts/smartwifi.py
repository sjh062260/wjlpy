# _*_ coding:utf-8 _*_
# ! /usr/bin/env python
__author__ = 'Administrator'

import re
import time


# def logRead(filepath):
#     try:
#         f = open(filepath,'r',encoding = 'utf-8')
#         log_str = f.read()
#         f.close()
#         return log_str
#     except:
#         log_str = ''
#         return log_str
#     # print(time.ctime())
#     # u = time.time()
#     # print(u)

def logReadline(filepath):
	log_str = list()
	f = open(filepath,'r',encoding = 'utf-8')
	for line in f:
		line = f.readline()
		log_str.append(line)
	f.close()
    # u = time.time()
    # # print(u)

def logReadLines(filepath):
    try:
        with open(filepath,'r',encoding = 'utf-8') as f:
        # f = open(filepath,'r',encoding = 'utf-8')
            log_str = f.readlines()
        # return log_str
    except:
        log_str = []
        # return log_str
    # u = time.time()
    # print(u-t)
if __name__ == "__main__":
    # tenant_list = ['cdfyh','ngjn','bdcsgc','nhcs','nghx','wsq','xhcsgc','ycjf','sydyc','nthqgc','nhdh']
    # tenant_list = ['xhcsgc']
    # tenant_list = ['sydyc']
    # tenant_dict = {"cdfyh":"10112","ngjn":"10110","bdcsgc":"10106","nhcs":"10105","nghx":"10109","wsq":"10103","xhcsgc":"10107","sydyc":"10113","nthqgc":"10115","nhdh":"10108","ycjf":"10114"}
    # tenant_dict = {'xhcsgc':"10107"}
    portal_log_file1 = r'G:\wifi_portal_log\project.log.2016-09-22.txt'
    portal_log_file2 = r'G:\wifi_portal_log\project.log.2016-09-22-01.txt'
    portal_log_file3 = r'G:\wifi_portal_log\project.log.2016-09-22-02.txt'
    # print(time.ctime())
    # t = time.time()
    logRead(portal_log_file2)
    # logReadline(portal_log_file2)
    # logReadLines(portal_log_file2)

    # log_str_lines1 = logRead(portal_log_file1)
    # log_str_lines2 = logRead(portal_log_file2)
    # log_str_lines3 = logRead(portal_log_file3)
    # print(len(log_str_lines1))
    # print(len(log_str_lines2))
    # print(len(log_str_lines3))

    # log_str_lines = log_str_lines1+log_str_lines2+log_str_lines3
    # log_str_lines1=log_str_lines2=log_str_lines3=[]
