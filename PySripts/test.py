#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

from bs4 import BeautifulSoup
import re
import requests

url_params = {"username":"admin","password":"888888","type":"1"}
url = "http://admin.xxyxc.demo.shangquanquan.com/dologin.aj"
# path = r"C:\Users\jiaohui\Desktop\scpg\urls.txt"
# urls1 = GetUrls(url,url_params,path)
# urls1.__write_urls()
# d2 = datetime.datetime.now()
# time = d2 -urls1.startData
# print(time)
url_welcome = "http://admin.xxyxc.demo.shangquanquan.com/t/welcome.j"

html_login = requests.post(url,url_params)
html_welcome = requests.get(url_welcome)


# with open(html_welcome.content, 'r', encoding='utf-8') as f:
#     soup = BeautifulSoup(f)
soup = BeautifulSoup(html_welcome.content.decode('utf-8'))
for link in soup.find_all('a'):
    print(link.get('href'))



