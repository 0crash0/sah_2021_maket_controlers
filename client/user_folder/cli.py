#!/usr/bin/python3  
import http.client
from urllib import request
import time
import wiringpi as wp
import json
from array import array
from _thread import *
import threading
import requests
from urllib.error import HTTPError

btnP =      array('i', [7,    1,    0,    2,    4,    3,    5,    6,    26,   23,   24,   27,   25,   28,   29])
btnlststt = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
btnlststt = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def threaded(sendstr):
    #connection.request('GET', sendstr)
    #response = connection.getresponse()
    try:
        response = requests.get('http://192.168.1.1:8000'+sendstr)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        pass
    

def raspberrypi_init():
    try:
        wp.wiringPiSetup()
        for i in range(15):
            wp.pinMode(btnP[i], wp.INPUT)
            wp.pullUpDnControl(btnP[i],wp.PUD_UP)
    except:
        pass

def chkServWthMe():
    try:
        response = requests.get('http://192.168.1.1:8000/getparams')
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        pass
        
    params=json.loads(response.content)
    for i in range(14):
        #print(i,btnlststt[i], int(params[i]['led'+str(i+1)]))
        if ((btnlststt[i] != int(params[i]['led'+str(i+1)])) and btnlststt[14] != 1):
            getpg='on'if btnlststt[i] else 'off'
            sendstr='/' +str(i+1)+getpg
            start_new_thread(threaded, (sendstr,))
            cntr_recv=1

#connection = http.client.HTTPConnection("192.168.1.1:8000", timeout=20)

raspberrypi_init()
cntr_recv=0
while (True):
    sendstr=''
    for i in range(15):
        readed=wp.digitalRead(btnP[i])
        if (btnlststt[i] != readed):
            getpg='on'if readed else 'off'
            
            #request.urlopen('http://192.168.1.1:8000/'+ str(i+1) +getpg).read()
            if(i==14):
                sendstr='/all' +getpg
                #connection.request('GET', '/all' +getpg)
                #print('/all' +getpg)
            else:
                sendstr='/' +str(i+1)+getpg
                #connection.request('GET', '/' + str(i+1) +getpg)
                #print('/' + str(i+1) +getpg)
            start_new_thread(threaded, (sendstr,))
            cntr_recv=1
            #response = connection.getresponse()
            #print(wp.digitalRead(btnP[i]),(btnP[i]),i)
            btnlststt[i]=wp.digitalRead(btnP[i])
            ###print('on'if readed else 'off' )
            ###print(readed)
    if(cntr_recv==0):
        #connection.request('GET', '/getparams')
        #response = connection.getresponse()
        #r = requests.get('http://192.168.1.1:8000/getparams')
        chkServWthMe()
        #print(response.read().decode())
    time.sleep(0.25)
#    print("-----------------------------------------------------")
    cntr_recv=cntr_recv+1
    if(cntr_recv==10):
        cntr_recv=0
    
