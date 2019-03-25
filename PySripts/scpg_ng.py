# _*_ coding:utf-8 _*_
# ! /usr/bin/env python
__author__ = 'Administrator'

import re
def logRead(filepath):
    try:
        with open(filepath,'r',encoding = 'utf-8') as f:
            log_str = f.read()
        return log_str
    except:
        log_str = ''
        return log_str

def userUrl(filepath):
    log_str_lines = filepath
    url_pattern = r'wx.xayxc.scpretail.net"```"/.*'
    url_list = re.findall(url_pattern,log_str_lines)
    # for line in url_list:
    #     print(line)
    url_dict = dict()
    for line in url_list:
        user_url = line.split("```")[1]
        # print(user_url)
        if user_url in url_dict.keys():
            url_dict[user_url] = url_dict[user_url] +1
        else:
            url_dict[user_url] = 1
    # print(url_dict)
    return url_dict

        # print(user_url)


    # userurl_pattern = r'userurl=(.+?)\&'
    # for line in portal_index_list:
    #     # print(line)
    #     try:
    #         url = re.findall(userurl_pattern,line)[0]
    #         # print(url)
    #         if url in url_dict.keys():
    #             url_dict[url] = url_dict[url]+1
    #         else:
    #             url_dict[url] = 1
    #     except IndexError:
    #         pass
    # url_dict = sorted(url_dict.iteritems(), key=lambda d:d[1], reverse = True)
    # print(url_dict)
    return  url_dict

def dict_sorted(dict):
    d = dict
    d = sorted(d.items(), key=lambda  d:d[1])
    return d

if __name__ == "__main__":

    portal_log_file1 = r'C:\Users\jiaohui\Desktop\wx-yxc-access_20161220.log'
    portal_log_file2 = r'C:\Users\jiaohui\Desktop\wx-yxc-access_20161220-2.log'
    # portal_log_file3 = r'G:\wifi_portal_log\project.log.2016-09-22-02.txt'
    with open(portal_log_file1, 'r', encoding='utf-8') as f:
        log_str_lines1 = f.read()
    with open(portal_log_file2, 'r', encoding='utf-8') as f:
        log_str_lines2 = f.read()
    log_str_lines = log_str_lines1+log_str_lines2
    url_dict = userUrl(log_str_lines)
    dict_sorted(url_dict)
    for item in url_dict:
        print(item+ " "+str(url_dict[item]))

