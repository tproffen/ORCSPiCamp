import socket
import os
import requests

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
ssid=os.popen("sudo iwgetid -r").read()

url = 'https://data.orcsgirls.org/devices.php'
key = 'ORCS2023'
mydata = [('Hostname', host_name),('IPAddress', host_ip),('WiFiName', ssid),('Key', key)]
response=requests.post(url, data=mydata)
