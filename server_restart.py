#coding:utf-8
import sys
import MailClient
import time
import os
import threading

reload(sys)
sys.setdefaultencoding('utf8')

working_dic = "/home/chenyue/nodejs/wanba_v1.0/dreamserver/game-server"
key = "wanba_v1"

def restart():
    cmd = "ps  -ef | grep node | grep " + key;
    output = os.popen(cmd)
    temp = output.read().split('\n');
    for line in temp:
        if len(line.split(' ')) < 2:
            continue
        pid = line.split(' ')[2];
        print "killing pid", pid
        kill_cmd = "kill -9 " + pid
        output = os.popen(kill_cmd);
        print output.read();

    cmd = "pomelo start -D --directory " + working_dic

    output = os.popen(cmd);
    print output.read();




if __name__ == '__main__':


    #timer = threading.Timer(5, process_check)
    #timer.start()
    restart();
