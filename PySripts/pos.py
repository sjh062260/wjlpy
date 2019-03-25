# _*_ coding:utf-8 _*_
# ! /usr/bin/env python
__author__ = 'Administrator'

import re


def logRead(filepath):
    try:
        with open(filepath,'r',encoding = 'utf-8') as f:
        # f = open(filepath,'r',encoding = 'utf-8')
            log_str = f.readlines()
        return log_str
    except:
        log_str = []
        return log_str

def loginFail(loglines):
    loglines = loglines
    # fail_pattern = re.compile(r'/third/queryStoreBymCode.*en=.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*设备未注册')
    # fail_list = re.findall(r'/third/queryStoreBymCode.*en=(.+?)\n.*设备未注册',loglines)
    # print(fail_list)
    queryPattern = r'/third/queryStoreBymCode.*en=.*'
    i = 0
    fail_str = r'设备未注册'
    loglength = len(loglines)
    en_list = []
    for i in range(loglength):
        try:
            while(re.search(queryPattern,loglines[i])):
                fail_line = loglines[i+8]
                if fail_str in fail_line:
                    # print(loglines[i])
                    en_list.append((re.findall(r'en=(.+?)\|',loglines[i]))[0])
                i = i +9
        except IndexError:
            pass
    return list(set(en_list))

            # print(fail_line)
if __name__ == "__main__":
    filepath1 = r'C:\Users\jiaohui\Desktop\1111\POS\project.log.2016-11-04.txt'
    filepath2 = r'C:\Users\jiaohui\Desktop\1111\POS\project.log.2016-11-04_02.txt'
    filepath3 = r'C:\Users\jiaohui\Desktop\1111\POS\project.log.2016-11-05.txt'
    filepath4 = r'C:\Users\jiaohui\Desktop\1111\POS\project.log.2016-11-05_02.txt'
    filepath5 = r'C:\Users\jiaohui\Desktop\1111\POS\project.log.2016-11-06.txt'
    filepath6 = r'C:\Users\jiaohui\Desktop\1111\POS\project.log.2016-11-06_02.txt'
    filepath7 = r'C:\Users\jiaohui\Desktop\1111\POS\project.log.2016-11-07.txt'
    filepath8 = r'C:\Users\jiaohui\Desktop\1111\POS\project.log.2016-11-07_02.txt'
    filepath9 = r'C:\Users\jiaohui\Desktop\1111\POS\project.log.2016-11-08.txt'
    filepath10 = r'C:\Users\jiaohui\Desktop\1111\POS\project.log.2016-11-08_02.txt'
    logstr1 = logRead(filepath1)
    en1 = loginFail(logstr1)
    logstr2 = logRead(filepath2)
    en2 = loginFail(logstr2)
    logstr3 = logRead(filepath3)
    en3 = loginFail(logstr3)
    logstr4 = logRead(filepath4)
    en4 = loginFail(logstr4)
    logstr5 = logRead(filepath5)
    en5 = loginFail(logstr5)
    logstr6 = logRead(filepath6)
    en6 = loginFail(logstr6)
    logstr7 = logRead(filepath7)
    en7 = loginFail(logstr7)
    logstr7 = logRead(filepath7)
    en7 = loginFail(logstr7)
    logstr8 = logRead(filepath8)
    en8 = loginFail(logstr8)
    logstr9 = logRead(filepath9)
    en9 = loginFail(logstr9)
    logstr10 = logRead(filepath10)
    en10 = loginFail(logstr10)
    pos = en1+en2+en3+en4+en5+en6+en7+en8+en9+en10
    print(list(set(pos)))
