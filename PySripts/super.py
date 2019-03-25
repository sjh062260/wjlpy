#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

# Created on 2016年7月16日
# @author: jiaohui

# 按行读取文件
def logReadLines(filepath):
    with open(filepath,'r',encoding='utf-8') as f:
        log_str = f.readlines()
    return log_str

# 将相同pid 的日志联接到一起
def splitLog(loglines):  
    pids = []
    # pid_log = []
    pid_log = {}
    i = 0
    for i in range(len(loglines)):
        j = 1
        for j in range(20):
            line = loglines[i+j]
            # print(line)
            s = line.split(' ',maxsplit = 5)
            # print(s)
            try:
                pid = s[4]
                # print(pid)
                pid_str = s[5]
            except IndexError:
                pass
            if pid in pids:
                pid_log[pid].join(' '+pid_str)
            else:
                pids.append(pid)
                pid_log[pid] = pid_str
            print(len(pid_log))
            j = j+1
        i = i+j
        # print(i,j)

    return pid_log

def IndexCount(tenant):
    tenant = tenant
    index_pattern = r'Access log.*/index.*usermac.*\n.*'+tenant+r'-wifi'
    index_list = re.findall(index_pattern,log_str_lines)
    index_access_num = len(index_list)

    index_mac = []
    for line in index_list:
        try:
            index_mac.append(re.findall(r'usermac=(.+?)\|',line)[0])
        except IndexError:
            pass

    index_mac = list(set(index_mac))
    index_access_user = len(index_mac)
    print(tenant+" index 连接数 :"+str(index_access_num)+' '+tenant+" index access 用户数 :"+str(index_access_user))
    return_dict = {"tenant":tenant,"url":"index","access_num":len(index_list),"access_user":len(index_mac)}
    return return_dict


if __name__ == "__main__":
    portal_log_file2 = r'G:\wifi_portal_log\project.log.2016-09-26.txt'
    log = logReadLines(portal_log_file2)
    log_dic = splitLog(log)
    print(log_dic)
            


