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
# tenant_dict = {'xhcsgc': '10107'}
tenant_list = ['xhcsgc','mallshow','sydyc','ngcs','bdcsgc','nghx','ngjn','nhdh','wsq']
def Tenant_Connect_Auth(filepath):
    portal_log_file = filepath
    with open(portal_log_file, 'r', encoding='utf-8') as f:
        log_str_lines = f.read()
    for tenant in tenant_list:
        auth_suc_pattern = tenant + r'/connect.*?usermac(?:.*\n)+?.*' + tenant.capitalize() + r'WifiCon.*?online auth suc'
        auth_fail_pattern = tenant + r'/connect.*?usermac(?:.*\n)+?.*' + tenant.capitalize() + r'WifiCon.*?online auth fail'
        tenant_index_pattern = r'/' + tenant + r'/index.*?usermac=' + MAC_PATTERN

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

        # tenant_connect_pattern = r'/' + tenant + \
        #                          r'/connect.*?usermac=' + MAC_PATTERN
        # tenant_connect_list = re.findall(tenant_connect_pattern, log_str_lines)
        # print(tenant + ' connect 总连接申请数量：' + str(len(tenant_connect_list)))
        # connect_mac = []
        # for line in tenant_connect_list:
        #     try:
        #         connect_mac.append(re.findall(MAC_PATTERN, line)[0])
        #     except IndexError:
        #         pass
        #     connect_mac = list(set(connect_mac))
        #     # print(suc_mac)
        #
        # print(tenant + ' connect用户数: ' + str(len(connect_mac)))
        # print(tenant + ' 连index 而未连 connect用户数: ' + str(len(list(set(index_mac) - set(connect_mac)))))
        # print('---------------')
        #
        # # 认证成功
        # try:
        #     tenant_auth_suc = re.findall(auth_suc_pattern, log_str_lines)
        # except:
        #     tenant_auth_suc = []
        #     pass
        #
        # try:
        #     tenant_yijian_suc = re.findall(yijian_pattern, log_str_lines)
        # except:
        #     tenant_yijian_suc = []
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
        #
        # print(tenant + '认证成功用户数: ' + str(len(suc_mac)))
        # print('------------')

        # 认证失败
        # tenant_auth_fail = re.findall(auth_fail_pattern, log_str_lines)
        # print(tenant + '认证失败数量：' + str(len(tenant_auth_fail)))
        # fail_mac = []
        # for line in tenant_auth_fail:
        #     fail_mac.append(re.findall(MAC_PATTERN, line)[0])
        #     fail_mac = list(set(fail_mac))
        # print(tenant + '认证失败用户数: ' + str(len(fail_mac)))
        # # 一直未认证成功用户
        # print(tenant + '影响用户数:' + str(len(list(set(fail_mac) - set(suc_mac)))))
        print("------------------------")

def Connect_Auth(filepath):
    portal_log_file = filepath
    with open(portal_log_file, 'r', encoding='utf-8') as f:
        log_str_lines = f.read()
    auth_suc_pattern = r'/connect.*?usermac(?:.*\n)+?.*WifiCon.*?online auth suc'
    auth_fail_pattern = r'/connect.*?usermac(?:.*\n)+?.*WifiCon.*?online auth fail'
    index_pattern = r'Access log.*/index.*?usermac='+MAC_PATTERN
    # index_pattern = r'Access log.*/index.*usermac=.*'
    tenant_index_list = re.findall(index_pattern, log_str_lines)
    print('index连接申请数量：' + str(len(tenant_index_list)))
    index_mac = []
    for line in tenant_index_list:
        try:
            index_mac.append(re.findall(MAC_PATTERN, line)[0])
        except IndexError:
            pass
        index_mac = list(set(index_mac))
        # print(suc_mac)
    # cdfy index mac
    # cdfy_index_mac_pattern = r'portal/index ssid=FanyueMall.*usermac=(.{12})'
    # index_mac_hw = []
    # for line in tenant_index_list:
    #     try:
    #         index_mac_hw.append(re.findall(cdfy_index_mac_pattern,line)[0])
    #     except IndexError:
    #         pass
    #     index_mac_hw = list(set(index_mac_hw))
    # print("cdfy index mac:"+ str(len(index_mac_hw)))
    print(' index 连接用户数: ' + str(len(index_mac)))
    print('------------')

    connect_pattern = r'/connect.*?usermac=' + MAC_PATTERN
    connect_list = re.findall(connect_pattern, log_str_lines)
    print(' connect 总连接申请数量：' + str(len(connect_list)))
    connect_mac = []
    for line in connect_list:
        try:
            connect_mac.append(re.findall(MAC_PATTERN, line)[0])
        except IndexError:
            pass
        connect_mac = list(set(connect_mac))
        # print(suc_mac)

    print(' connect用户数: ' + str(len(connect_mac)))
    print(' 连index 而未连 connect用户数: ' + str(len(list(set(index_mac) - set(connect_mac)))))
    print('---------------')

    # 认证成功
    try:
        tenant_auth_suc = re.findall(auth_suc_pattern, log_str_lines)
    except:
        tenant_auth_suc = []
        pass

    # try:
    #     tenant_yijian_suc = re.findall(yijian_pattern, log_str_lines)
    # except:
    #     tenant_yijian_suc = []
    print('认证成功数量：' + str(len(tenant_auth_suc)))
    # print(tenant + '一键上网成功数量:' + str(len(tenant_yijian_suc)))
    suc_mac = []
    for line in tenant_auth_suc:
        try:
            suc_mac.append(re.findall(MAC_PATTERN, line)[0])
        except IndexError:
            pass
        suc_mac = list(set(suc_mac))
        # print(suc_mac)

    print('认证成功用户数: ' + str(len(suc_mac)))
    print('------------')

    # 认证失败
    auth_fail = re.findall(auth_fail_pattern, log_str_lines)
    print('认证失败数量：' + str(len(auth_fail)))
    fail_mac = []
    for line in auth_fail:
        fail_mac.append(re.findall(MAC_PATTERN, line)[0])
        fail_mac = list(set(fail_mac))
    print('认证失败用户数: ' + str(len(fail_mac)))
    # 一直未认证成功用户
    print('影响用户数:' + str(len(list(set(fail_mac) - set(suc_mac)))))

    # print("************************** WIFI PORTAL 用户访问和新用户认证统计 ***************************")
    # print("*Index Req******Index Mac*****Connect Req*****Connect Mac*****Auth Suc Req*****Auth Suc Mac*****Auth Fail Req*****Auth Fail MAC*****Effect Mac*")
    # print("*%s*")




if __name__ == "__main__":
    portal_log_file = r'G:\wifi_portal_log\project.log.2016-09-12-01.txt'
    Connect_Auth(portal_log_file)
    # Tenant_Connect_Auth(portal_log_file)

