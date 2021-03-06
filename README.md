# MCP9808-micropython
Drivers for the MCP9808 temperature sensor for micropython. Made for the Raspberry Pi Pico

Example:
from machine import Pin, I2C
import MCP9808lib

address = 24
temp_reg = 5
res_reg = 8

i2c = machine.I2C(1, scl=machine.Pin(7), sda=machine.Pin(6))

MCP9808lib.temp(data)

