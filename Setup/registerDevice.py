import socket
import subprocess
import os
import requests

#----------------------------------------------------------------------
def checkConnection():
  hostname = socket.gethostname()
  cmd = "hostname -I | awk '{print $1}' -"
  IP = subprocess.check_output(cmd, shell = True )
  ip = IP.decode('utf-8', 'ignore')

  cmd = "iwgetid wlan0 --raw"
  WIFI = subprocess.check_output(cmd, shell = True )
  wifi = WIFI.decode('utf-8', 'ignore')
  wifi = wifi.strip()
  ip   = ip.strip()

  return(wifi,ip,hostname)

#----------------------------------------------------------------------

url = 'https://data.orcsgirls.org/devices.php'
key = 'ORCS2023'
(wifi,ip,hostname)=checkConnection();
mydata = [('Hostname', hostname),('IPAddress', ip),('WiFiName', wifi),('Key', key)]

response=requests.post(url, data=mydata)
