#!/usr/bin/env python3
#----------------------------------------------------------------------
import ST7735
from PIL import Image, ImageDraw, ImageFont
from fonts.ttf import RobotoMedium as UserFont
import subprocess
import time
import os

disp = ST7735.ST7735(port=0,cs=1,dc=9,backlight=12,rotation=270,
                     spi_speed_hz=10000000)

#----------------------------------------------------------------------
# Settings
#----------------------------------------------------------------------

back_colour = (0, 60, 20)
text_colour = (255, 255, 255)
font_size   = 14
logo_img    = 'background.png'
m           = 5

#----------------------------------------------------------------------
cmd = "hostname -I | cut -d\' \' -f1"
IP = subprocess.check_output(cmd, shell = True )
ip = "IP: "+IP.decode('utf-8', 'ignore')

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

# Draw background rectangle and write text.
draw.text((m, m), "ORCSPICamp 2021", font=font, fill=text_colour)
draw.text((m, m+1.50*size_y), "Welcome :)", font=font, fill=text_colour)
draw.text((m, m+3.75*size_y), ip, font=font, fill=text_colour)

#----------------------------------------------------------------------
disp.display(img)
print ("Welcome display finished.")


