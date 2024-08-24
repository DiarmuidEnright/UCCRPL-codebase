import time
from threading import Thread
from sensor_data import get_altitude
from gpio_controller import release_parachute
from typing import NoReturn

ALTITUDE_THRESHOLD: int = 1000
CHECK_INTERVAL: int = 1

def monitor_altitude() -> NoReturn:
    while True:
        altitude: float = get_altitude()
        if altitude <= ALTITUDE_THRESHOLD:
            print("Failsafe: Altitude threshold reached. Deploying parachute.")
            release_parachute()
            break
        time.sleep(CHECK_INTERVAL)

def start_failsafe_monitoring() -> None:
    failsafe_thread: Thread = Thread(target=monitor_altitude)
    failsafe_thread.daemon = True
    failsafe_thread.start()
