# _*_ coding:utf-8 _*_
# ! /usr/bin/env python
__author__ = 'Administrator'
from prettytable import PrettyTable
import re
def logRead(filepath):
    try:
        with open(filepath,'r',encoding = 'utf-8') as f:
            log_str = f.read()
        return log_str
    except:
        log_str = ''
        return log_str

# def ngSplit(tenant):
#     for line in ng_str:
#         s = line.split("```")
#         tenant_host = s[3]
#         tenant_code = tenant_host.split(".")[1]
#         access_url = s[4]
#         action = access_url.split("/")[-1].replace('"','')
#         user_mac = s[-2].replace('"','')
#         # print(tenant_code,action,user_mac)

def listToMac(lists):
    mac = []
    mac_pattern = re.compile(r'"```"(.?)"```"$')
    for line in lists:
        try:
            mac.append(re.findall(mac_pattern,line)[0])
            # print(mac)
        except IndexError:
            pass
    return mac
    print(mac)


def ngActions(tenant):
    index_pattern = re.compile(r'wifi\.'+tenant+r'\.mallshow.net"```"/portal/index".*usermac.*')
    connect_pattern = re.compile(r'wifi\.'+tenant+r'\.mallshow.net"```"/portal/connect".*usermac.*')
    timeOutOnline_pattern = re.compile(r'wifi\.'+tenant+r'\.mallshow.net"```"/portal/timeOutOnline".*usermac.*')
    wxOnlline_pattern = re.compile(r'wifi\.'+tenant+r'\.mallshow.net"```"/portal/wxOnline".*usermac.*')
    index_list = re.findall(index_pattern,ng_str)
    index_pv = len(index_list)
    index_mac = listToMac(index_list)
    index_uv = len(list(set(index_mac)))

    connect_list = re.findall(connect_pattern,ng_str)
    connect_pv = len(connect_list)
    connect_mac = listToMac(connect_list)
    connect_uv = len(list(set(connect_mac)))

    timeOutOnline_list = re.findall(timeOutOnline_pattern,ng_str)
    timeOutOnline_pv = len(timeOutOnline_list)
    timeOutOnline_mac = listToMac(timeOutOnline_list)
    timeOutOnline_uv = len(list(set(timeOutOnline_mac)))

    wxOnline_list = re.findall(wxOnlline_pattern,ng_str)
    wxOnline_pv = len(wxOnline_list)
    wxOnlline_mac = listToMac(wxOnline_list)
    wxOnline_uv = len(list(set(wxOnlline_mac)))

    return {"index_pv":index_pv,"index_uv":index_uv,"connect_pv":connect_pv,"connect_uv":connect_uv,"timeOutOnline_pv":timeOutOnline_pv,
            "timeOutOnline_uv":timeOutOnline_uv,"wxOnline_pv":wxOnline_pv,"wxOnline_uv":wxOnline_uv}



if __name__ == "__main__":
    tenant_dict = {"cdfyh":"10112","ngjn":"10110","bdcsgc":"10106","nhcs":"10105","nghx":"10109","wsq":"10103","xhcsgc":"10107","sydyc":"10113","nthqgc":"10115","nhdh":"10108","ycjf":"10114"}
    # tenants = ["cdfyh","ngjn","ycjf"]
    # actions = ["index","connect","timeOutOnline","wxOnline"]
    wifi_ng_file = r'C:\Users\jiaohui\Desktop\wifi-access_20161113.log'
    ng_str = logRead(wifi_ng_file)
    x = PrettyTable(["广场ID","首页PV","首页UV","短信认证PV","短信认证UV","超时认证PV","超时认证UV","微信认证PV","微信认证UV"])
    x.align["广场ID"] = "l"
    x.padding_width = 1
    for tenant in tenant_dict.keys():
        s = ngActions(tenant)
        x.add_row([tenant,s["index_pv"],s["index_uv"],s["connect_pv"],s["connect_uv"],s["timeOutOnline_pv"],s["timeOutOnline_uv"],s["wxOnline_pv"],s["wxOnline_uv"]])
    print(x)




