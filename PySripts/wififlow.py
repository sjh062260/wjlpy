# _*_ coding:utf-8 _*_
# ! /usr/bin/env python
__author__ = 'Administrator'

import re


def flow (filepath):
	i = 0
	filepath = filepath
	with open (filepath, encoding="utf-8") as f:
		log_lines = f.readlines ()
	for line in log_lines:
		# print(line)
		for http_host in line.split ("```"):
			if i == 0:  # 获取时间字段，位于日志位置1，格式如:"18/Jul/2016:00:00:03 +0800"
				timerow = flow.split (":")
				hm = timerow [1] + ":" + timerow [2]  # 获取小时和分钟做为key
			if i == 3 and re.match (r'"wifi.*?.net"', http_host):  # 获取日志中的wifi_url ,作为key
				yield http_host, 1  # 初始化key:value,value计数为1
			i += 1


if __name__ == '__main__':
	filepath = r'C:\Users\Administrator\Desktop\wifi_log\wifi-access.log'
	flow (filepath)
