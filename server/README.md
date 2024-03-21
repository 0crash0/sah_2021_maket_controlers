#server configuring:

1 set server raspberry as wifi AP
sudo apt install dnsmasq hostapd


apt install -y netfilter-persistent iptables-persistent

sudo systemctl stop dnsmasq
sudo systemctl stop hostapd



EDIT files from this repo: etc/hostapd.conf and etc/wpa_supplicant/wpa_supplicant.conf:
ssid=YOUR_SSID
wpa_passphrase=YOUR_PASSWORD



sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig
sudo cp etc/dnsmasq.conf /etc
sudo cp etc/dhcpcd.conf /etc
sudo cp etc/sysctl.d/routed-ap.conf /etc
sudo cp etc/hostapd/hostapd.conf /etc
sudo cp etc/wpa_supplicant/wpa_supplicant.conf /etc/wpa_supplicant

sudo rfkill unblock wlan
sudo systemctl unmask hostapd
sudo systemctl enable hostapd
sudo service dhcpcd restart
sudo systemctl start dnsmasq
sudo systemctl reboot


2 setup LCD

git clone https://github.com/waveshare/LCD-show.git
cd LCD-show
chmod +x LCD35-HDMI-480x320-show
sudo ./LCD35-HDMI-480x320-show 180

3 setup for python server:

sudo apt-get install omxplayer python3-dev python3-rpi.gpio python3-pip git
sudo pip3 install wiringpi
sudo pip3 install git+https://github.com/amperka/TroykaCapPython




cp user_folder/* /home/pi
sudo cp *.service /systemd/system

chmod +x /home/pi/serv1.py

chmod 664 /etc/systemd/system/video.service
chmod 664 /etc/systemd/system/pyserv.service

sudo systemctl daemon-reload
sudo systemctl enable video.service
sudo systemctl enable pyserv.service

sudo systemctl start video.service
sudo systemctl start pyserv.service


