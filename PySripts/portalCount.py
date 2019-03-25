# _*_ coding:utf-8 _*_
# ! /usr/bin/env python
__author__ = 'Administrator'

import re

MAC_PATTERN = r'usermac=(.{12,17})'

def Ngcdfy():
    portal_log_file = filepath
    with open(portal_log_file, 'r', encoding='utf-8') as f:
        log_str_lines = f.read()
    #index
    index_pattern = r'Access log.*/portal/index ssid=FanyueMall.*usermac.*'

    # connect
    # connect_pattern =
    auth_suc_pattern = r'/connect.*?usermac(?:.*\n)+?.*WifiCon.*?online auth suc'
    auth_fail_pattern = r'/connect.*?usermac(?:.*\n)+?.*WifiCon.*?online auth fail'
    # index_pattern = r'Access log.*/index.*usermac=.*'
    tenant_index_list = re.findall(index_pattern, log_str_lines)
    print('index连接申请数量：' + str(len(tenant_index_list)))
    index_mac = []
    for line in tenant_index_list:
        try:
            index_mac.append(re.findall(r'usermac=(.+?)\|', line)[0])
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

    connect_pattern = r'/connect.*?usermac=.*'
    connect_list = re.findall(connect_pattern, log_str_lines)
    print(' connect 总连接申请数量：' + str(len(connect_list)))
    connect_mac = []
    for line in connect_list:
        try:
            connect_mac.append(re.findall(r'usermac=(.+?)\|', line)[0])
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

def IndexCount(logs):
    log_str_lines = logs
    index_pattern = r'portal/index.*usermac.*'
    index_list = re.findall(index_pattern,log_str_lines)
    index_access_num = len(index_list)
    # print("index 连接数 :"+str(index_access_num))

    index_mac = []
    for line in index_list:
        # print(line)
        try:
            index_mac.append(re.findall(r'usermac=(.+?)\|',line)[0])
        except IndexError:
            pass

    index_mac = list(set(index_mac))
    # print(index_mac)
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
    connect_pattern = r'portal/connect vs.*usermac.*'
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

    auth_suc_pattern = r'doOnline.*call api success(?:.*\n)+?.*WifiPortalController\.connect.*online auth suc'
    auth_suc_list = re.findall(auth_suc_pattern,log_str_lines)
    print("conncet access num : "+str(len(connect_list))+"connect access mac :"+str(len(connect_mac))+"认证成功数："+str(len(auth_suc_list)))

    # auth_suc_mac = []
    # for line in auth_suc_list:
    #     try:
    #         auth_suc_mac.append(re.findall(MAC_PATTERN,line)[0])
    #     except IndexError:
    #         pass
    # auth_suc_mac = list(set(auth_suc_mac))
    # print("auth suc mac :"+ str(len(auth_suc_mac)))

    # sms auth suc
    sms_auth_suc_pattern = r'WifiPortal.*toWaitForPage params,mode:sms,mac:.*'
    sms_auth_list = re.findall(sms_auth_suc_pattern,log_str_lines)
    # print("sms auth num :"+str(len(sms_auth_list)))
    sms_auth_mac = []
    for line in sms_auth_list:
        # print(line)
        try:
            sms_auth_mac.append(re.findall(r'mac:(.*)\,',line)[0])
        except IndexError:
            pass
    sms_auth_mac = list(set(sms_auth_mac))
    # print(sms_auth_mac)
    # print("connect auth mac:"+str(len(sms_auth_mac)))

    # sms auth fail
    sms_auth_fail_pattern = r'WifiPortal.*connect.*online auth fail'
    sms_fail_list = re.findall(sms_auth_fail_pattern,log_str_lines)
    print("sms 认证失败数 :"+ str(len(sms_fail_list)))

    return connect_mac

def wxOnline(logs):
    log_str_lines =logs
    wxOnline_pattern = r'Access log.*portal/wxOnline.*usermac.*'
    wxOnline_list = re.findall(wxOnline_pattern,log_str_lines)
    # print("Portal/wxOnline Access num :"+str(len(wxOnline_list)))

    wxOnline_mac = []
    for line in wxOnline_list:
        try:
            wxOnline_mac.append(re.findall(r'usermac=(.+?)\|',line)[0])
        except IndexError:
            pass
    wxOnline_mac = list(set(wxOnline_mac))
    # print(wxOnline_mac)
    print("Portal/wxOnline access user :"+str(len(wxOnline_mac)))
    return wxOnline_mac

    openId = []
    for line in wxOnline_list:
        try:
            openId.append(re.findall(r'openId=(.{32})',line)[0])
        except IndexError:
            pass
    openId = list(set(openId))
    # print("Portal/wxOnline access openId :"+str(len(openId)))

