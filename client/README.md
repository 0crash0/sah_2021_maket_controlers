#client configuring:

1 set client raspberry wifi

EDIT files from this repo: etc/wpa_supplicant/wpa_supplicant.conf:
ssid=YOUR_SSID
wpa_passphrase=YOUR_PASSWORD

sudo cp etc/wpa_supplicant/wpa_supplicant.conf /etc/wpa_supplicant
sudo reboot


2 setup for python service:
sudo apt-get install python3-dev python3-rpi.gpio python3-pip git
sudo pip3 install wiringpi
sudo pip3 install requests
sudo pip3 install git+https://github.com/amperka/TroykaCapPython


cp user_folder/cli.py /home/pi/cli.py
sudo cp cli.service /systemd/system

sudo chmod 644 /etc/systemd/system/cli.service
sudo chmod 744 /home/pi/cli.py

sudo systemctl daemon-reload
sudo systemctl enable cli.service
sudo systemctl start cli.service