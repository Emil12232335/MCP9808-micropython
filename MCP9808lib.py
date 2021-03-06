import machine
def temp(data):
    address = 24
    temp_reg = 5
    res_reg = 8
    i2c = machine.I2C(1, scl=machine.Pin(7), sda=machine.Pin(6))
    data = i2c.readfrom_mem(address, temp_reg, 2)
    value = data[0] << 8 | data[1]
    temp = (value & 0xFFF) / 16.0
    if value & 0x1000:
        temp -= 256.0
    return temp
