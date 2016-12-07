#!/usr/bin/python2.6
import re
import os
import glob
import datetime
now = datetime.datetime.now();
log_dir = "/home/example.com/logs"
log_match = 'access_log-'+ now.strftime("%Y-%m-%d")+'-[0-9]' 
#regex = '([(\d\.)]+) - - \[(.*?)\] "(GET.*?\/.*)" ([2][0-9[0-9]+) - "(.*?)" "(.*?)"'
# group(1) = ip, group(2) =date , group(3) = post/head/get group(4) = url group(5) code

def scanLog(dir, regex):
    logregex = '([(\d\.)]+) - - \[(.*?)\] "(POST|HEAD|GET) (.*[^manager\/index]\.php.*?) HTTP.*?" ([2]\d+)'
        for file in os.listdir(dir)e
            if re.match(regex,file):
                for i, line in enumerate(open(dir+'/'+file)):
                    match = re.match(logregex,line)
                    if match:
                        print(match.group(5)+' '+ match.group(4))

scanLog(log_dir,log_match)

