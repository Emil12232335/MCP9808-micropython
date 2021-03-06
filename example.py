from machine import Pin, I2C
import MCP9808lib

address = 24
temp_reg = 5
res_reg = 8

i2c = machine.I2C(1, scl=machine.Pin(7), sda=machine.Pin(6))

data = i2c.readfrom_mem(address, temp_reg, 2)
print(MCP9808lib.temp(data))
