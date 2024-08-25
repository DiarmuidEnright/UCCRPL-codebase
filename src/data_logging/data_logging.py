import time
import board
import busio
import adafruit_bmp280
import adafruit_mpu6050
import digitalio
import adafruit_sdcard
import storage
from typing import Tuple

i2c: busio.I2C = busio.I2C(board.SCL, board.SDA)
bmp280: adafruit_bmp280.Adafruit_BMP280_I2C = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
mpu6050: adafruit_mpu6050.MPU6050 = adafruit_mpu6050.MPU6050(i2c)

spi: board.SPI = board.SPI()
cs: digitalio.DigitalInOut = digitalio.DigitalInOut(board.D5)
sd_card: adafruit_sdcard.SDCard = adafruit_sdcard.SDCard(spi, cs)
vfs: storage.VfsFat = storage.VfsFat(sd_card)
storage.mount(vfs, "/sd")

log_file = open("/sd/sensor_logs.csv", "a")

def log_data() -> None:
    temperature: float = bmp280.temperature
    pressure: float = bmp280.pressure
    altitude: float = bmp280.altitude
    acceleration: Tuple[float, float, float] = mpu6050.acceleration
    gyro: Tuple[float, float, float] = mpu6050.gyro

    log_file.write(
        f"Time: {time.time()}, "
        f"Temperature: {temperature}, "
        f"Pressure: {pressure}, "
        f"Altitude: {altitude}, "
        f"Acceleration: {acceleration}, "
        f"Gyro: {gyro}\n"
    )
    log_file.flush()

while True:
    log_data()
    time.sleep(1)
