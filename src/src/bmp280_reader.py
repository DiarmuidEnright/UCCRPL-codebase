import time
import board
import busio
from adafruit_bmp280 import Adafruit_BMP280_I2C
from typing import NoReturn

i2c: busio.I2C = busio.I2C(board.SCL, board.SDA)
bmp280: Adafruit_BMP280_I2C = Adafruit_BMP280_I2C(i2c)

def read_bmp280() -> None:
    temperature: float = bmp280.temperature
    pressure: float = bmp280.pressure
    altitude: float = bmp280.altitude
    print(f"Temperature: {temperature:.2f} C, Pressure: {pressure:.2f} hPa, Altitude: {altitude:.2f} m")

def main() -> NoReturn:
    while True:
        read_bmp280()
        time.sleep(1)

if __name__ == "__main__":
    main()
