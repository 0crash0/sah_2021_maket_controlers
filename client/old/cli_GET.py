import http.client
import time
import wiringpi as wp
import json
from array import array

btnP =      array('i', [7,    1,    0,    2,    4,    3,    5,    6,    26,   23,   24,   27,   25,   28,   29])
btnlststt = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

        
def raspberrypi_init():
    try:
        wp.wiringPiSetup()
        for i in range(15):
            wp.pinMode(btnP[i], wp.INPUT)
            wp.pullUpDnControl(btnP[i],wp.PUD_UP)
    except:
        pass


connection = http.client.HTTPConnection("192.168.1.1:8000", timeout=20)
connection.request('GET', '/allon')
response = connection.getresponse()
time.sleep(2)
connection.request('GET', '/alloff')
response = connection.getresponse()




raspberrypi_init()
while (True):
    for i in range(15):
        readed=wp.digitalRead(btnP[i])
        if (btnlststt[i] != readed):
            getpg='on'if readed else 'off'
            connection.request('GET', '/' + str(i+1) +getpg)
            response = connection.getresponse()
            print(wp.digitalRead(btnP[i]),(btnP[i]),i)
            btnlststt[i]=wp.digitalRead(btnP[i])
            print('on'if readed else 'off')

    time.sleep(1)
    print("-----------------------------------------------------")
    
