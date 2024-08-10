import RPi.GPIO as GPIO
import time

DELAY_CHARGE_PIN = 22 

def initialize_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DELAY_CHARGE_PIN, GPIO.OUT)


def trigger_delay_charge():
    print("Triggering delay charge for rocket separation")
    GPIO.output(DELAY_CHARGE_PIN, GPIO.HIGH)
    time.sleep(1)  # Duration for which the charge is active
    GPIO.output(DELAY_CHARGE_PIN, GPIO.LOW)
    print("Delay charge completed, rocket separated from thruster")

def cleanup_gpio():
    GPIO.cleanup()
