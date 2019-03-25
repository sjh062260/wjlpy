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
tenant_dict = {'xhcsgc': '10107'}



def Portal(log):
    log_str_lines = log
    # tenant_list = ['bdcsgc', 'nhdh', 'xhcsgc', 'nghx', 'ngcs', 'ngjn']
    # tenant_list = ['xhcsgc']
    for tenant in tenant_dict.keys():
        # online auth suc
        auth_suc_pattern = tenant + r'/connect.*?usermac(?:.*\n)+?.*' + tenant.capitalize() + r'WifiCon.*?online auth suc'
        # online auth fail
        auth_fail_pattern = tenant + r'/connect.*?usermac(?:.*\n)+?.*' + tenant.capitalize() + r'WifiCon.*?online auth fail'
        error_auth_pattern = r'call api fail.*<errcode>.*\n.*' + tenant.capitalize() + r'WifiController.*online auth fail'

        # timeOutOnline
        timeout_online_pattern = r'doUpdateOnline.*call api success.*basId=' + tenant_dict[tenant] + r'.*'

        # 一键上网
        yijian_pattern = tenant.capitalize(
        ) + r'WifiController.*?yi jian shang wang'

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

        # try:
        #     tenant_yijian_suc = re.findall(yijian_pattern, log_str_lines)
        # except:
        #     tenant_yijian_suc = []
        print(tenant + '认证成功数量：' + str(len(tenant_auth_suc)))
        # print(tenant + '一键上网成功数量:' + str(len(tenant_yijian_suc)))
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
        # # 认证重试
        # tenant_retry = re.findall(auth_retry_pattern, log_str_lines)
        # retry_mac = []
        # for line in tenant_retry:
        #     retry_mac.append(re.findall(MAC_PATTERN, line)[0])
        # retry_mac = list(set(retry_mac))
        # print(tenant + '认证重试数量：' + str(len(tenant_retry)))
        # print(tenant + '认证重试用户数量：' + str(len(retry_mac)))
        # print('------------')
        #
        # # 认证重试失败
        # tenant_retry_fail = re.findall(auth_retry_fail_pattern, log_str_lines)
        # retry_fail_mac = []
        # for line in tenant_retry_fail:
        #     retry_fail_mac.append(re.findall(MAC_PATTERN, line)[0])
        # retry_fail_mac = list(set(retry_fail_mac))
        # print(tenant + '认证重试失败数量：' + str(len(tenant_retry_fail)))
        # print(tenant + '认证重试失败用户数量：' + str(len(retry_fail_mac)))
        # print('------------')
        #
        # # 认证重试成功
        # tenant_retry_suc = re.findall(auth_retry_suc_pattern, log_str_lines)
        # # print(tenant_retry_suc)
        # retry_suc_mac = []
        # usermac_pattern = r'usermac.*?' + MAC_PATTERN
        # for line in tenant_retry_suc:
        #     retry_suc_mac.append(re.findall(usermac_pattern, line)[0])
        # retry_suc_mac = list(set(retry_suc_mac))
        #
        # print(tenant + '认证重试成功数量：' + str(len(tenant_retry_suc)))
        # print(tenant + '认证重试成功用户数量：' + str(len(retry_suc_mac)))
        # print('------------')

        error_auth_list = re.findall(error_auth_pattern, log_str_lines)

        # 区分错误码
        # mac_list = []
        error_list_H30201 = []
        error_list_H30401 = []
        error_list_P00004 = []
        error_P00004_mac = []
        for line in error_auth_list:
            # mac_list.append(re.findall(MAC_PATTERN, line)[0])
            while re.search('H30201', line):
                error_list_H30201.append(re.findall('H30201', line))
                break
            while re.search('H30401', line):
                error_list_H30401.append(re.findall('H30401', line))
                break
            while re.search('P00004', line):
                error_list_P00004.append(re.findall('P00004', line))
                # error_P00004_mac.append(re.findall(MAC_PATTERN, line)[0])
                break
        print('认证错误P00004:' + str(len(error_list_P00004)))
        # print(len(error_P00004_mac))
        print('认证错误H30201:' + str(len(error_list_H30201)))
        print('认证错误H30401:' + str(len(error_list_H30401)))
        print('-----------------')
    # 老用户，非手机号验证
    timeout_online = re.findall(timeout_online_pattern, log_str_lines)
    print(tenant + " 超时自动认证：" + str(len(timeout_online)))

