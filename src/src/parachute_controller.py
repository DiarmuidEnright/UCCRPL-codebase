import RPi.GPIO as GPIO
import time
from typing import Optional

PARACHUTE_PIN: int = 27  

def initialize_parachute() -> None:
    GPIO.setup(PARACHUTE_PIN, GPIO.OUT)
    GPIO.output(PARACHUTE_PIN, GPIO.LOW)  

def release_parachute() -> None:
    print("Parachute release initiated")
    GPIO.output(PARACHUTE_PIN, GPIO.HIGH)
    time.sleep(1)  
    GPIO.output(PARACHUTE_PIN, GPIO.LOW)
    print("Parachute release completed")

def check_and_release_parachute(altitude: float, threshold: Optional[float] = 1000) -> None:
    if altitude < threshold:
        release_parachute()
    else:
        print(f"Altitude {altitude} is above the threshold; parachute not released")
