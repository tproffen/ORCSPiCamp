#!/usr/bin/env python3

import ST7735
from PIL import Image, ImageDraw, ImageFont
from fonts.ttf import RobotoMedium as UserFont
import socket
from subprocess import check_output
import datetime
import os

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def get_ssid():
    ssid="Not found"
    scanoutput = check_output(["iwlist", "wlan0", "scan"])
    for line in scanoutput.split():
        if line.startswith(b'ESSID'):
            ssid = line.split(b'"')[1].decode("utf-8") 
    return ssid

disp = ST7735.ST7735(
    port=0,
    cs=1,
    dc=9,
    backlight=12,
    rotation=270,
    spi_speed_hz=10000000
)

# Initialize display.
disp.begin()

# Width and height to calculate text position.
WIDTH = disp.width
HEIGHT = disp.height

# New canvas to draw on.
img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))
draw = ImageDraw.Draw(img)
# New canvas to draw on.
back_colour = (0, 60, 20)

dirname = os.path.dirname(__file__)
background = os.path.join(dirname, 'background.png')
img = Image.open(background)
draw = ImageDraw.Draw(img)

# Output text
header="ORCSPiCamp 2021"
myip="IP: "+get_ip_address()
myssid="SSID: "+get_ssid()

# Text settings
font_size = 14
font = ImageFont.truetype(UserFont, font_size)
text_colour = (255, 255, 255)
size_x, size_y = draw.textsize(myip, font)
margin = 5

# Draw background rectangle and write text.
back_colour = (0, 60, 20)
draw.rectangle((0, 0, 160, size_y+2*margin), back_colour)
draw.text((margin, margin), header, font=font, fill=text_colour)
draw.text((margin, margin+2.5*size_y), myip, font=font, fill=text_colour)
draw.text((margin, margin+3.75*size_y), myssid[:17], font=font, fill=text_colour)

disp.display(img)

