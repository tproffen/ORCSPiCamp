from board import *
import busio
from adafruit_seesaw import seesaw, pwmout
import time

myI2C = busio.I2C(SCL, SDA)

ss = seesaw.Seesaw(myI2C)
pwm = pwmout.PWMOut(ss,5)

while True:
  pwm.duty_cycle=0x80
  time.sleep(1)
  pwm.duty_cycle=0x00
  time.sleep(1)
