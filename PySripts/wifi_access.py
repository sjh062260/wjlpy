# ! /usr/bin/env python
# _*_ coding:utf-8 _*_
import re,datetime
import mysql.connector

class wifiNgAnalysis(object):
    def __init__(self):
        self.request_dict = {}
        self.total_request_times = 0
        # self.date = datetime.datetime.strptime("2016-08-09","%Y-%m-%d")
        # self.split_dict = {"request_date":self.date}
        # self.conn = mysql.connector.connect(user='root',password = 'shi1987122',database = '')

    def split_eachLine_toDict(self,line):
        # 将单行日志拆分
        split_line = line.split("```")
        split_dict = {"remote_ip":split_line[1].strip('"'),"method":split_line[2].strip('"'),"host":split_line[3].strip('"'),"request_menu":split_line[4].strip('"'),\
                      "params":split_line[5].strip('"'),"http_code":split_line[6].strip('"'),"pro_time":split_line[7].strip('"'),"source_url":split_line[8].strip('"'),\
                      "user_agent":split_line[10].strip('"'),"server_pro_time":split_line[15].strip('"'),}
        split_dict["request_date"]="2016-08-09"
        # 获取ip和usermac
        if split_dict["params"] == "-":
            if split_dict["source_url"]=="-":
                split_dict["request_ip"]=""
                split_dict["user_mac"]=""
            elif re.findall(r'cdfyh',split_dict["source_url"]):
                split_dict["request_ip"]=re.findall(r'userip=(.+?)&',split_dict["source_url"])[0]
                split_dict["user_mac"]=re.findall(r'usermac=(.{12})',split_dict["source_url"])[0]
            else:
                split_dict["request_ip"]=re.findall(r'userip=(.+?)&',split_dict["source_url"])[0]
                split_dict["user_mac"]=re.findall(r'usermac=(.+?)&',split_dict["source_url"])[0]
        if split_dict["params"] !="-":
            split_dict["request_ip"]=re.findall(r'userip=(.+?)&',split_dict["params"])[0]
            split_dict["user_mac"]=re.findall(r'usermac=(.+?)&',split_dict["params"])[0]
        # 获取请求日期
        timeline = split_line[0]

        return split_dict

    def insert_to_mysql(self,lineDict):
        conn = mysql.connector.connect(user='root',password = 'shi1987122',database = 'mntor')
        cursor = conn.cursor()
        sql = "INSERT INTO cloudportal_wifiaccess VALUES (%s,%s,%s,%s,%s,%s,%s,%f,%f,%s)"
        paras = (lineDict["request_menu"],lineDict["request_date"],lineDict["remote_ip"],lineDict["host"],lineDict["source_url"],lineDict["request_ip"],lineDict["user_mac"], float(lineDict["pro_time"]),float(lineDict["server_pro_time"]),lineDict["user_agent"])
        cursor.execute(sql,paras)
        conn.commit()
        cursor.close()
        conn.close()
    # def string_to_time(self,line):
    #     line = line.split(" ")[0]
    #     time_dict = {"data":line.split(":")[0],"hour":line.split(":")[0],"min":line.split(":")[0],"sec":line.split(":")[0]}
    #     time = datetime.datetime.strptime(line,"%d/%m/%Y:%H:%M:%S")
    def generate_log_report(self,object):
        logfile = object
        with open(logfile, 'r', encoding='utf-8') as f:
            i = 0
            for line in f:
                try:
                    line_dict = self.split_eachLine_toDict(line)
                except ValueError:
                    continue
                except IndexError:
                    continue
                self.insert_to_mysql(line_dict)
                # print(line_dict["request_ip"]+"   "+line_dict["user_mac"])
                # print(line_dict["request_time"])


if __name__ == '__main__':
    logfile = r'G:\ng-wifi_access\wifi-access_20160809.log'
    # wifiNgAnalysis.generate_log_report(r'C:\Users\jiaohui\Desktop\portal.midware-access_20160809.log')
    main_object = wifiNgAnalysis()
    main_object.generate_log_report(logfile)






