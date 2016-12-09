#!/usr/bin/python
import re
import os
import glob
import sys
import datetime
import subprocess,shlex
now = datetime.datetime.now();
log_dir = "/home/example.com/logs"
log_match = 'access_log-'+ now.strftime("%Y-%m-%d")+'-[0-9]' 

def scanLog(dir, regex):
    # group(1) = ip, group(2) =date , group(3) = post/head/get group(4) = url group(5) code
    logregex = '([(\d\.)]+) - - \[(.*?)\] "(POST|HEAD|GET) (.*[^manager\/index]\.php.*?) HTTP.*?" ([2]\d+)'
    for file in os.listdir(dir):
        if re.match(regex,file):
            for i, line in enumerate(open(dir+'/'+file)):
                match = re.match(logregex,line)
                if match:
                    print(match.group(5)+' '+ match.group(4))
                        
def scanbase64(dir):   
    hostsa = subprocess.check_output("egrep --color=always --include=*.php -Rn 'b\w*a\w*s\w*e\w*6\w*4\w*_\w*d\w*e.*c.*o.*d.*e.*\"' " + dir + " | cut -c -1000", shell=True)
    print hostsa
    hostsb = subprocess.check_output("egrep -Rn --color=always --include=.*php '\\\\x65\\\\x76\\\\x61\\\\x6C' "+ dir + " | cut -c -1000", shell=True)
    print hostsb
    hostsc = subprocess.check_output("egrep -Rn --color=always --include=.*php '\\\\x62\\\\x61\\\\x73\\\\x65\\\\x36\\\\x34\\\\x5F\\\\x64\\\\x65\\\\x63\\\\x6F\\\\x64\\\\x65' "+ dir + " | cut -c -1000", shell=True)
    print hostsc


#scanLog(log_dir,log_match)

scanbase64(sys.argv[1])

