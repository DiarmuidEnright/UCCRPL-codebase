import time
import board
import busio
from adafruit_bmp280 import Adafruit_BMP280_I2C

i2c = busio.I2C(board.SCL, board.SDA)
bmp280 = Adafruit_BMP280_I2C(i2c)

def read_bmp280():
    temperature = bmp280.temperature
    pressure = bmp280.pressure
    altitude = bmp280.altitude
    print(f"Temperature: {temperature} C, Pressure: {pressure} hPa, Altitude: {altitude} m")

while True:
    read_bmp280()
    time.sleep(1)
  