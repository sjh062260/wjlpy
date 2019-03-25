# _*_ coding:utf-8 _*_
# ! /usr/bin/env python
__author__ = 'Administrator'

'''
@created by sjh
2016-06-22
'''

import re

# read log file

# log_list = []
with open(r'G:\wifi_portal_log\project.log.2016-07-30.txt', 'r', encoding='utf-8') as f:
# with open(r'C:\Users\jiaohui\Desktop\wifi_log\project.log.2016-07-26.txt', 'r', encoding='utf-8') as f:
    log_str_lines = f.read()
    # print(len(log_str_lines))

# with open(r'C:\Users\Administrator\Desktop\20160628.txt','r',encoding = 'utf-8') as f:
# 	log = f.readlines()
# 	for line in log:
# 		log_list.append(line.strip('\n'))
# 	log_str = ''.join(log_list)
# 	print(len(log_str))
# define tenant list


# tenant_list = ['bdcsgc', 'nhdh', 'xhcsgc', 'nghx', 'ngcs', 'ngjn']
tenant_list = ['xhcsgc','ngcdfy']
MAC_PATTERN = '[0-9a-fA-F]{2}-[0-9a-fA-F]{2}-[0-9a-fA-F]{2}-[0-9a-fA-F]{2}-[0-9a-fA-F]{2}-[0-9a-fA-F]{2}'
# print('all connect num:'+str(len(re.findall('/connect vs=', log_str))))
for tenant in tenant_list:
    if tenant == 'ngcs':
        # online auth fail
        # auth_fail_pattern = r'Nhcs.*?online auth fail.*\n.*'
        auth_fail_pattern = r'<errcode>.*\n.*' + r'Nhcs.*online auth fail(?:.*\n)+?.*usermac.*'
        auth_retry_pattern = r'/ngcs/connect.*?opType=retry.*?usermac=' + MAC_PATTERN
        auth_retry_fail_pattern = r'Nhcs.*online auth fail.*\n.*opType.*retry\n.*\n.*usermac.*\n.*tenantcode :nhcs'
        # Nhcs.*online auth
        # fail.*\n.*opType.*retry\n.*\n.*usermac.*\n.*tenantcode :nhcs
        auth_retry_suc_pattern = r'Nhcs.*online auth suc.*\n.*opType.*?retry\n(?:.*?\n)+?.*usermac.*\n.*tenantcode :nhcs'
        # Nhcs.*online auth
        # suc.*\n.*opType.*?retry\n(.*?\n){4,6}.*usermac.*\n.*tenantcode :nhcs
        auth_suc_pattern = r'Nhcs.*?online auth suc(?:.*\n)+?.*usermac.*'
    else:
        auth_fail_pattern = r'<errcode>.*\n.*' + tenant.capitalize(
        ) + r'WifiController.*online auth fail(?:.*\n)+?.*usermac.*\n.*tenantcode :' + tenant
        auth_retry_pattern = tenant + r'/connect.*?opType=retry.*?usermac=' + MAC_PATTERN
        auth_retry_fail_pattern = tenant.capitalize(
        ) + r'WifiController.*online auth fail.*\n.*opType.*retry\n.*\n.*usermac.*\n.*tenantcode :' + tenant
        auth_retry_suc_pattern = tenant.capitalize(
        ) + r'WifiController.*online auth suc.*\n.*opType.*?retry\n(?:.*?\n)+?.*usermac.*\n.*tenantcode :' + tenant
        auth_suc_pattern = tenant.capitalize(
        ) + r'WifiController.*?online auth suc(?:.*\n)+?.*usermac.*'
        # auth_suc_pattern = r'/' + tenant + r'/connect.*?usermac=(?:.*\n)+?.*'+tenant.capitalize() + r'WifiController.*?online auth suc(?:.*\n)+?.*usermac.*'
        yijian_pattern = tenant.capitalize(
        ) + r'WifiController.*?yi jian shang wang'
        # auth_fail_pattern = tenant.capitalize(
        # ) + r'WifiController.*.auth fail.*usermac.*tenantcode.*' + tenant
        # auth_retry_pattern = tenant.capitalize(
        # ) + r'WifiController.*.auth success.*retry.*usermac.*tenantcode.*' + tenant
        # auth_retry_fail_pattern = tenant.capitalize(
        # ) + r'WifiController.*.auth fail.*retry.usermac.*tenantcode.*' + tenant
    # 总连接申请
    tenant_index_pattern = r'/' + tenant + \
                             r'/index.*?usermac='+MAC_PATTERN
    tenant_index_list = re.findall(tenant_index_pattern,log_str_lines)
    print(tenant + 'index连接申请数量：' + str(len(tenant_index_list)))
    index_mac = []
    for line in tenant_index_list:
        try:
            index_mac.append(re.findall(MAC_PATTERN, line)[0])
        except IndexError:
            pass
        index_mac = list(set(index_mac))
        # print(suc_mac)
    print(tenant + ' index 连接用户数: ' + str(len(index_mac)))
    print('------------')

    tenant_connect_pattern = r'/' + tenant + \
                             r'/connect.*?usermac='+MAC_PATTERN
    tenant_connect_list = re.findall(tenant_connect_pattern, log_str_lines)
    print(tenant + ' connect 总连接申请数量：' + str(len(tenant_connect_list)))
    connect_mac = []
    for line in tenant_connect_list:
        try:
            connect_mac.append(re.findall(MAC_PATTERN, line)[0])
        except IndexError:
            pass
        connect_mac = list(set(connect_mac))
        # print(suc_mac)
    print(tenant + ' connect用户数: ' + str(len(connect_mac)))
    print(tenant + ' 连index 而未连 connect用户数: ' + str(len(list(set(index_mac)-set(connect_mac)))))
    print('---------------')

    # 认证成功
    tenant_auth_suc = re.findall(auth_suc_pattern, log_str_lines)
    tenant_yijian_suc = re.findall(yijian_pattern, log_str_lines)
    print(tenant + '认证成功数量：' + str(len(tenant_auth_suc)))
    print(tenant + '一键上网成功数量:' + str(len(tenant_yijian_suc)))
    suc_mac = []
    for line in tenant_auth_suc:
        try:
            suc_mac.append(re.findall(MAC_PATTERN, line)[0])
        except IndexError:
            pass
        suc_mac = list(set(suc_mac))
        # print(suc_mac)
    print(tenant + '认证成功用户数: ' + str(len(suc_mac)))
    print('------------')

    # 认证失败
    tenant_auth_fail = re.findall(auth_fail_pattern, log_str_lines)
    print(tenant + '认证失败数量：' + str(len(tenant_auth_fail)))
    fail_mac = []
    for line in tenant_auth_fail:
        fail_mac.append(re.findall(MAC_PATTERN, line)[0])
        fail_mac = list(set(fail_mac))
    print(tenant + '认证失败用户数: ' + str(len(fail_mac)))
    # 一直未认证成功用户
    print(tenant + '影响用户数:' + str(len(list(set(fail_mac) - set(suc_mac)))))
    # 统计认证失败后ip变更又认证成功的用户数量
    # retry_success_mac = list(set(fail_mac)&set(suc_mac))
    # for mac in retry_success_mac:
    #     mac_connect_pattern =

    print('------------')



    # 认证重试
    tenant_retry = re.findall(auth_retry_pattern, log_str_lines)
    retry_mac = []
    for line in tenant_retry:
        retry_mac.append(re.findall(MAC_PATTERN, line)[0])
    retry_mac = list(set(retry_mac))
    print(tenant + '认证重试数量：' + str(len(tenant_retry)))
    print(tenant + '认证重试用户数量：' + str(len(retry_mac)))
    print('------------')

    # 认证重试失败
    tenant_retry_fail = re.findall(auth_retry_fail_pattern, log_str_lines)
    retry_fail_mac = []
    for line in tenant_retry_fail:
        retry_fail_mac.append(re.findall(MAC_PATTERN, line)[0])
    retry_fail_mac = list(set(retry_fail_mac))
    print(tenant + '认证重试失败数量：' + str(len(tenant_retry_fail)))
    print(tenant + '认证重试失败用户数量：' + str(len(retry_fail_mac)))
    print('------------')

    # 认证重试成功
    tenant_retry_suc = re.findall(auth_retry_suc_pattern, log_str_lines)
    # print(tenant_retry_suc)
    retry_suc_mac = []
    usermac_pattern = r'usermac.*?' + MAC_PATTERN
    for line in tenant_retry_suc:
        retry_suc_mac.append(re.findall(usermac_pattern, line)[0])
    retry_suc_mac = list(set(retry_suc_mac))

    print(tenant + '认证重试成功数量：' + str(len(tenant_retry_suc)))
    print(tenant + '认证重试成功用户数量：' + str(len(retry_suc_mac)))
    print('------------')

    # 区分错误码
    mac_list = []
    error_list_H30201 = []
    error_list_H30401 = []
    error_list_P00004 = []
    error_P00004_mac = []
    for line in tenant_auth_fail:
        mac_list.append(re.findall(MAC_PATTERN, line)[0])
        while re.search('H30201', line):
            error_list_H30201.append(re.findall('H30201', line))
            break
        while re.search('H30401', line):
            error_list_H30401.append(re.findall('H30401', line))
            break
        while re.search('P00004', line):
            error_list_P00004.append(re.findall('P00004', line))
            error_P00004_mac.append(re.findall(MAC_PATTERN, line)[0])
            break
    print('认证错误P00004:' + str(len(error_list_P00004)))
    # print(len(error_P00004_mac))
    print('认证错误H30201:' + str(len(error_list_H30201)))
    print('认证错误H30401:' + str(len(error_list_H30401)))
    print('-----------------')
