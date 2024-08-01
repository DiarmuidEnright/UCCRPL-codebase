import random

def get_sensor_readings():
    accel_x = random.uniform(-10, 10)
    accel_y = random.uniform(-10, 10)
    accel_z = random.uniform(-10, 10)
    gyro_x = random.uniform(-180, 180)
    gyro_y = random.uniform(-180, 180)
    gyro_z = random.uniform(-180, 180)
    return accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z
