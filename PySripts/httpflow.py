# _*_ coding:utf-8 _*_
# ! /usr/bin/env python
__author__ = 'Administrator'

from mrjob.job import MRJob
import re


class MRCounter (MRJob):
	def mapper (self, key, line):
		i = 0
		for http_url in line.split ("```"):
			if i == 0:  # 获取时间字段，位于日志位置1，格式如:"18/Jul/2016:00:00:03 +0800"
				timerow = flow.split (":")
				hm = timerow [1] + ":" + timerow [2]  # 获取小时和分钟做为key
			if i == 3 and re.match (r'"wifi.*?.net"', http_url):  # 获取日志中的wifi_url ,作为key
				yield http_url, 1  # 初始化key:value,value计数为1
			i += 1

	def reducer (self, http_url, occurrences):
		yield http_url, sum (occurrences)  # 对排序后的key对应的value做sum操作

	def steps (self):
		return [self.mr (mapper=self.mapper),
		        self.mr (reducer=self.reducer)]


if __name__ == '__main__':
	MRCounter.run ()
