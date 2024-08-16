import time
import board
import busio
from adafruit_mpu6050 import MPU6050

i2c = busio.I2C(board.SCL, board.SDA)
mpu = MPU6050(i2c)

def read_mpu6050():
    acceleration = mpu.acceleration
    gyro = mpu.gyro
    print(f"Acceleration: {acceleration}, Gyro: {gyro}")

while True:
    read_mpu6050()
    time.sleep(1)
