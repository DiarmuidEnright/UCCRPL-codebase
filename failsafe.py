import time
from threading import Thread
from sensor_data import get_altitude 
from gpio_controller import release_parachute

ALTITUDE_THRESHOLD = 1000 
CHECK_INTERVAL = 1

def monitor_altitude():
    while True:
        altitude = get_altitude()
        if altitude <= ALTITUDE_THRESHOLD:
            print("Failsafe: Altitude threshold reached. Deploying parachute.")
            release_parachute()
            break
        time.sleep(CHECK_INTERVAL)

def start_failsafe_monitoring():
    failsafe_thread = Thread(target=monitor_altitude)
    failsafe_thread.daemon = True
    failsafe_thread.start()
