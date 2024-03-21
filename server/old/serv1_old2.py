#!/usr/bin/python3
try:
    import RPi.GPIO as GPIO
    import wiringpi as wp
    import json
    import os
    from array import array
    from time import sleep
    from http.server import BaseHTTPRequestHandler, HTTPServer
except ModuleNotFoundError:
    pass


port = 8000
server_address = ('', port)

ledP =      array('i', [7,    1,    0,    2,    4,    3,    5,    6,    26,   23,   24,   27,   25,   28,   29])
ledPstate = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]

def raspberrypi_init():
    try:
        wp.wiringPiSetup()
        for i in range(15):
            wp.pinMode(ledP[i], wp.OUTPUT)
    except:
        pass

def rpiSetp(pin: int, value: bool):
    ledPstate[pin-1]=value 
    try:
        wp.digitalWrite(ledP[pin-1], wp.HIGH if value else wp.LOW)
        #value_when_true if condition else value_when_false
    except:
        pass

def rpiSetAll(value: bool):
    for i in range(15):
        rpiSetp(i+1, value)
    for i in range(15):
        print (ledPstate[i])

def rasperrypi_cleanup():
    try:
        GPIO.cleanup()
    except:
        pass


            
def server_thread(port):
    httpd = HTTPServer(server_address, MyServer)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        exit
    httpd.server_close()


def ports200(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"OK")