#
def Midware(filepath):
    portal_log_file = filepath
    with open(portal_log_file, 'r', encoding='utf-8') as f:
        log_str_lines = f.read()
    for tenant in tenant_dict.keys():
        # 通过微信立即连接上网
        wxOnline_pattern = r'Access log.*/wxOnline basId=' + tenant_dict[tenant] + r'.*openId=.*'
        # 在portal 页点击一键上网，超时自动认证
        outTime_pattern = r'/updateOnlineTime.*basId=' + tenant_dict[tenant] + r'.*'
        outTime_list = re.findall(outTime_pattern, log_str_lines)
        wxOnline_list = re.findall(wxOnline_pattern, log_str_lines)

        print(tenant + " 通过微信立即上网：" + str(len(wxOnline_list)))
        print(tenant + ' PORTAL认证超时，自动联网：' + str(len(outTime_list)))
        # PORTAL 认证超时，自动联网IP数
        # outTime_ip = []
        # for line in outTime_list:
        #     outTime_ip.append(re.findall(IP_PATTERN, line)[0])
        # outTime_ip = list(set(outTime_ip))
        # print("PORTAL 认证超时，自动联网IP数：" + str(len(outTime_ip)))
        #
        # # 通过微信立即上网IP数
        # wxOnline_ip = []
        # for line in wxOnline_list:
        #     wxOnline_ip.append(re.findall(IP_PATTERN, line)[0])
        # wxOnline_ip = list(set(wxOnline_ip))
        # print("通过微信立即上网IP 数量：" + str(len(wxOnline_ip)))

        # 最终不能上网IP, 在上网认证失败，不在微信上网，超时自动联网
        # final_effect_ip = []
        # online_ip =list(set(wxOnline_ip+outTime_ip))
        # final_effect_ip = list(set(online_fail_ip)-set(online_ip))
        # print("最终无法上网IP数:"+str(len(online_fail_ip)))
        # print("----------------------------")

def IndexCount(logs):
    log_str_lines = logs
    index_pattern = r'/xhcsgc/index.*usermac.*'
    index_list = re.findall(index_pattern,log_str_lines)
    index_access_num = len(index_list)
    # print("index 连接数 :"+str(index_access_num))

    index_mac = []
    for line in index_list:
        # print(line)
        try:
            index_mac.append(re.findall(r'xhcsgc.*usermac=(.+?)\|',line)[0])
        except IndexError:
            pass

    index_mac = list(set(index_mac))
    print("index 请求用户数："+str(len(index_mac)))
    # print(index_mac)
    # count = 0
    # for mac in index_mac:
    #     if len(mac)==12:
    #         count =count+1
            # print(count,mac,len(mac))
    # print("index 连接数 :"+str(len(index_list))+" index access 用户数 :"+str(len(index_mac)))
    return index_mac

def ConnectCount(logs):
    log_str_lines = logs
    # connect_pattern = r'portal/connect vs.*usermac=.*(?:.*\n)+?.*' + r'WifiCon.*?online auth.*(?:.*\n)+?.*'+r'toWaitForPage.*'
    connect_pattern = r'xhcsgc/connect vs.*usermac.*'
    connect_list = re.findall(connect_pattern,log_str_lines)
    # print("connect access num :"+str(len(connect_list)))

    connect_mac = []
    for line in connect_list:
        try:
            connect_mac.append(re.findall(r'usermac=(.+?)\|',line)[0])
        except IndexError:
            pass
    connect_mac = list(set(connect_mac))
    # print("connect access mac :"+ str(len(connect_mac)))

    auth_suc_pattern = r'XhcsgcWifiController\.connect.*online auth suc.*\n.*addFreeCreditFlag.*'
    auth_suc_list = re.findall(auth_suc_pattern,log_str_lines)
    connect_suc_mac = []
    for line in auth_suc_list:
        try:
            connect_suc_mac.append(re.findall(MAC_PATTERN,line)[0])
        except IndexError:
            pass
    connect_suc_mac = list(set(connect_suc_mac))
    # print(connect_suc_mac)
    effect_mac = list(set(connect_mac)-set(connect_suc_mac))
    # print(len(effect_mac))
    print("Conncet access num : "+str(len(connect_list))+" Connect access mac :"+str(len(connect_mac))+" 认证成功数："+str(len(auth_suc_list))+" 认证成功MAC :"+str(len(connect_suc_mac)))
    print("conncet auth fail mac "+str(len(effect_mac)))
    # auth_fail_pattern = r'XhcsgcWifiController\.connect.*online auth fail.*'
    # auth_fail_list = re.findall(auth_fail_pattern,log_str_lines)
    # connect_fail_mac = []
    # for line in auth_fail_list:
    #     try:
    #         connect_fail_mac.append(re.findall(MAC_PATTERN,line)[0])
    #     except IndexError:
    #         pass
    # connect_fail_mac = list(set(connect_fail_mac))
    # print("connect auth fail num  "+ str(len(auth_fail_list))+"connect auth fail mac "+ str(len(connect_fail_mac)))


    return connect_mac

