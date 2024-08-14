import RPi.GPIO as GPIO
import time

IGNITION_PIN = 17
MOTOR_PIN = 18
PARACHUTE_PIN = 22
DELAY_CHARGE_PIN = 27

def initialize_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(IGNITION_PIN, GPIO.OUT)
    GPIO.setup(MOTOR_PIN, GPIO.OUT)
    GPIO.setup(PARACHUTE_PIN, GPIO.OUT)
    GPIO.setup(DELAY_CHARGE_PIN, GPIO.OUT)

def trigger_delay_charge():
    GPIO.output(DELAY_CHARGE_PIN, True)
    time.sleep(2)
    GPIO.output(DELAY_CHARGE_PIN, False)

def release_parachute():
    GPIO.output(PARACHUTE_PIN, True)
    time.sleep(1)
    GPIO.output(PARACHUTE_PIN, False)
