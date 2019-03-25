# _*_ coding:utf-8 _*_
#! /usr/bin/env python
# __author__ = 'Administrator'

import  re
# from collections import Counter
def wifi_midware (filepath):
	filepath = filepath
	with open (filepath, 'r', encoding='utf-8') as f:
		log_str_lines = f.read ()

	MAC_PATTERN = '[0-9a-fA-F]{2}-[0-9a-fA-F]{2}-[0-9a-fA-F]{2}-[0-9a-fA-F]{2}-[0-9a-fA-F]{2}-[0-9a-fA-F]{2}'
	OPENID_PATTERN=r'openId=(.{28})'
	# IP_PATTERN =
	# tenant_dict = {'nhcs': '10105', 'bdcsgc': '10106', 'ngjn': '10110','xhcsgc':'10107','cdfyh':'10112'}
	tenant_dict = {"nhcs":"10105"}
	# tenant_dict = {'xhcsgc':'10107','cdfyh':'10112'}
	# error_code = ['0201','0202','0203','0401','0403']
	for line in tenant_dict.values ():
		access_pattern = r'Access log.*wifi basId=' + line
		online_pattern = r'Access log.*/online.*basId=' + line
		wxOnline_pattern = r'Access log.*/wxOnline basId=' + line + r'.*openId=.*'
		wifi_pattern = r'Access log.*/wifi basId=' + line + r'.*'
		timeoutOnlie_pattern = r'Access log.*/timeOutOnline basId=' + line
		wifi_access_error_pattern = r'Access log.*/wifi basId=' + line + r'.*usermac=.*(?:.*\n)+?.*临时放行出错错误原因BAS.*'
		wifi_success_pattern = r'Access log.*/wifi basId=' + line + r'(?:.*\n)+?.*H3ChapMsgHandler.online.*请求认证，成功发送挑战报文并得到正确回应'
		# 错误码正则
		error_pattern= r'basId='+ line + r'(?:.*\n)+?.*bas返回错误码：\d\d\d\d\n.*BAS 设备通知 Portal Server.*'
		# error_pattern= r'bas返回错误码.*\n.*临时放行出错错误原因BAS'

		# error_0202_pattern= r'Access log.* basId='+line+r'(?:.*\n)+?.*bas返回错误码: 0202(?:.*\n)+?.*BAS 设备通知 Portal Server.*'
		# error_0401_pattern= r'Access log.* basId='+line+r'(?:.*\n)+?.*bas返回错误码: 0401(?:.*\n)+?.*BAS 设备通知 Portal Server.*'
		# error_0403_pattern= r'Access log.* basId='+line+r'(?:.*\n)+?.*bas返回错误码: 0403(?:.*\n)+?.*BAS 设备通知 Portal Server.*'
		# error_0203_pattern= r'Access log.* basId='+line+r'(?:.*\n)+?.*bas返回错误码: 0203(?:.*\n)+?.*BAS 设备通知 Portal Server.*'
		# error_0402_pattern= r'Access log.* basId='+line+r'(?:.*\n)+?.*bas返回错误码: 0402(?:.*\n)+?.*BAS 设备通知 Portal Server.*'

		# error_0202 = re.findall(error_0202_pattern,log_str_lines)
		# print("error_0202 num :"+str(len(error_0202)))


		access = re.findall (access_pattern, log_str_lines)
		print ("-------" + line + "-------")
		# print ("access num :" + str (len (access)))
		# access_mac = []
		# for line in access:
		# 	access_mac.append(re.findall(MAC_PATTERN,line)[0])
		# access_mac = list(set(access_mac))
		# print("access mac num :"+str(len(access_mac)))
		online = re.findall (online_pattern, log_str_lines)
		# print ("online access num:" + str (len (online)))

		wxOnline = re.findall (wxOnline_pattern, log_str_lines)
		# print ("wxOnline access num :" + str (len (wxOnline)))
		openId_list = []
		for line in wxOnline:
    			openId_list.append(re.findall(OPENID_PATTERN,line)[0])
		openId_list= list(set(openId_list))
		print("wxOnline 用户数:"+str(len(openId_list)))	

		wifi_access_error = re.findall (wifi_access_error_pattern, log_str_lines)
		print ("临时放行失败: " + str (len (wifi_access_error)))
		fail_mac = []
		error_list = []
		# 尝试使用collections.Counter 统计错误码
		# 0201_num = 0202_num = 0203_num = 0401_num=0403_num = 0
		# c= Counter()
		for line in wifi_access_error:
			fail_mac.append (re.findall (MAC_PATTERN, line) [0])
		# error_list.append(re.findall(r'bas返回错误码：(0201|0202|0203|0401|0403)',line))
		fail_mac = list (set (fail_mac))
		# print ("临时放行失败用户数 :" + str (len (fail_mac)))
		# print(error_list)
		# num = 1
		# for line in error_list:
		# 	print (line[0])
		# for x in range(len(error_list)):
		# 	print(error_list[x][0]+"   "+str(x))
		# print(len(error_list))

		wifi_access = re.findall (wifi_pattern, log_str_lines)
		print ("wifi access num:" + str (len (wifi_access)))
		wifi_access_mac = []
		# 当wifi access 日志未带有usermac时，跳过index of range 异常，并继续下一次统计
		for line in wifi_access:
			try:
				wifi_access_mac.append (re.findall (MAC_PATTERN, line) [0])
			except IndexError:
				pass
		wifi_access_mac = list (set (wifi_access_mac))
		print ("WIFI ACCESS用户数：" + str (len (wifi_access_mac)))

		wifi_access_success = re.findall (wifi_success_pattern, log_str_lines)
		print ("WIFI认证成功：" + str (len (wifi_access_success)))
		success_mac = []
		# 当wifi access 日志未带有usermac时，跳过index of range 异常，并继续下一次统计
		for line in wifi_access_success:
			try:
				success_mac.append (re.findall (MAC_PATTERN, line) [0])
			except IndexError:
				pass
		success_mac = list (set (success_mac))
		print ("wifi access success 用户数 :" + str (len (success_mac)))

		timeoutOnline = re.findall (timeoutOnlie_pattern, log_str_lines)
		print ("timeOutOnline num:" + str (len (timeoutOnline)))

		total_fail_mac = list (set (fail_mac) - set (success_mac))
		print ("一直认证失败用户数：" + str (len (total_fail_mac)))
		
		error_num = re.findall(error_pattern,log_str_lines)
		# print("error num: "+ str(len(error_num)))
		

if __name__ == "__main__":
	logfile = r'G:\portal_midware_log\project.log.2016-08-01.txt'
	wifi_midware (logfile)
