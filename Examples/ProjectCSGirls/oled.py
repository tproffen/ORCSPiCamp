# You need to install the driover using 
#   sudo pip3 install adafruit-circuitpython-ssd1306

import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# Define the Reset Pin
oled_reset = digitalio.DigitalInOut(board.D4)

WIDTH = 128
HEIGHT = 32 

# Use for I2C.
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)

# Clear display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (oled.width, oled.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Load default font.

# Draw Some Text
text = "ProjectCSGirls"
font = ImageFont.truetype("arial.ttf", 7)
(font_width, font_height) = font.getsize(text)
draw.text( (oled.width // 2 - font_width // 2, 0), text, font=font, fill=255,)

text = "Katie & Kristen"
font = ImageFont.truetype("arial.ttf", 12)
(font_width, font_height) = font.getsize(text)
draw.text( (oled.width // 2 - font_width // 2, 10), text, font=font, fill=255,)

# Display image
oled.image(image)
oled.show()

