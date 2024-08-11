import RPi.GPIO as GPIO
import time

DELAY_CHARGE_PIN = 22
PARACHUTE_PIN = 17

def initialize_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DELAY_CHARGE_PIN, GPIO.OUT)
    GPIO.setup(PARACHUTE_PIN, GPIO.OUT)

def trigger_delay_charge():
    GPIO.output(DELAY_CHARGE_PIN, GPIO.HIGH)
    time.sleep(2)  # Example delay
    GPIO.output(DELAY_CHARGE_PIN, GPIO.LOW)

def release_parachute():
    GPIO.output(PARACHUTE_PIN, GPIO.HIGH)
    time.sleep(1)  # Example activation time
    GPIO.output(PARACHUTE_PIN, GPIO.LOW)

def cleanup_gpio():
    GPIO.cleanup()
