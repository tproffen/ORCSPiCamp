#!/usr/bin/python

# Raspberry Pi LM75A I2C temperature sample code.

import smbus

# By default the address of LM75A is set to 0x48
address = 0x48

# Read I2C data and calculate temperature
bus = smbus.SMBus(1)
raw = bus.read_word_data(address, 0) & 0xFFFF
raw = ((raw << 8) & 0xFF00) + (raw >> 8)
temperature = (raw / 32.0) / 8.0

# Print temperature
out= 'Temperature: {0:0.2f} *C'.format(temperature)
print(out)
