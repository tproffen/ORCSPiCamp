#!/usr/bin/env python3
#----------------------------------------------------------------------
import ST7735
from PIL import Image, ImageDraw, ImageFont
from fonts.ttf import RobotoMedium as UserFont
import subprocess
import time
import os
import re

disp = ST7735.ST7735(port=0,cs=1,dc=9,backlight=12,rotation=270,
                     spi_speed_hz=10000000)

#----------------------------------------------------------------------
# Settings
#----------------------------------------------------------------------

back_colour = (0, 60, 20)
text_colour = (255, 255, 255)
head_colour = (255, 255,   0)
warn_colour = (255,  50,  50)
font_size   = 14
logo_img    = 'background.png'
m           = 5

#----------------------------------------------------------------------
def checkConnection():
  cmd = "hostname -I | awk '{print $1}' -"
  IP = subprocess.check_output(cmd, shell = True )
  ip = IP.decode('utf-8', 'ignore')

  cmd = "nmcli conn show | sed '1d' | awk '{print $1}' -"
  WIFI = subprocess.check_output(cmd, shell = True )
  wifi = WIFI.decode('utf-8', 'ignore')

  return(wifi,ip)
#----------------------------------------------------------------------
disp.begin()

# Width and height to calculate text position.

w = disp.width
h = disp.height

# Setup and loading background

dirname = os.path.dirname(__file__)
background = os.path.join(dirname, logo_img)
logo = Image.open(background)

# Create new image, set color and paste logo

img = Image.new('RGBA', (w, h))
draw = ImageDraw.Draw(img)

# Text settings

font = ImageFont.truetype(UserFont, font_size)
size_x, size_y = draw.textsize('text', font)

#----------------------------------------------------------------------
# Welcome screen
#----------------------------------------------------------------------
draw.rectangle((0, 0, w, h), back_colour)
img.paste(logo,(0,0), mask=logo)
draw.text((m, m), "ORCSPICamp 2021", font=font, fill=head_colour)
draw.text((m, m+4.0*size_y), 'Not connected', font=font, fill=warn_colour)
disp.display(img)

#----------------------------------------------------------------------
# Waiting for WiFi connection
#----------------------------------------------------------------------

(wifi, ip) = checkConnection()
while not (re.search('[a-zA-Z]', wifi) and re.search('[0-9]',ip)):
  time.sleep(0.5)
  (wifi, ip) = checkConnection()

draw.rectangle((0, 0, w, h), back_colour)
img.paste(logo,(0,0), mask=logo)
draw.text((m, m), "ORCSPICamp 2021", font=font, fill=head_colour)
draw.text((m, m+2.5*size_y), "WIFI: "+wifi[:17], font=font, fill=text_colour)
draw.text((m, m+4.0*size_y), "IP: "+ip, font=font, fill=text_colour)
disp.display(img)


