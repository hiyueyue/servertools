
#coding:utf-8
import sys
import os
import time

#srcPath = '/usr/local/mongodb/data/'
dstPath = '/data/chenyue/temp/'


def dataBackup(dst):
    cmd = 'mkdir ' + dst;
    output = os.popen(cmd)
    #temp = output.read();
    #print temp
    cmd = "/usr/local/mongodb/bin/mongodump -d dreamtown_wanba -o " + dst ;
    print cmd
    output = os.popen(cmd)
    #temp = output.read();
    #print temp
    cmd = "/usr/local/mongodb/bin/mongodump -d counters -o " + dst ;
    print cmd
    output = os.popen(cmd)




if __name__ == '__main__':
    date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    print date
    dst = dstPath + date
    dataBackup(dst)
