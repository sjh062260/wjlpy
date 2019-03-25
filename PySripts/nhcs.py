# _*_ coding:utf-8 _*_
# ! /usr/bin/env python
__author__ = 'Administrator'

'''
@created by sjh
2016-06-22
'''

import re

MAC_PATTERN = '[0-9a-fA-F]{2}-[0-9a-fA-F]{2}-[0-9a-fA-F]{2}-[0-9a-fA-F]{2}-[0-9a-fA-F]{2}-[0-9a-fA-F]{2}'
IP_PATTERN = r'userIp=([0-9]{1,3}\.){3}[0-9]{1,3}'
tenant_dict = {'ngcs': '10105'}


def Portal(filepath):
    portal_log_file = filepath
    with open(portal_log_file, 'r', encoding='utf-8') as f:
        log_str_lines = f.read()
    # tenant_list = ['bdcsgc', 'nhdh', 'xhcsgc', 'nghx', 'ngcs', 'ngjn']
    # tenant_list = ['xhcsgc']
    for tenant in tenant_dict.keys():
        # online auth suc
        auth_suc_pattern = tenant + r'/connect.*?usermac(?:.*\n)+?.*NhcsWifiCon.*connect.*?online auth suc'
        # online auth fail
        auth_fail_pattern = tenant + r'/connect.*?usermac(?:.*\n)+?.*NhcsWifiCon.*connect.*?online auth fail'
        error_auth_pattern = r'call api fail.*<errcode>.*\n.*NhcsWifiCon.*connect.*online auth fail'

        # timeOutOnline
        timeout_online_pattern = r'doUpdateOnline.*call api success.*basId=' + tenant_dict[tenant] + r'.*'

        # 一键上网
        yijian_pattern = r'NhcsWifiController.*?yi jian shang wang'

        # portal index 页面
        tenant_index_pattern = r'/' + tenant + \
                               r'/index.*?usermac=' + MAC_PATTERN
        tenant_index_list = re.findall(tenant_index_pattern, log_str_lines)
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
                                 r'/connect.*?usermac=' + MAC_PATTERN
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
        print(tenant + ' 连index 而未连 connect用户数: ' + str(len(list(set(index_mac) - set(connect_mac)))))
        print('---------------')

        # 认证成功
        try:
            tenant_auth_suc = re.findall(auth_suc_pattern, log_str_lines)
        except:
            tenant_auth_suc = []
            pass

        try:
            tenant_yijian_suc = re.findall(yijian_pattern, log_str_lines)
        except:
            tenant_yijian_suc = []
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


        error_auth_list = re.findall(error_auth_pattern, log_str_lines)

        # # 区分错误码
        # # mac_list = []
        # error_list_H30201 = []
        # error_list_H30401 = []
        # error_list_P00004 = []
        # error_P00004_mac = []
        # for line in error_auth_list:
        #     # mac_list.append(re.findall(MAC_PATTERN, line)[0])
        #     while re.search('H30201', line):
        #         error_list_H30201.append(re.findall('H30201', line))
        #         break
        #     while re.search('H30401', line):
        #         error_list_H30401.append(re.findall('H30401', line))
        #         break
        #     while re.search('P00004', line):
        #         error_list_P00004.append(re.findall('P00004', line))
        #         # error_P00004_mac.append(re.findall(MAC_PATTERN, line)[0])
        #         break
        # print('认证错误P00004:' + str(len(error_list_P00004)))
        # # print(len(error_P00004_mac))
        # print('认证错误H30201:' + str(len(error_list_H30201)))
        # print('认证错误H30401:' + str(len(error_list_H30401)))
        # print('-----------------')
    # 老用户，非手机号验证
    # timeout_online = re.findall(timeout_online_pattern, log_str_lines)
    # print(tenant + " 超时自动认证：" + str(len(timeout_online)))

    jumpwxOnline_pattern = tenant+r'/jumpWxWifi.*'
    jumpwxOnline = re.findall(jumpwxOnline_pattern,log_str_lines)
    print("jump wxOnline "+str(len(jumpwxOnline)))
    # print(jumpwxOnline)

    jump_mac = []
    for line in jumpwxOnline:
        jump_mac.append(re.findall(MAC_PATTERN,line)[0])
        # print(jump_mac)
    jump_mac = list(set(jump_mac))
    print("jump mac "+ str(len(jump_mac)))
    wxOnline_pattern = tenant+r'/wxOnline.*openId.*'
    wxOnline = re.findall(wxOnline_pattern,log_str_lines)
    print("wxOnline "+ str(len(wxOnline)))

    no_portal_suc_pattern = tenant+r'/index.*?usermac=(?:.*\n)+?.*NhcsWifiCon.*no portal online auth suc'
    no_portal_suc = re.findall(no_portal_suc_pattern,log_str_lines)
    # print(len(no_portal_suc))
    no_portal_fail_pattern = tenant+r'/index.*?usermac=(?:.*\n)+?.*NhcsWifiCon.*no portal online auth fail'
    no_portal_fail = re.findall(no_portal_fail_pattern,log_str_lines)
    print(len(no_portal_fail))

    no_portal_suc_mac = []
    no_portal_fail_mac =[]

    for line in no_portal_suc:
        no_portal_suc_mac.append(re.findall(MAC_PATTERN,line)[0])
    no_portal_suc_mac = list(set(no_portal_suc_mac))
    # print("no portal suc mac"+str(len(no_portal_suc_mac)))
    for line in no_portal_fail:
        no_portal_fail_mac.append(re.findall(MAC_PATTERN,line)[0])
    no_portal_fail_mac = list(set(no_portal_fail_mac))
    # print("no portal fail mac"+str(len(no_portal_fail_mac)))
    print("no portal effect user "+ str(len(list(set(no_portal_fail_mac)-set(no_portal_suc_mac)))))

def Midware(filepath):
    portal_log_file = filepath
    with open(portal_log_file, 'r', encoding='utf-8') as f:
        log_str_lines = f.read()
    for tenant in tenant_dict.keys():
        # 通过微信立即连接上网
        wxOnline_pattern = r'/wxOnline basId=' + tenant_dict[tenant] + r'.*openId=.*'
        # 在portal 页点击一键上网，超时自动认证
        # outTime_pattern = r'/updateOnlineTime.*basId=' + tenant_dict[tenant] + r'.*'

        # outTime_list = re.findall(outTime_pattern, log_str_lines)
        outTimeOnline_pattern = r'timeOutOnline basId='+ tenant_dict[tenant]
        wxOnline_list = re.findall(wxOnline_pattern, log_str_lines)
        outTimeOnline = re.findall(outTimeOnline_pattern,log_str_lines)

        print(tenant + " 通过微信立即上网：" + str(len(wxOnline_list)))
        print(tenant + ' PORTAL认证超时，自动联网：' + str(len(outTimeOnline)))


if __name__ == "__main__":
    portal_log_file = r'G:\wifi_portal_log\project.log.2016-08-18.txt'
    # midware_log_file = r'G:\portal_midware_log\project.log.2016-08-23.txt'
    Portal(portal_log_file)
    # Midware(midware_log_file)
