#coding:utf-8
import sys
import MailClient
import time
import os
import threading

reload(sys)
sys.setdefaultencoding('utf8')
mailto_list = ['569116141@qq.com', 'ethanwang@lichisoft.com'];


def checkProcessExist(port):
    cmd = "netstat -nltp | grep " + str(port);
    output = os.popen(cmd)
    temp = output.read();
    print temp
    if len(temp) == 0:
        print "none...."
        title = "dreamserver warning"
        content = "game server process is not exist." + str(port)
        MailClient.send_mail(mailto_list,title,content)
        



def checkDiskUse():
    cmd = "df -h";
    output = os.popen(cmd)
    res = output.read().split('\n');
    for line in res: 
        print line 
        
        arr = line.split(' ')
        #print 'arr',arr
        if arr[0] == '/dev/vda1' or arr[0] == '/dev/vdb':
            percent = arr[len(arr) - 2][:len(arr[4]) - 1]
            print "percent",percent
            if int(percent) > 80:
                title = "dreamserver warning"
                content = "dist use warning. disk:" + arr[0] + " use:" + arr[len(arr) - 2];
                MailClient.send_mail(mailto_list,title,content)
                #sendmail


def process_check():
    checkProcessExist(3000);
    checkDiskUse();


if __name__ == '__main__':


    #timer = threading.Timer(5, process_check)
    #timer.start()
    process_check();

    '''
    time_str = time.strftime('%Y%m%d')
    file_name = "../statlog." + time_str
    process_log(file_name)
    GenerateWarningList()
    title = "DataWarning"
    print "============"
    print content 
    print "send",g_is_send
    if g_is_send == 1:
        MailClient.send_mail(StatisticsConf.mailto_list,title,content)
        result_file = "warning." + time_str
        file_object = open(result_file,'w')
        file_object.write(content)
        file_object.close()
        '''