def CallApiFail(logs):
    log_str_line = logs
    call_api_fail_pattern = r'call api fail.*basId=10107.*'

    call_api_fail_list = re.findall(call_api_fail_pattern,log_str_line)

    print("call api fail num :"+ str(len(call_api_fail_list)))
    effect_ip = []
    for line in call_api_fail_list:
        try:
            effect_ip.append(re.findall(r'userIp=(.+?)\&',line)[0])
        except IndexError:
            pass
    effect_ip = list(set(effect_ip))

    print("effect_ip num :" + str(len(effect_ip)))

def timeOutOnline(logs):
    log_str_lines = logs
    timeOutOnline_pattern = r'Access log.*xhcsgc/timeOutOnline.*'
    timeOutOnline_list = re.findall(timeOutOnline_pattern,log_str_lines)
    # print("timeOutOnline access num :"+str(len(timeOutOnline_list)))

    timeOutOnline_mac = []
    for line in timeOutOnline_list:
        try:
            timeOutOnline_mac.append(re.findall(r'xhcsgc.*usermac=(.+?)\|',line)[0])
        except IndexError:
            pass
    timeOutOnline_mac = list(set(timeOutOnline_mac))
    print("timeOutOnline Requests num:"+str(len(timeOutOnline_list))+" timeOutOnline mac :"+str(len(timeOutOnline_mac)))
    return timeOutOnline_mac

def jumpWxWifi(logs):
    log_str_lines = logs
    jumpWxWifi_pattern = r'Access log.*/portal/jumpWxWifi.*usermac.*'
    jumpWxWifi_list = re.findall(jumpWxWifi_pattern,log_str_lines)
    # print("jumpWxWifi access num :"+str(len(jumpWxWifi_list)))

    jumpWx_mac = []
    for line in jumpWxWifi_list:
        try:
            jumpWx_mac.append(re.findall(r'usermac=(.+?)\|',line)[0])
        except IndexError:
            pass
    jumpWx_mac = list(set(jumpWx_mac))
    print("jumpWx mac :"+str(len(jumpWx_mac)))

    return jumpWx_mac

def toUserRedirectUrl(logs):
    log_str_lines = logs
    toUserRedirectUrl_pattern = r'WifiPortalControl.*toUserRedirectUrl.*'
    toUserRedirectUrl_list = re.findall(toUserRedirectUrl_pattern,log_str_lines)
    # print("toUserRedirect access num :"+str(len(toUserRedirectUrl_list)))

    toUserRedirectUrl_suc_pattern = r'call api success.*userIp.*\n.*WifiPortalControl.*toUserRedirectUrl.*free portal online auth suc'
    toUserRedirectUrl_suc = re.findall(toUserRedirectUrl_suc_pattern,log_str_lines)
    # print("toUserRedirect auth suc :"+str(len(toUserRedirectUrl_suc)))
    userIp = []
    for line in toUserRedirectUrl_suc:
        try:
            userIp.append(re.findall(r'userIp=(.+?)\&',line)[0])
        except IndexError:
            pass
    userIp = list(set(userIp))
    # print("toRedirectUrl user ip num :"+str(len(userIp)))


    toUserRedirectUrl_fail_pattern = r'call api fail.*userIp.*\n.*WifiPortalControl.*toUserRedirectUrl.*free portal online auth fail'
    toUserRedirectUrl_fail = re.findall(toUserRedirectUrl_fail_pattern,log_str_lines)
    fail_ip = []
    for line in toUserRedirectUrl_fail:
        try:
            fail_ip.append((re.findall(r'userIp=(.+?)(&|\|)',line)[0])[0])
        except IndexError:
            pass
    fail_ip = list(set(fail_ip))
    print("toUserRedirect 认证失败数 :"+str(len(toUserRedirectUrl_fail))+"认证失败ip:"+str(len(fail_ip)))

