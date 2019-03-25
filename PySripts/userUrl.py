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

    # try:
    #     with open(filepath,'r',encoding='utf-8') as f:
    #         log_str = f.read()
    #     return log_str
    # except FileNotFoundError:
    #     pass

def userUrl(filepath):
    log_str_lines = filepath
    portal_index_pattern = r'portal/index.*generate_204"```"200"```"0.[5-9].*'
    portal_index_list = re.findall(portal_index_pattern,log_str_lines)
    print(portal_index_list)
    url_dict = dict()
    userurl_pattern = r'userurl=(.+?)\&'
    for line in portal_index_list:
        # print(line)
        try:
            url = re.findall(userurl_pattern,line)[0]
            # print(url)
            if url in url_dict.keys():
                url_dict[url] = url_dict[url]+1
            else:
                url_dict[url] = 1
        except IndexError:
            pass
    # url_dict = sorted(url_dict.iteritems(), key=lambda d:d[1], reverse = True)
    # print(url_dict)
    return  url_dict

def dict_sorted(dict):
    d = dict
    d = sorted(d.items(), key=lambda  d:d[1])
    return d

if __name__ == "__main__":

    portal_log_file1 = r'C:\Users\jiaohui\Desktop\wifi-access_2016101102.log'
    portal_log_file2 = r'C:\Users\jiaohui\Desktop\wifi-access_20161011.log'
    # portal_log_file3 = r'G:\wifi_portal_log\project.log.2016-09-22-02.txt'
    with open(portal_log_file1, 'r', encoding='utf-8') as f:
        log_str_lines1 = f.read()
    with open(portal_log_file2, 'r', encoding='utf-8') as f:
        log_str_lines2 = f.read()

    log_str_lines = log_str_lines1+log_str_lines2
    # print(len(log_str_lines))
    log_str_lines1=log_str_lines2=''
    # print(type(log_str_lines))
    userdict = userUrl(log_str_lines)
    d = dict_sorted(userdict)
    print(d)