class MyServer(BaseHTTPRequestHandler):

    def do_HEAD(self):

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        """ do_GET() can be tested using curl command
            'curl http://server-ip-address:port'
        """
        html = '''
              <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
                 .button_led {display: inline-block; background-color: #e7bd3b; border: none; border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}


.onoffswitch {
    position: relative; width: 110px;
    -webkit-user-select:none; -moz-user-select:none; -ms-user-select: none;
}
.onoffswitch-checkbox {
    position: absolute;
    opacity: 0;
    pointer-events: none;
}
.onoffswitch-label {
    display: block; overflow: hidden; cursor: pointer;
    height: 36px; padding: 0; line-height: 36px;
    border: 2px solid #E3E3E3; border-radius: 36px;
    background-color: #FFFFFF;
    transition: background-color 0.3s ease-in;
}
.onoffswitch-label:before {
    content: "";
    display: block; width: 36px; margin: 0px;
    background: #FFFFFF;
    position: absolute; top: 0; bottom: 0;
    right: 72px;
    border: 2px solid #E3E3E3; border-radius: 36px;
    transition: all 0.3s ease-in 0s; 
}
.onoffswitch-checkbox:checked + .onoffswitch-label {
    background-color: #49E845;
}
.onoffswitch-checkbox:checked + .onoffswitch-label, .onoffswitch-checkbox:checked + .onoffswitch-label:before {
   border-color: #49E845;
}
.onoffswitch-checkbox:checked + .onoffswitch-label:before {
    right: 0px; 
}


              </style>
              <script src="jquery-3.6.0.min.js"></script>
              <script type="text/javascript" charset="utf-8">
              $(document).ready(function(){   
                $.ajax({
                    url: '/getparams', //Адрес страницы или скрипта
                    type: 'GET',  // HTTP метод
                    //data: { action: 'get_weather' },  // Данные для отправки (в данном случае в видео объекта)
                    success: function (data, status, xhr) { //callback на случай успешного выполнения запроса
                        //var data1 = JSON.parse(xhr.response);
                        alert(xhr.responseText); //Показываем результат на странице
                    }
                });});
              //setInterval(xmlGET(), 10000)
                    function xmlGET1(){
                        var xhr = new XMLHttpRequest();
                        xhr.open('GET', 'getparams', false);
                        xhr.send();
                        if (xhr.status != 200) {
                          //alert( xhr.status + ': ' + xhr.statusText ); 
                        } else {
                          //alert( xhr.responseText ); 
                          var data = JSON.parse(xhr.response);'''
        for i in range(15):
            html=html+'''document.getElementById("myonoffswitch'''+str(i+1)+'''").checked = data['''+str(i)+'''].led'''+str(i+1)+''';'''
        html=html+'''   }
                    }
                    function httpPostAsync(method, params, callback) {
                        var xmlHttp = new XMLHttpRequest();
                        xmlHttp.onreadystatechange = function() { 
                            if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
                                callback(xmlHttp.responseText);
                            else
                                callback(`Error ${xmlHttp.status}`)
                        }
                        xmlHttp.open("POST", window.location.href + method, true);
                        xmlHttp.setRequestHeader("Content-Type", "application/json");
                        xmlHttp.send(params);
                    }

                    function ledOn(num) {
                        document.getElementById("textstatus").textContent = "Making LED on...";
                        httpPostAsync("led", JSON.stringify({"led":num, "on": true }), function(resp) { 
                            document.getElementById("textstatus").textContent = `Led ON: ${resp}`;
                        });
                    }

                    function ledOff(num) {
                        document.getElementById("textstatus").textContent = "Making LED off...";
                        httpPostAsync("led", JSON.stringify({"led":num, "on": false }), function(resp) { 
                            document.getElementById("textstatus").textContent = `Led OFF: ${resp}`;
                        });
                    }                            
              </script>
              <body onload1="xmlGET();">
                 <h2>Hello from the Raspberry Pi!</h2>
                 
'''
        for i in range(15):
            html = html+ '''<div class="onoffswitch">
                <input type="checkbox" name="onoffswitch'''+str(i+1)+'''" class="onoffswitch-checkbox" id="myonoffswitch'''+str(i+1)+'''" tabindex="0"  onclick="if(!this.checked){ledOff('''+str(i+1)+''');}else{ledOn('''+str(i+1)+''');}">
                <label class="onoffswitch-label" for="myonoffswitch'''+str(i+1)+'''">
                    <span class="onoffswitch-inner">led'''+str(i+1)+'''</span>
                    <span class="onoffswitch-switch">led'''+str(i+1)+'''</span>
                </label></div>'''

        html = html+'''
                 <p><button class="button button_led" onclick="ledOn(1);">1 ON</button><button class="button button_led" onclick="ledOff(1);">1 OFF</button></p>
                 <p><button class="button button_led" onclick="ledOn(2);">2 ON</button><button class="button button_led" onclick="ledOff(2);">2 OFF</button></p>
                 <p><button class="button button_led" onclick="ledOn(3);">3 ON</button><button class="button button_led" onclick="ledOff(3);">3 OFF</button></p>
                 <p><button class="button button_led" onclick="ledOn(4);">4 ON</button><button class="button button_led" onclick="ledOff(4);">4 OFF</button></p>
                 <p><button class="button button_led" onclick="ledOn(5);">5 ON</button><button class="button button_led" onclick="ledOff(5);">5 OFF</button></p>
                 <p><button class="button button_led" onclick="ledOn(6);">6 ON</button><button class="button button_led" onclick="ledOff(6);">6 OFF</button></p>
                 <p><button class="button button_led" onclick="ledOn(7);">7 ON</button><button class="button button_led" onclick="ledOff(7);">7 OFF</button></p>
                 <p><button class="button button_led" onclick="ledOn(8);">8 ON</button><button class="button button_led" onclick="ledOff(8);">8 OFF</button></p>
                 <p><button class="button button_led" onclick="ledOn(9);">9 ON</button><button class="button button_led" onclick="ledOff(9);">9 OFF</button></p>
                 <p><button class="button button_led" onclick="ledOn(10);">10 ON</button><button class="button button_led" onclick="ledOff(10);">10 OFF</button></p>
                 <p><button class="button button_led" onclick="ledOn(11);">11 ON</button><button class="button button_led" onclick="ledOff(11);">11 OFF</button></p>
                 <p><button class="button button_led" onclick="ledOn(12);">12 ON</button><button class="button button_led" onclick="ledOff(12);">12 OFF</button></p>
                 <p><button class="button button_led" onclick="ledOn(13);">13 ON</button><button class="button button_led" onclick="ledOff(13);">13 OFF</button></p>
                 <p><button class="button button_led" onclick="ledOn(14);">14 ON</button><button class="button button_led" onclick="ledOff(14);">14 OFF</button></p>
                 <p><button class="button button_led" onclick="ledOn(15);">15 ON</button><button class="button button_led" onclick="ledOff(15);">15 OFF</button></p>
                 <span id="textstatus">Status: Ready</span>
                 <br><br><br>
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

              </body>
           </html>
        '''
        print("GET request, path:", self.path)
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))
        elif self.path.endswith(".jpg"):
            self.send_response(200)
            self.send_header('Content-type', 'image/jpg')
            self.end_headers()
            with open(os.curdir + os.sep + 'img' + os.sep + self.path, 'rb') as file:
                self.wfile.write(file.read())
        elif self.path.endswith(".js"):
            self.send_response(200)
            self.send_header('Content-type', 'application/javascript')
            self.end_headers()
            with open(os.curdir + os.sep + 'js' + os.sep + self.path, 'rb') as file:
                self.wfile.write(file.read())  

        elif self.path=='/1on':
            rpiSetp(1,True)
            ports200(self)
        elif self.path=='/1off':
            rpiSetp(1,False)
            ports200(self)

        elif self.path=='/2on':
            rpiSetp(2,True)
            ports200(self)
        elif self.path=='/2off':
            rpiSetp(2,False)
            ports200(self)
            
        elif self.path=='/3on':
            rpiSetp(3,True)
            ports200(self)
        elif self.path=='/3off':
            rpiSetp(3,False)
            ports200(self)

        elif self.path=='/4on':
            rpiSetp(4,True)
            ports200(self)
        elif self.path=='/4off':
            rpiSetp(4,False)
            ports200(self)
 
        elif self.path=='/5on':
            rpiSetp(5,True)
            ports200(self)
        elif self.path=='/5off':
            rpiSetp(5,False)
            ports200(self)
 
        elif self.path=='/6on':
            rpiSetp(6,True)
            ports200(self)
        elif self.path=='/6off':
            rpiSetp(6,False)
            ports200(self)
 
        elif self.path=='/7on':
            rpiSetp(7,True)
            ports200(self)
        elif self.path=='/7off':
            rpiSetp(7,False)
            ports200(self)
 
        elif self.path=='/8on':
            rpiSetp(8,True)
            ports200(self)
        elif self.path=='/8off':
            rpiSetp(8,False)
            ports200(self)
 
        elif self.path=='/9on':
            rpiSetp(9,True)
            ports200(self)
        elif self.path=='/9off':
            rpiSetp(9,False)
            ports200(self)

        elif self.path=='/10on':
            rpiSetp(10,True)
            ports200(self)
        elif self.path=='/10off':
            rpiSetp(10,False)
            ports200(self)
 
        elif self.path=='/11on':
            rpiSetp(11,True)
            ports200(self)
        elif self.path=='/11off':
            rpiSetp(11,False)
            ports200(self)

        elif self.path=='/12on':
            rpiSetp(12,True)
            ports200(self)
        elif self.path=='/12off':
            rpiSetp(12,False)
            ports200(self)
 
        elif self.path=='/13on':
            rpiSetp(13,True)
        elif self.path=='/13off':
            rpiSetp(13,False)
            ports200(self)
 
        elif self.path=='/14on':
            rpiSetp(14,True)
            ports200(self)
        elif self.path=='/14off':
            rpiSetp(14,False)
            ports200(self)

        elif self.path=='/15on':
            rpiSetp(15,True)
            ports200(self)
        elif self.path=='/15off':
            rpiSetp(15,False)
            ports200(self)
        elif self.path=='/allon':
            rpiSetAll(True)
            ports200(self)
        elif self.path=='/alloff':
            rpiSetAll(False)
            ports200(self)
        elif self.path=='/getparams':
            params =[]
            for i in range(15):
                params.append({'led'+str(i+1):ledPstate[i]})
            html=json.dumps(params)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))
        else:
            self.send_error(404, "Page Not Found {}".format(self.path))
    
    
        
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        try:
            print("POST request, path:", self.path, "body:", body.decode('utf-8'))
            if self.path == "/led":
                data_dict = json.loads(body.decode('utf-8'))
                if 'on' in data_dict:
                    print(data_dict['led'], data_dict['on'])
                    rpiSetp(data_dict['led'], data_dict['on'])

                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b"OK")
            if self.path == "/getparams":
                params =[]
                for i in range(15):
                    params.append({'led':i+1,'state':ledPstate[i]})
                html=json.dumps(params)
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(html)
            else:
                self.send_response(400, 'Bad Request: Method does not exist')
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
        except Exception as err:
            print("do_POST exception: %s" % str(err))

print("Starting server at port %d" % port)

raspberrypi_init()

while True:
    server_thread(port)

rasperrypi_cleanup()