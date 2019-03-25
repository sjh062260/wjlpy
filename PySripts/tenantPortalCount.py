# _*_ coding:utf-8 _*_
# ! /usr/bin/env python
__author__ = 'Administrator'

import re
from prettytable import PrettyTable

def index(tenant):
    index_pattern = re.compile(r'Access log.*portal/index.*usermac.*\n.*'+tenant+r'-wifi')
    index_list = re.findall(index_pattern,log_str)
    index_mac = []
    mac_pattern = re.compile(r'usermac=(.+?)\|')
    for line in index_list:
        try:
            index_mac.append(re.findall(mac_pattern,line)[0])
        except IndexError:
            pass
    index_mac = list(set(index_mac))
    index = {"index request macs":len(index_mac)}
    return index
    del index_list


def message(tenant):
    message_pattern = re.compile(r'Access log.*portal/connect.*usermac.*\n.*'+tenant+r'-wifi')
    message_list = re.findall(message_pattern,log_str)
    message_mac = []
    mac_pattern = re.compile(r'usermac=(.+?)\|')
    for line in message_list:
        try:
            message_mac.append(re.findall(mac_pattern,line)[0])
        except IndexError:
            pass
    message_mac = list(set(message_mac))
    message= {"message request macs":len(message_mac)}
    return message
    del message_list



def smsSuc(tenant):
    sms_suc_pattern = re.compile(r'portal/connect.*?usermac.*\n.*'+tenant+r'-wifi(?:.*\n)+?.*call api suc.*\n.*WifiCon.*?online auth suc')
    sms_suc_list = re.findall(sms_suc_pattern,log_str)
    sms_suc_num = len(sms_suc_list)
    sms_suc_mac = []
    mac_pattern = re.compile(r'usermac=(.+?)\|')
    for line in sms_suc_list:
        try:
            sms_suc_mac.append(re.findall(mac_pattern,line)[0])
        except IndexError:
            pass
    sms_suc_mac = list(set(sms_suc_mac))
    sms_suc_user = len(sms_suc_mac)
    # print(tenant+"\t短信认证请求成功次数:"+str(sms_suc_num)+"\t短信认证请求成功用户数:"+str(sms_suc_user))
    sms_suc = {"sms_suc_num":sms_suc_num,"sms_suc_user":sms_suc_user}
    return sms_suc
    del sms_suc_list
    del sms_suc_mac

def smsFail(tenant):
    sms_fail_pattern = re.compile(
        r'portal/connect.*?usermac.*\n.*'+tenant+r'-wifi(?:.*\n)+?.*call api fail.*\n.*WifiCon.*?online auth fail')
    sms_fail_list = re.findall(sms_fail_pattern,log_str)
    sms_fail_num = len(sms_fail_list)
    sms_fail_mac = []
    mac_pattern = re.compile(r'usermac=(.+?)\|')
    for line in sms_fail_list:
        try:
            sms_fail_mac.append(re.findall(mac_pattern,line)[0])
        except IndexError:
            pass
    sms_fail_mac = list(set(sms_fail_mac))
    sms_fail_user = len(sms_fail_mac)
    # print(tenant+"\t短信认证请求失败次数:"+str(sms_fail_num)+"\t短信认证请求失败用户数:"+str(sms_fail_user))
    # return sms_fail_num,sms_fail_user
    sms_fail = {"sms_fail_num":sms_fail_num,"sms_fail_user":sms_fail_user}
    return sms_fail
    del sms_fail_list
    del sms_fail_mac

def wxOnline(tenant):
    wxOnline_pattern = re.compile(r'Access log.*portal/wxOnline.*usermac.*\n.*'+tenant+r'-wifi')
    wxOnline_list = re.findall(wxOnline_pattern,log_str)
    wxOnline_mac = []
    mac_pattern = re.compile(r'usermac=(.+?)\|')
    for line in wxOnline_list:
        try:
            wxOnline_mac.append(re.findall(mac_pattern,line)[0])
        except IndexError:
            pass
    wxOnline_mac = list(set(wxOnline_mac))
    wxOnline= {"wxOnline request macs":len(wxOnline_mac)}
    return wxOnline
    del wxOnline


