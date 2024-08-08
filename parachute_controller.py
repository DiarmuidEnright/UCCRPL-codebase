import RPi.GPIO as GPIO
import time

PARACHUTE_PIN = 27  # GPIO pin connected to the parachute release mechanism

def initialize_parachute():
    GPIO.setup(PARACHUTE_PIN, GPIO.OUT)
    GPIO.output(PARACHUTE_PIN, GPIO.LOW)  # Ensure the parachute release is initially deactivated

def release_parachute():
    print("Parachute release initiated")
    GPIO.output(PARACHUTE_PIN, GPIO.HIGH)
    time.sleep(1)  # Hold the release mechanism active for 1 second
    GPIO.output(PARACHUTE_PIN, GPIO.LOW)
    print("Parachute release completed")

# Example of a safety check for altitude (you can call this function as needed):
def check_and_release_parachute(altitude, threshold=1000):
    if altitude < threshold:
        release_parachute()
    else:
        print(f"Altitude {altitude} is above the threshold; parachute not released")