def timeOutOnline(logs):
    log_str_lines = logs
    timeOutOnline_pattern = r'Access log.*portal/timeOutOnline.*'
    timeOutOnline_list = re.findall(timeOutOnline_pattern,log_str_lines)
    # print("timeOutOnline access num :"+str(len(timeOutOnline_list)))

    timeOutOnline_mac = []
    for line in timeOutOnline_list:
        try:
            timeOutOnline_mac.append(re.findall(r'usermac=(.+?)\|',line)[0])
        except IndexError:
            pass
    timeOutOnline_mac = list(set(timeOutOnline_mac))
    print("timeOutOnline mac :"+str(len(timeOutOnline_mac)))
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
    getFreeCreditMobile_pattern = r'Access log.*/portal/index(?:.*\n)+?.*getFreeCreditMobile.*'
    getFreeCreditMobile_list = re.findall(getFreeCreditMobile_pattern,log_str_lines)
    # print("getFree Credit num :"+ str(len(getFreeCreditMobile_list)))

    getFreeCreditMobile_mac = []
    for line in getFreeCreditMobile_list:
        # print(line)
        try:
            # if 'A4-3D-78-4B-54-7C' in line:
            #     print(line)
            # getFreeCreditMobile_mac.append((re.findall(r'usermac=(.+?)(&|\|)',line)[0])[0])
            getFreeCreditMobile_mac.append(re.findall(r'usermac=(.+?)\|',line)[0])
        except IndexError:
            pass

    getFreeCreditMobile_mac = list(set(getFreeCreditMobile_mac))

    # print("get free credit mac :"+str(len(getFreeCreditMobile_mac)))
    # print(getFreeCreditMobile_mac)
    return getFreeCreditMobile_mac


if __name__ == "__main__":
    portal_log_file1 = r'G:\wifi_portal_log\project.log.2016-09-19-01.txt'
    portal_log_file2 = r'G:\wifi_portal_log\project.log.2016-09-19.txt'
    portal_log_file3 = r'G:\wifi_portal_log\project.log.2016-09-19-02.txt'
    try:
        f1 = open(portal_log_file1,'r',encoding='utf-8')
        log_str_lines1 = f1.read()
    except:
        log_str_lines1 = ''
    try:
        f2 = open(portal_log_file2,'r',encoding='utf-8')
        log_str_lines2 = f2.read()
    except:
        log_str_lines2 = ''
    try:
        f3 = open(portal_log_file3,'r',encoding='utf-8')
        log_str_lines3 = f3.read()
    except:
        log_str_lines3=''

    # log_str_lines1 = f1.read()
    # log_str_lines2 = f2.read()
    # with open(portal_log_file1, 'r', encoding='utf-8') as f:
    #     log_str_lines1 = f.read()
    # with open(portal_log_file2, 'r', encoding='utf-8') as f2:
    #     log_str_lines2 = f.read()
    log_str_lines = log_str_lines1+log_str_lines2+log_str_lines3
    # log_str_lines = log_str_lines2
    f1.close()
    f2.close()
    f3.close()

    index_mac = IndexCount(log_str_lines)
    getFreeCreditMobile_mac = getFreeCreditMobile(log_str_lines)
    connect_mac = ConnectCount(log_str_lines)
    wxOnline_mac = wxOnline(log_str_lines)
    timeOutOnline_mac = timeOutOnline(log_str_lines)
    jumpWxWifi_mac = jumpWxWifi(log_str_lines)
    toUserRedirectUrl(log_str_lines)

    realOutmac = list(set(index_mac)-set(getFreeCreditMobile_mac+jumpWxWifi_mac+wxOnline_mac+connect_mac+timeOutOnline_mac))
    print("无法上网用户数："+str(len(realOutmac)))

    all_mac = list(set(index_mac+connect_mac+wxOnline_mac+timeOutOnline_mac+jumpWxWifi_mac+getFreeCreditMobile_mac))
    # print(len(all_mac))
    count = 0
    for mac in all_mac:
        if len(mac)<=17:
            count = count +1
            # print(count,mac)
    print("all access mac :"+str(count))