def wxOnlineSuc(tenant):
    wxOnlie_suc_pattern = re.compile(r'Access log.*/portal/wxOnline userip.*openId.*\n.*'+tenant+r'-wifi(?:.*\n)+?.*bindMemberInfo params.*openId.*\n.*code= 200')
    wxOnlie_suc_list = re.findall(wxOnlie_suc_pattern,log_str)
    wxOnline_suc_num = len(wxOnlie_suc_list)
    wxOnline_suc_mac = []
    mac_pattern = re.compile(r'usermac=(.+?)\|')
    for line in wxOnlie_suc_list:
        try:
            wxOnline_suc_mac.append(re.findall(mac_pattern, line)[0])
        except IndexError:
            pass
    wxOnline_suc_mac = list(set(wxOnline_suc_mac))
    wxOnline_suc_user = len(wxOnline_suc_mac)
    # print(tenant+"\t微信认证成功请求次数："+str(wxOnline_suc_num)+"\t微信认证成功用户数："+str(wxOnline_suc_user))
    # return wxOnline_suc_num,wxOnline_suc_user
    wxOnline_suc = {"wxOnline_suc_num":wxOnline_suc_num,"wxOnline_suc_macs":wxOnline_suc_user}
    return wxOnline_suc
    del wxOnlie_suc_list
    del wxOnline_suc_mac

# def wxOnlineFail(tenant):
#     wxOnline_pattern = re.compile(r'Access log.*/portal/wxOnline userip.*openId.*\n.*'+tenant+r'-wifi')
#     wxOnline_list = re.findall(wxOnline_pattern,log_str)
#     # print(wxOnline_list)
#     wx_mac = []
#     mac_pattern = re.compile(r'usermac=(.+?)\|')
#     for line in wxOnline_list:
#         # print(line)
#         try:
#             wx_mac.append(re.findall(mac_pattern, line)[0])
#         except IndexError:
#             pass
#     wx_mac = list(set(wx_mac))
#     print(len(wx_mac))
#     wxOnline_suc_pattern = re.compile(r'Access log.*/portal/wxOnline userip.*openId.*\n.*'+tenant+r'-wifi(?:.*\n)+?.*bindMemberInfo params.*openId.*')
#     wxOnlie_suc_list = re.findall(wxOnline_suc_pattern,log_str)
#     wxOnline_suc_num = len(wxOnlie_suc_list)
#     wxOnline_suc_mac = []
#     for line in wxOnlie_suc_list:
#         try:
#             wxOnline_suc_mac.append(re.findall(mac_pattern, line)[0])
#         except IndexError:
#             pass
#     wxOnline_suc_mac = list(set(wxOnline_suc_mac))
#     wxOnline_suc_user = len(wxOnline_suc_mac)
#     # print(tenant+"    微信认证成功请求次数："+str(wxOnline_suc_num)+"    微信认证成功用户数："+str(wxOnline_suc_user))
#     wx_fail_mac = list(set(wx_mac)-set(wxOnline_suc_mac))
#     print(wx_fail_mac)
#     del wxOnlie_suc_list
#     del wxOnline_suc_mac

def timeOutOnline(tenant):
    timeOutOnline_pattern = re.compile(r'Access log.*portal/timeOutOnline.*usermac.*\n.*'+tenant+r'-wifi')
    timeOutOnline_list = re.findall(timeOutOnline_pattern,log_str)
    timeOutOnline_mac = []
    mac_pattern = re.compile(r'usermac=(.+?)\|')
    for line in timeOutOnline_list:
        try:
            timeOutOnline_mac.append(re.findall(mac_pattern,line)[0])
        except IndexError:
            pass
    timeOutOnline_mac = list(set(timeOutOnline_mac))
    timeOutOnline= {"timeOutOnline macs":len(timeOutOnline_mac)}
    return timeOutOnline
    del timeOutOnline_list


# def directOnline(tenant):
#     direct_suc_pattern = re.compile(r'doOnline.*call api success.*basId='+tenant_dict[tenant]+r'.*\n.*toUserRedirectUrl.*free portal online auth suc')
#     direct_fail_pattern = re.compile(r'doOnline.*call api fail.*basId='+tenant_dict[tenant]+r'.*\n.*toUserRedirectUrl.*free portal online auth fail')

#     direct_suc_list = re.findall(direct_suc_pattern,log_str)
#     direct_suc_num = len(direct_suc_list)
#     mac_pattern = re.compile(r'mac=(.+?)\;')
#     direct_suc_mac = []
#     for line in direct_suc_list:
#         try:
#             direct_suc_mac.append(re.findall(mac_pattern,line)[0])
#         except IndexError:
#             pass
#     direct_suc_mac = list(set(direct_suc_mac))
#     direct_suc_user = len(direct_suc_mac)
#     # print(tenant+"\t免认证成功请求数："+str(direct_suc_num)+"\t免认证成功用户数："+str(len(direct_suc_mac)))
    