def getFreeCreditMobile(logs):
    log_str_lines = logs
    getFreeCreditMobile_pattern = r'Access log.*xhcsgc/index(?:.*\n)+?.*getFreeCreditMobile'
    getFreeCreditMobile_list = re.findall(getFreeCreditMobile_pattern,log_str_lines)
    # print("getFree Credit num :"+ str(len(getFreeCreditMobile_list)))

    getFreeCreditMobile_mac = []
    for line in getFreeCreditMobile_list:
        # print(line)
        try:
            # if '90-3C-92-55-8E-D5' in line:
            #     print(line)
            # getFreeCreditMobile_mac.append((re.findall(r'usermac=(.+?)(&|\|)',line)[0])[0])
            getFreeCreditMobile_mac.append(re.findall(r'xhcsgc.*usermac=(.+?)\|',line)[0])
        except IndexError:
            pass

    getFreeCreditMobile_mac = list(set(getFreeCreditMobile_mac))


    print("get free credit mac :"+str(len(getFreeCreditMobile_mac)))
    # print(getFreeCreditMobile_mac)
    return getFreeCreditMobile_mac

def wxOnline(logs):
    log_str_lines = logs
    wxOnline_pattern = r'Access log.*/wxOnline basId=10107.*'
    wxOnline_list = re.findall(wxOnline_pattern,log_str_lines)

    wxOnline_openId = []
    for line in wxOnline_list:
        try:
            wxOnline_openId.append(re.findall(r'openId=(.+?)\|',line)[0])
        except IndexError:
            pass
    wxOnline_openId = list(set(wxOnline_openId))
    print("wxOnline requests :"+str(len(wxOnline_list))+"wxOnline requests openId :"+str(len(wxOnline_openId)))




if __name__ == "__main__":
    # with open(r'G:\portal_midware_log\project.log.2016-09-20.txt',mode='r',encoding='utf-8') as w:
    #     midware_logs = w.read()
    # wxOnline(midware_logs)
    portal_log_file1 = r'G:\wifi_portal_log\project.log.2016-09-19-01.txt'
    portal_log_file2 = r'G:\wifi_portal_log\project.log.2016-09-19.txt'
    portal_log_file3 = r'G:\wifi_portal_log\project.log.2016-09-19-02.txt'
    try:
        f1 = open(portal_log_file1,'r',encoding='utf-8')
        log_str_lines1 = f1.read()
        f1.close()
    except:
        log_str_lines1 = ''
    try:
        f2 = open(portal_log_file2,'r',encoding='utf-8')
        log_str_lines2 = f2.read()
        f2.close()
    except:
        log_str_lines2 = ''
    try:
        f3 = open(portal_log_file3,'r',encoding='utf-8')
        log_str_lines3 = f3.read()
        f3.close()
    except:
        log_str_lines3=''

    # log_str_lines1 = f1.read()
    # log_str_lines2 = f2.read()
    # with open(portal_log_file1, 'r', encoding='utf-8') as f:
    #     log_str_lines1 = f.read()
    # with open(portal_log_file2, 'r', encoding='utf-8') as f2:
    #     log_str_lines2 = f.read()
    log_str_lines = log_str_lines1+log_str_lines2+log_str_lines3
    log_str_lines1=log_str_lines2 = log_str_lines3 = ''


    # Portal(log_str_lines)
    index_mac =IndexCount(log_str_lines)
    ConnectCount(log_str_lines)
    timeOutOnline(log_str_lines)
    CallApiFail(log_str_lines)
    # getFreeCreditMobile_mac = getFreeCreditMobile(log_str_lines)

    # print(list(set(index_mac)-set(connect_mac+timeOutOnline_mac)))
    # print(len(list(set(index_mac)-set(connect_mac+timeOutOnline_mac))))
    # print(list(set(getFreeCreditMobile_mac)-set(index_mac)))
    # print(list(set(index_mac)-set(getFreeCreditMobile_mac)))