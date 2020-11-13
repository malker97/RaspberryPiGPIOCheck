#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import datetime

def save_to_file(file_name, contents):
    fh = open(file_name,'a')
    fh.write(contents+""+"\n")
    fh.close()
    
def hmstime(seconds):
    a=str(seconds//3600)
    b=str((seconds%3600)//60)
    c=str((seconds%3600)%60)
    d=["{} hours {} mins {} seconds".format(a, b, c)]
    return d

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)
pre_status = True
startTime = time.time()
endTime = time.time()
status1 = GPIO.input(4)
status2 = GPIO.input(4)
# print GPIO.input(4)
totalTime = 0

while pre_status:
#    if GPIO.input(4):
    str_day_time = str(datetime.date.today())
    str_file_name = './logs/txt/'+str_day_time+'-log.txt'
    status1 = status2
    status2 = GPIO.input(4)
    if status1 != status2:
        if(status2):
            startTime = time.time()
            arr_data = ['S',str(datetime.datetime.now())]
            print arr_data
            save_to_file(str_file_name,'S,'+str(datetime.datetime.now()))
            #print ('S, '+str(datetime.datetime.now()))
        else:
            endTime = time.time()
            save_to_file(str_file_name,'E,'+str(datetime.datetime.now()))
            arr_data = ['E',str(datetime.datetime.now())]
            print arr_data
            #print ('E,'+str(datetime.datetime.now()))
            totalTime = totalTime + (endTime-startTime)
            arr_data = ['T',str(hmstime(totalTime))]
            print arr_data
            save_to_file(str_file_name,'T,'+str(hmstime(totalTime)))
            #print ('T,'+str(hmstime(totalTime)))
#    if totalTime:
#        print totalTime
    time.sleep(0.001)