#     del direct_suc_list

#     direct_fail_list = re.findall(direct_fail_pattern,log_str)
#     direct_fail_num = len(direct_fail_list)
#     direct_fail_mac = []
#     for line in direct_fail_list:
#         try:
#             direct_fail_mac.append(re.findall(mac_pattern,line)[0])
#         except IndexError:
#             pass
#     direct_fail_mac = list(set(direct_fail_mac))
#     effect_mac = list(set(direct_fail_mac)-set(direct_suc_mac))
#     # print(tenant+"\t免认证失败请求数："+str(direct_fail_num)+"\t免认证失败用户数："+str(len(direct_fail_mac))+"\t免认证影响用户数:"+str(len(effect_mac)))
#     direct_fail_user = len(direct_fail_mac)
#     effect_user = len(effect_mac)
#     # return direct_suc_num,direct_suc_user,direct_fail_num,direct_fail_user,effect_user
#     direct = {"direct_suc_num":direct_suc_num,"direct_suc_user":direct_suc_user,"direct_fail_num":direct_fail_num,"direct_fail_user":direct_fail_user,"effect_user":effect_user}
#     return direct
#     del direct_fail_list

def callApiFail(tenant):
    callApiFail_pattern = re.compile(r'call api fail.*basId='+tenant_dict[tenant]+r'.*')
    callApiFail_list = re.findall(callApiFail_pattern,log_str)
    effect_ip = []
    for line in callApiFail_list:
        try:
            effect_ip.append(re.findall(r'userIp=(.+?)\&',line)[0])
        except IndexError:
            pass
    effect_ip = list(set(effect_ip))
    call_api_fail = {"call api fail num":len(callApiFail_list),"effect ip num":len(effect_ip)}
    return call_api_fail
    del callApiFail_list

def logRead(filepath):
    try:
        with open(filepath,'r',encoding = 'utf-8') as f:
            log_str = f.read()
        return log_str
    except:
        log_str = ''
        return log_str



if __name__ == "__main__":
    # tenant_dict = {"cdfyh":"10112","ngjn":"10110","bdcsgc":"10106","nhcs":"10105","nghx":"10109","wsq":"10103","xhcsgc":"10107","sydyc":"10113","nthqgc":"10115","nhdh":"10108","ycjf":"10114"}
    tenant_dict= {"xhcsgc":"10107"}
    portal_log_file = r'C:\Users\jiaohui\Desktop\project.log'
    log_str = logRead(portal_log_file)
    # x = PrettyTable(["广场ID","短信认证成功PV","短信认证成功UV","短信认证失败PV","短信认证失败UV","微信认证成功PV","微信认证成功UV","免认证成功PV","免认证成功UV","免认证失败PV","免认证失败UV","免认证失败影响UV","认证失败请求数"])
    x = PrettyTable(["广场ID","联网MAC","短信认证MAC","微信认证MAC","超时自动认证MAC","短信认证失败MAC","认证失败请求数","影响IP数"])
    x.align["广场ID"] = "l"
    x.padding_width = 1
    for tenant in tenant_dict.keys():
        print(tenant)
        # sms_suc = smsSuc(tenant)
        # sms_fail = smsFail(tenant)
        # wxOnline_suc = wxOnlineSuc(tenant)
        # direct = directOnline(tenant)
        # call_api_fail = callApiFail(tenant)
        # x.add_row([tenant,sms_suc["sms_suc_num"],sms_suc["sms_suc_user"],sms_fail["sms_fail_num"],sms_fail["sms_fail_user"],
        #           wxOnline_suc["wxOnline_suc_num"],wxOnline_suc["wxOnline_suc_user"],direct["direct_suc_num"],direct["direct_suc_user"],
        #           direct["direct_fail_num"],direct["direct_fail_user"],direct["effect_user"],call_api_fail["call api fail num"]])
        index = index(tenant)
        # print(index)
        message = message(tenant)
        # print(message)
        wx = wxOnline(tenant)
        # print(wx)
        timeOutOnline = timeOutOnline(tenant)
        # print(timeOutOnline)
        smsfail = smsFail(tenant)
        # print(smsfail)
        callapifail = callApiFail(tenant)

        x.add_row([tenant,index["index request macs"],message["message request macs"],wx["wxOnline request macs"],timeOutOnline["timeOutOnline macs"],smsfail["sms_fail_user"],callapifail["call api fail num"],callapifail["effect ip num"]])
    print(x)


