
#coding:utf-8
import sys
import os
import time

srcPath = '/usr/local/mongodb/data/'
dstPath = '/data/chenyue/temp/'


def copyData(src, dst):
    cmd = 'mkdir ' + dst;
    output = os.popen(cmd)
    #temp = output.read();
    #print temp
    cmd = "cp -r " + srcPath + 'dreamtown_wanba.0 ' + dst ;
    print cmd
    output = os.popen(cmd)
    #temp = output.read();
    #print temp
    cmd = "cp -r " + srcPath + 'dreamtown_wanba.ns ' + dst ;
    print cmd
    output = os.popen(cmd)

    cmd = "cp -r " + srcPath + 'counters.0 ' + dst ;
    print cmd
    output = os.popen(cmd)

    cmd = "cp -r " + srcPath + 'counters.ns ' + dst ;
    print cmd
    output = os.popen(cmd)




if __name__ == '__main__':
    date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    print date
    dst = dstPath + date
    copyData(srcPath,dst)
