#!/usr/bin/python

import RPi.GPIO as GPIO
import wiringpi as wp
import os
from time import sleep
from http.server import BaseHTTPRequestHandler, HTTPServer

host_name = '192.168.1.73'  # Change this to your Raspberry Pi IP address
host_port = 8000

class MyServer(BaseHTTPRequestHandler):
    """ A special implementation of BaseHTTPRequestHander for reading data from
        and control GPIO of a Raspberry Pi
    """

    def do_HEAD(self):
        """ do_HEAD() can be tested use curl command
            'curl -I http://server-ip-address:port'
        """
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        """ do_GET() can be tested using curl command
            'curl http://server-ip-address:port'
        """
        html = '''
           <html>
           <body style="width:960px; margin: 20px auto;">
           <h1>Welcome to my Raspberry Pi</h1>
           <p>Current GPU temperature is {}</p>
           <p>Turn all: <a href="/allon">On</a> <a href="/alloff">Off</a></p>
           
           <p>Turn all: <a href="/1on">On</a> <a href="/1off">Off</a></p>
           <p>Turn all: <a href="/2on">On</a> <a href="/2off">Off</a></p>
           <p>Turn all: <a href="/3on">On</a> <a href="/3off">Off</a></p>
           <p>Turn all: <a href="/4on">On</a> <a href="/4off">Off</a></p>
           <p>Turn all: <a href="/5on">On</a> <a href="/5off">Off</a></p>
           <p>Turn all: <a href="/6on">On</a> <a href="/6off">Off</a></p>
           <p>Turn all: <a href="/7on">On</a> <a href="/7off">Off</a></p>
           <p>Turn all: <a href="/8on">On</a> <a href="/8off">Off</a></p>
           <p>Turn all: <a href="/9on">On</a> <a href="/9off">Off</a></p>
           <p>Turn all: <a href="/10on">On</a> <a href="/10off">Off</a></p>
           <p>Turn all: <a href="/11on">On</a> <a href="/11off">Off</a></p>
           <p>Turn all: <a href="/12on">On</a> <a href="/12off">Off</a></p>
           <p>Turn all: <a href="/13on">On</a> <a href="/13off">Off</a></p>
           <p>Turn all: <a href="/14on">On</a> <a href="/14off">Off</a></p>
           <p>Turn all: <a href="/15on">On</a> <a href="/15off">Off</a></p>
           
           <div id="led-status"></div>
           <script>
               document.getElementById("led-status").innerHTML="{}";
           </script>
           </body>
           </html>
        '''
        temp = os.popen("/opt/vc/bin/vcgencmd measure_temp").read()
        self.do_HEAD()
        status = ''
        if self.path=='/':
            status='/'

        elif self.path=='/1on':
            wp.digitalWrite(7, wp.HIGH)
            status='on'
        elif self.path=='/1off':
            wp.digitalWrite(7, wp.LOW)
            status='off'

        elif self.path=='/2on':
            wp.digitalWrite(1, wp.HIGH)
            status='on'
        elif self.path=='/2off':
            wp.digitalWrite(1, wp.LOW)
            status='off'
 

        elif self.path=='/3on':
            wp.digitalWrite(0, wp.HIGH)
            status='on'
        elif self.path=='/3off':
            wp.digitalWrite(0, wp.LOW)
            status='off'

        elif self.path=='/4on':
            wp.digitalWrite(2, wp.HIGH)
            status='on'
        elif self.path=='/4off':
            wp.digitalWrite(2, wp.LOW)
            status='off'
 
        elif self.path=='/5on':
            wp.digitalWrite(4, wp.HIGH)
            status='on'
        elif self.path=='/5off':
            wp.digitalWrite(4, wp.LOW)
            status='off'
 
        elif self.path=='/6on':
            wp.digitalWrite(3, wp.HIGH)
            status='on'
        elif self.path=='/6off':
            wp.digitalWrite(3, wp.LOW)
            status='off'
 
        elif self.path=='/7on':
            wp.digitalWrite(5, wp.HIGH)
            status='on'
        elif self.path=='/7off':
            wp.digitalWrite(5, wp.LOW)
            status='off'
 
        elif self.path=='/8on':
            wp.digitalWrite(6, wp.HIGH)
            status='on'
        elif self.path=='/8off':
            wp.digitalWrite(6, wp.LOW)
            status='off'
 
        elif self.path=='/9on':
            wp.digitalWrite(26, wp.HIGH)
            status='on'
        elif self.path=='/9off':
            wp.digitalWrite(26, wp.LOW)
            status='off'

        elif self.path=='/10on':
            wp.digitalWrite(23, wp.HIGH)
            status='on'
        elif self.path=='/10off':
            wp.digitalWrite(23, wp.LOW)
            status='off'
 

        elif self.path=='/11on':
            wp.digitalWrite(24, wp.HIGH)
            status='on'
        elif self.path=='/11off':
            wp.digitalWrite(24, wp.LOW)
            status='off'

        elif self.path=='/12on':
            wp.digitalWrite(27, wp.HIGH)
            status='on'
        elif self.path=='/12off':
            wp.digitalWrite(27, wp.LOW)
            status='off'
 
        elif self.path=='/13on':
            wp.digitalWrite(25, wp.HIGH)
            status='on'
        elif self.path=='/13off':
            wp.digitalWrite(25, wp.LOW)
            status='off'
 
        elif self.path=='/14on':
            wp.digitalWrite(28, wp.HIGH)
            status='on'
        elif self.path=='/14off':
            wp.digitalWrite(28, wp.LOW)
            status='off'

        elif self.path=='/15on':
            wp.digitalWrite(29, wp.HIGH)
            status='on'
        elif self.path=='/15off':
            wp.digitalWrite(29, wp.LOW)
            status='off'


  
        elif self.path=='/allon':
            wp.digitalWrite(7, wp.HIGH)
            wp.digitalWrite(1, wp.HIGH)
            wp.digitalWrite(0, wp.HIGH)
            wp.digitalWrite(2, wp.HIGH)
            wp.digitalWrite(4, wp.HIGH)
            wp.digitalWrite(3, wp.HIGH)
            wp.digitalWrite(5, wp.HIGH)
            wp.digitalWrite(6, wp.HIGH)

            wp.digitalWrite(26, wp.HIGH)
            wp.digitalWrite(23, wp.HIGH)
            wp.digitalWrite(24, wp.HIGH)
            wp.digitalWrite(27, wp.HIGH)
            wp.digitalWrite(25, wp.HIGH)
            wp.digitalWrite(28, wp.HIGH)
            wp.digitalWrite(29, wp.HIGH)
            status='allon'
        elif self.path=='/alloff':
            wp.digitalWrite(7, wp.LOW)
            wp.digitalWrite(1, wp.LOW)
            wp.digitalWrite(0, wp.LOW)
            wp.digitalWrite(2, wp.LOW)
            wp.digitalWrite(4, wp.LOW)
            wp.digitalWrite(3, wp.LOW)
            wp.digitalWrite(5, wp.LOW)
            wp.digitalWrite(6, wp.LOW)

            wp.digitalWrite(26, wp.LOW)
            wp.digitalWrite(23, wp.LOW)
            wp.digitalWrite(24, wp.LOW)
            wp.digitalWrite(27, wp.LOW)
            wp.digitalWrite(25, wp.LOW)
            wp.digitalWrite(28, wp.LOW)
            wp.digitalWrite(29, wp.LOW)
            status='alloff'
 
 
        self.wfile.write(html.format(temp[5:], status).encode("utf-8"))

def maain():
    wp.wiringPiSetup()
    wp.pinMode(7, wp.OUTPUT)
    wp.pinMode(1, wp.OUTPUT)
    wp.pinMode(0, wp.OUTPUT)
    wp.pinMode(2, wp.OUTPUT)
    wp.pinMode(4, wp.OUTPUT)
    wp.pinMode(3, wp.OUTPUT)
    wp.pinMode(5, wp.OUTPUT)
    wp.pinMode(6, wp.OUTPUT)

    wp.pinMode(26, wp.OUTPUT)
    wp.pinMode(23, wp.OUTPUT)
    wp.pinMode(24, wp.OUTPUT)
    wp.pinMode(27, wp.OUTPUT)
    wp.pinMode(25, wp.OUTPUT)
    wp.pinMode(28, wp.OUTPUT)
    wp.pinMode(29, wp.OUTPUT)

    http_server = HTTPServer((host_name, host_port), MyServer)
    print("Server Starts - %s:%s" % (host_name, host_port))

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()

while True:
    maain()
