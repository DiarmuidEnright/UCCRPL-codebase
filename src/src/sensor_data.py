import random
from typing import Tuple

def get_sensor_readings() -> Tuple[float, float, float, float, float, float]:
    accel_x: float = random.uniform(-10, 10)
    accel_y: float = random.uniform(-10, 10)
    accel_z: float = random.uniform(-10, 10)
    gyro_x: float = random.uniform(-180, 180)
    gyro_y: float = random.uniform(-180, 180)
    gyro_z: float = random.uniform(-180, 180)
    return accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z