#!/usr/bin/env php
<?php

$ledP =      array(7,    1,    0,    2,    4,    3,    5,    6,    26,   23,   24,   27,   25,   28,   29)
$ledPstate = array(False,False,False,False,False,False,False,False,False,False,False,False,False,False,False)


$wiringpi = new WiringPi();
$wiringpi->setmode(WiringPi::WPI_MODE_PHYS);
$wiringpi->setup( $pin, WiringPi::OUTPUT);

for ( $n = 0; $n < count($ledP) ; $n ++ ) {
		$wiringpi->output( $ledP );
	}



function rpiSetp(int $pin, bool $value ){
    ledPstate[$pin-1]=$value 
    wp.digitalWrite($ledP[$pin-1], $value==true ? WiringPi::HIGH : WiringPi::LOW)
    #condition ? value_when_true : value_when_false
}

function rpiSetAll(bool $value){
    for ( $n = 0; $n < count($ledP) ; $n ++ ) {
		rpiSetp($n+1, $value==true ? WiringPi::HIGH : WiringPi::LOW)
		print ($ledPstate[$n])
	}
}	

             
        elif self.path=='/1on':
            rpiSetp(1,True)
            ports200(self)
        elif self.path=='/1off':
            rpiSetp(1,False)
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


class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass
    


print("Starting server at port %d" % port)

raspberrypi_init()

while True:
    server_thread(port)



























 <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
                 .button7 {
  font-weight: 700;
  color: white;
  text-decoration: none;
  padding: .8em 1em calc(.8em + 3px);
  border-radius: 3px;
  background: rgb(64,199,129);
  box-shadow: 0 -3px rgb(53,167,110) inset;
  transition: 0.2s;
} 
.button7:hover { background: rgb(53, 167, 110); }
.button7:active {
  background: rgb(33,147,90);
  box-shadow: 0 3px rgb(33,147,90) inset;
}

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
              <script type="text/javascript" src="jquery-3.6.0.min.js"></script>
              <script type="text/javascript" charset="utf-8">
              $(document).ready(function(){   
              //xmlGET();
              setInterval(func, 5000);
              });
             
              var func =      function xmlGET(){
                $.ajax({
                    url: '/getparams',
                    type: 'GET',  
                    //data: { action: 'get_weather' }, 
                    success: function (data, status, xhr) { 
                        //var data1 = JSON.parse(xhr.response);
                        //alert(xhr.responseText);
                    
              
               '''
        for i in range(15):
            html=html+'''$('#myonoffswitch'''+str(i+1)+'''').prop('checked', data['''+str(i)+'''].led'''+str(i+1)+''');
            '''
        html=html+'''
                    }
                });
                    
              
                    
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

        for i in range(15):
            html = html+'''
                 <p><button class="button7" onclick="ledOn('''+str(i+1)+''');">'''+str(i+1)+''' ON</button><button class="button7" onclick="ledOff('''+str(i+1)+''');">'''+str(i+1)+''' OFF</button></p>
'''
        html = html+'''         <span id="textstatus">Status: Ready</span>
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