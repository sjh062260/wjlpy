# _*_ coding:utf-8 _*_
# ! /usr/bin/env python
__author__ = 'Administrator'

'''
@created by sjh
2016-06-22
'''

import re
# portal 日志
with open(r'G:\wifi_portal_log\project.log.2016-08-08.txt', 'r', encoding='utf-8') as f:
    portal_logs = f.read()
# midware 日志
with open(r'G:\portal_midware_log\project.log.2016-08-08.txt', 'r', encoding='utf-8') as f:
    midware_logs = f.read()



# tenant_list = ['bdcsgc', 'nhdh', 'xhcsgc', 'nghx', 'ngcs', 'ngjn']
# basId_list = {'ngcdfy':'10112','xhcsgc':'10107'}
basId_list = {'ngcdfy':'10112'}
# tenant_list = ['ngcdfy']
# MAC_PATTERN = '[0-9a-fA-F]{2}-[0-9a-fA-F]{2}-[0-9a-fA-F]{2}-[0-9a-fA-F]{2}-[0-9a-fA-F]{2}-[0-9a-fA-F]{2}'
MAC_PATTERN = r'usermac=.{12}'
IP_PATTERN = r'userIp=([0-9]{1,3}\.){3}[0-9]{1,3}'
for tenant in basId_list.keys():
    # 正则规则
    # 连接SSID ,进入index页面
    tenant_index_pattern = tenant+r'/index.*'+MAC_PATTERN

    # 在portal 页点击一键上网，超时自动认证
    tenant_outtime_pattern= r'/updateOnlineTime.*basId='+basId_list[tenant]+r'.*'
    # 中间层发送认证到AC, AC返回认证失败
    tenant_online_fail_pattern = r'call api fail.*basId='+basId_list[tenant]+r'.*errcode.*\n.*?'+tenant.capitalize()+r'.*onlineTmp auth fail'
    # tenant_online_fail_pattern = r'wifi\.pages\.'+tenant.capitalize()+r'.*onlineTmp auth fail'
    # 认证失败错误码
    H30401_ERROR_pattern = r'basId='+basId_list[tenant]+r'.*<errcode>H30401'
    # H30402_ERROR_pattern = r'basId='+basId_list[tenant]+r'.*<errcode>H30402'
    H30203_ERROR_pattern = r'basId='+basId_list[tenant]+r'.*<errcode>H30203'
    H30404_ERROR_pattern = r'basId='+basId_list[tenant]+r'.*<errcode>H30404'
    P00004_ERROR_pattern = r'basId='+basId_list[tenant]+r'.*<errcode>P00004'
    # 通过微信立即连接上网
    wxOnlie_pattern =  r'Access log.*/wxOnline basId=' + basId_list[tenant] + r'.*openId=.*'

    tenant_index_list = re.findall(tenant_index_pattern,portal_logs)
    tenant_online_fail_list = re.findall(tenant_online_fail_pattern,portal_logs)
    # H30401_ERROR_list = re.findall(H30401_ERROR_pattern,midware_logs)
    # H30203_ERROR_list = re.findall(H30203_ERROR_pattern,midware_logs)
    # H30404_ERROR_list = re.findall(H30404_ERROR_pattern,midware_logs)
    # P00004_ERROR_list = re.findall(P00004_ERROR_pattern,midware_logs)
    # H30404_ERROR_list = re.findall(H30404_ERROR_pattern,midware_logs)
    tenant_outtime_list = re.findall(tenant_outtime_pattern,midware_logs)
    wxOnlie_list = re.findall(wxOnlie_pattern,midware_logs)

    H30401_ERROR = []
    H30203_ERROR = []
    H30404_ERROR = []
    P00004_ERROR = []
    
    for line in tenant_online_fail_list:
        try:
            H30401_ERROR.append(re.findall(H30401_ERROR_pattern,line)[0])
            H30404_ERROR.append(re.findall(H30404_ERROR_pattern,line)[0])
            H30203_ERROR.append(re.findall(H30203_ERROR_pattern,line)[0])
            P00004_ERROR.append(re.findall(P00004_ERROR_pattern,line)[0])
        except IndexError:
            pass
    print(tenant + ' index连接申请数量：' + str(len(tenant_index_list)))
    print(tenant+' AC 返回上网认证失败:'+str(len(tenant_online_fail_list)))
    print(tenant+" 通过微信立即上网："+str(len(wxOnlie_list)))
    print(tenant+' PORTAL认证超时，自动联网：'+str(len(tenant_outtime_list)))
    print(tenant+' H30401 错误码：'+str(len(H30401_ERROR)))
    print(tenant+' H30404 错误码：'+str(len(H30404_ERROR)))
    print(tenant+' H30203 错误码：'+str(len(H30203_ERROR)))
    print(tenant+' P00004 错误码：'+str(len(P00004_ERROR)))

    index_mac = []
    for line in tenant_index_list:
        try:
            index_mac.append(re.findall(MAC_PATTERN, line)[0])
        except IndexError:
            pass
        index_mac = list(set(index_mac))
    print(tenant + ' index 连接用户数: ' + str(len(index_mac)))
    print('------------')

    wx_openId = []
    for line in wxOnlie_list:
        try:
            wx_openId.append(re.findall(r'openId=(.{28})', line)[0])
        except IndexError:
            pass
    print(len(wx_openId))
    wx_openId = list(set(wx_openId))
    print(tenant + ' 微信一键上网openId数: ' + str(len(wx_openId)))
    print('------------')

    # AC 返回上网认证失败ip数
    online_fail_ip = []
    for line in tenant_online_fail_list:
        online_fail_ip.append(re.findall(IP_PATTERN,line)[0])
    online_fail_ip = list(set(online_fail_ip))
    print("AC 返回上网认证失败IP数："+str(len(online_fail_ip)))

    # PORTAL 认证超时，自动联网IP数
    outTime_ip = []
    for line in tenant_outtime_list:
        outTime_ip.append(re.findall(IP_PATTERN,line)[0])
    outTime_ip = list(set(outTime_ip))
    print("PORTAL 认证超时，自动联网IP数："+str(len(outTime_ip)))

    # 通过微信立即上网IP数
    wxOnline_ip = []
    for line in wxOnlie_list:
        wxOnline_ip.append(re.findall(IP_PATTERN,line)[0])
    wxOnline_ip = list(set(wxOnline_ip))
    print("通过微信立即上网IP 数量："+str(len(wxOnline_ip)))

    # 最终不能上网IP, 在上网认证失败，不在微信上网，超时自动联网
    final_effect_ip = []
    online_ip =list(set(wxOnline_ip+outTime_ip))
    final_effect_ip = list(set(online_fail_ip)-set(online_ip))
    print("最终无法上网IP数:"+str(len(online_fail_ip)))
    print("----------------------------")

    # tenant_connect_pattern = r'/' + tenant + \
    #                          r'/connect.*?usermac='+MAC_PATTERN
    # tenant_connect_list = re.findall(tenant_connect_pattern, portal_logs)
    # print(tenant + ' connect 总连接申请数量：' + str(len(tenant_connect_list)))
    # connect_mac = []
    # for line in tenant_connect_list:
    #     try:
    #         connect_mac.append(re.findall(MAC_PATTERN, line)[0])
    #     except IndexError:
    #         pass
    #     connect_mac = list(set(connect_mac))
    #     # print(suc_mac)
    # print(tenant + ' connect用户数: ' + str(len(connect_mac)))
    # print(tenant + ' 连index 而未连 connect用户数: ' + str(len(list(set(index_mac)-set(connect_mac)))))
    # print('---------------')

    # # 认证成功
    # tenant_auth_suc = re.findall(auth_suc_pattern, portal_logs)
    # tenant_yijian_suc = re.findall(yijian_pattern, portal_logs)
    # print(tenant + '认证成功数量：' + str(len(tenant_auth_suc)))
    # print(tenant + '一键上网成功数量:' + str(len(tenant_yijian_suc)))
    # suc_mac = []
    # for line in tenant_auth_suc:
    #     try:
    #         suc_mac.append(re.findall(MAC_PATTERN, line)[0])
    #     except IndexError:
    #         pass
    #     suc_mac = list(set(suc_mac))
    #     # print(suc_mac)
    # print(tenant + '认证成功用户数: ' + str(len(suc_mac)))
    # print('------------')

    # # 认证失败
    # tenant_auth_fail = re.findall(auth_fail_pattern, portal_logs)
    # print(tenant + '认证失败数量：' + str(len(tenant_auth_fail)))
    # fail_mac = []
    # for line in tenant_auth_fail:
    #     fail_mac.append(re.findall(MAC_PATTERN, line)[0])
    #     fail_mac = list(set(fail_mac))
    # print(tenant + '认证失败用户数: ' + str(len(fail_mac)))
    # # 一直未认证成功用户
    # print(tenant + '影响用户数:' + str(len(list(set(fail_mac) - set(suc_mac)))))
    # # 统计认证失败后ip变更又认证成功的用户数量
    # # retry_success_mac = list(set(fail_mac)&set(suc_mac))
    # # for mac in retry_success_mac:
    # #     mac_connect_pattern =

    # print('------------')



    # # 认证重试
    # tenant_retry = re.findall(auth_retry_pattern, portal_logs)
    # retry_mac = []
    # for line in tenant_retry:
    #     retry_mac.append(re.findall(MAC_PATTERN, line)[0])
    # retry_mac = list(set(retry_mac))
    # print(tenant + '认证重试数量：' + str(len(tenant_retry)))
    # print(tenant + '认证重试用户数量：' + str(len(retry_mac)))
    # print('------------')

    # # 认证重试失败
    # tenant_retry_fail = re.findall(auth_retry_fail_pattern, portal_logs)
    # retry_fail_mac = []
    # for line in tenant_retry_fail:
    #     retry_fail_mac.append(re.findall(MAC_PATTERN, line)[0])
    # retry_fail_mac = list(set(retry_fail_mac))
    # print(tenant + '认证重试失败数量：' + str(len(tenant_retry_fail)))
    # print(tenant + '认证重试失败用户数量：' + str(len(retry_fail_mac)))
    # print('------------')

    # # 认证重试成功
    # tenant_retry_suc = re.findall(auth_retry_suc_pattern, portal_logs)
    # # print(tenant_retry_suc)
    # retry_suc_mac = []
    # usermac_pattern = r'usermac.*?' + MAC_PATTERN
    # for line in tenant_retry_suc:
    #     retry_suc_mac.append(re.findall(usermac_pattern, line)[0])
    # retry_suc_mac = list(set(retry_suc_mac))

    # print(tenant + '认证重试成功数量：' + str(len(tenant_retry_suc)))
    # print(tenant + '认证重试成功用户数量：' + str(len(retry_suc_mac)))
    # print('------------')

    # # 区分错误码
    # mac_list = []
    # error_list_H30201 = []
    # error_list_H30401 = []
    # error_list_P00004 = []
    # error_P00004_mac = []
    # for line in tenant_auth_fail:
    #     mac_list.append(re.findall(MAC_PATTERN, line)[0])
    #     while re.search('H30201', line):
    #         error_list_H30201.append(re.findall('H30201', line))
    #         break
    #     while re.search('H30401', line):
    #         error_list_H30401.append(re.findall('H30401', line))
    #         break
    #     while re.search('P00004', line):
    #         error_list_P00004.append(re.findall('P00004', line))
    #         error_P00004_mac.append(re.findall(MAC_PATTERN, line)[0])
    #         break
    # print('认证错误P00004:' + str(len(error_list_P00004)))
    # # print(len(error_P00004_mac))
    # print('认证错误H30201:' + str(len(error_list_H30201)))
    # print('认证错误H30401:' + str(len(error_list_H30401)))
    # print('-----------------')
