#!/usr/bin/python

# Raspberry Pi LM75A I2C temperature sample code.
# Author: Leon Anavi <leon@anavi.org>

import sys
import smbus

# By default the address of LM75A is set to 0x48
# aka A0, A1, and A2 are set to GND (0v).
address = 0x48

# Check if another address has been specified
if 1 < len(sys.argv):
	address = int(sys.argv[1], 16)

# Read I2C data and calculate temperature
bus = smbus.SMBus(1)
raw = bus.read_word_data(address, 0) & 0xFFFF
raw = ((raw << 8) & 0xFF00) + (raw >> 8)
temperature = (raw / 32.0) / 8.0
# Print temperature
print 'Temperature: {0:0.2f} *C'.format(temperature)
