import RPi.GPIO as GPIO
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
            GPIO.output(17, GPIO.HIGH)
            status='on'
        elif self.path=='/1off':
            GPIO.output(17, GPIO.LOW)
            status='off'

        elif self.path=='/2on':
            GPIO.output(27, GPIO.HIGH)
            status='on'
        elif self.path=='/2off':
            GPIO.output(27, GPIO.LOW)
            status='off'
 

        elif self.path=='/3on':
            GPIO.output(22, GPIO.HIGH)
            status='on'
        elif self.path=='/3off':
            GPIO.output(22, GPIO.LOW)
            status='off'

        elif self.path=='/4on':
            GPIO.output(5, GPIO.HIGH)
            status='on'
        elif self.path=='/4off':
            GPIO.output(5, GPIO.LOW)
            status='off'
 
        elif self.path=='/5on':
            GPIO.output(6, GPIO.HIGH)
            status='on'
        elif self.path=='/5off':
            GPIO.output(6, GPIO.LOW)
            status='off'
 
        elif self.path=='/6on':
            GPIO.output(13, GPIO.HIGH)
            status='on'
        elif self.path=='/6off':
            GPIO.output(13, GPIO.LOW)
            status='off'
 
        elif self.path=='/7on':
            GPIO.output(19, GPIO.HIGH)
            status='on'
        elif self.path=='/7off':
            GPIO.output(19, GPIO.LOW)
            status='off'
 
        elif self.path=='/8on':
            GPIO.output(26, GPIO.HIGH)
            status='on'
        elif self.path=='/8off':
            GPIO.output(26, GPIO.LOW)
            status='off'
 
        elif self.path=='/9on':
            GPIO.output(18, GPIO.HIGH)
            status='on'
        elif self.path=='/9off':
            GPIO.output(18, GPIO.LOW)
            status='off'

        elif self.path=='/10on':
            GPIO.output(23, GPIO.HIGH)
            status='on'
        elif self.path=='/10off':
            GPIO.output(23, GPIO.LOW)
            status='off'
 

        elif self.path=='/11on':
            GPIO.output(24, GPIO.HIGH)
            status='on'
        elif self.path=='/11off':
            GPIO.output(24, GPIO.LOW)
            status='off'

        elif self.path=='/12on':
            GPIO.output(25, GPIO.HIGH)
            status='on'
        elif self.path=='/12off':
            GPIO.output(25, GPIO.LOW)
            status='off'
 
        elif self.path=='/13on':
            GPIO.output(12, GPIO.HIGH)
            status='on'
        elif self.path=='/13off':
            GPIO.output(12, GPIO.LOW)
            status='off'
 
        elif self.path=='/14on':
            GPIO.output(16, GPIO.HIGH)
            status='on'
        elif self.path=='/14off':
            GPIO.output(16, GPIO.LOW)
            status='off'

        elif self.path=='/15on':
            GPIO.output(20, GPIO.HIGH)
            status='on'
        elif self.path=='/15off':
            GPIO.output(20, GPIO.LOW)
            status='off'

        elif self.path=='/16on':
            GPIO.output(21, GPIO.HIGH)
            status='on'
        elif self.path=='/16off':
            GPIO.output(21, GPIO.LOW)
            status='off'

  
        elif self.path=='/allon':
            GPIO.output(17, GPIO.HIGH)
            GPIO.output(27, GPIO.HIGH)
            GPIO.output(22, GPIO.HIGH)
            GPIO.output(5, GPIO.HIGH)
            GPIO.output(6, GPIO.HIGH)
            GPIO.output(13, GPIO.HIGH)
            GPIO.output(19, GPIO.HIGH)
            GPIO.output(26, GPIO.HIGH)
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(23, GPIO.HIGH)
            GPIO.output(24, GPIO.HIGH)
            GPIO.output(25, GPIO.HIGH)
            GPIO.output(12, GPIO.HIGH)
            GPIO.output(16, GPIO.HIGH)
            GPIO.output(20, GPIO.HIGH)
            GPIO.output(21, GPIO.HIGH)
            status='allon'
        elif self.path=='/alloff':
            GPIO.output(17, GPIO.LOW)
            GPIO.output(27, GPIO.LOW)
            GPIO.output(22, GPIO.LOW)
            GPIO.output(5, GPIO.LOW)
            GPIO.output(6, GPIO.LOW)
            GPIO.output(13, GPIO.LOW)
            GPIO.output(19, GPIO.LOW)
            GPIO.output(26, GPIO.LOW)
            GPIO.output(18, GPIO.LOW)
            GPIO.output(23, GPIO.LOW)
            GPIO.output(24, GPIO.LOW)
            GPIO.output(25, GPIO.LOW)
            GPIO.output(12, GPIO.LOW)
            GPIO.output(16, GPIO.LOW)
            GPIO.output(20, GPIO.LOW)
            GPIO.output(21, GPIO.LOW)
            status='alloff'
 
 
        self.wfile.write(html.format(temp[5:], status).encode("utf-8"))


if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)

    GPIO.setup(5, GPIO.OUT)
    GPIO.setup(6, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(19, GPIO.OUT)
    GPIO.setup(26, GPIO.OUT)

    GPIO.setup(18, GPIO.OUT)

    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)

    GPIO.setup(25, GPIO.OUT)

    GPIO.setup(12, GPIO.OUT)

    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(20, GPIO.OUT)
    GPIO.setup(21, GPIO.OUT)
    
    GPIO.output(17, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(5, GPIO.LOW)
    GPIO.output(6, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(26, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(25, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(20, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)

    http_server = HTTPServer((host_name, host_port), MyServer)
    print("Server Starts - %s:%s" % (host_name, host_port))

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()
