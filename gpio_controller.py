
import RPi.GPIO as GPIO
import time
from exceptions import GPIOSetupError, MotorControlError
from logging_config import logger

class GPIOController:
    def __init__(self, ignition_pin=17, motor_pin=18):
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(ignition_pin, GPIO.OUT)
            GPIO.setup(motor_pin, GPIO.OUT)
            self.ignition_pin = ignition_pin
            self.motor_pin = motor_pin
            logger.info("GPIO setup completed successfully.")
        except Exception as e:
            logger.error(f"GPIO setup failed: {e}")
            raise GPIOSetupError("Failed to set up GPIO pins.") from e

    def trigger_ignition(self):
        try:
            logger.debug("Attempting to trigger ignition.")
            GPIO.output(self.ignition_pin, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(self.ignition_pin, GPIO.LOW)
            logger.info("Ignition triggered successfully.")
        except Exception as e:
            logger.error(f"Failed to trigger ignition: {e}")
            raise MotorControlError("Ignition trigger failed.") from e

    def activate_motor(self):
        try:
            logger.debug("Attempting to activate motor.")
            GPIO.output(self.motor_pin, GPIO.HIGH)
            time.sleep(2)
            GPIO.output(self.motor_pin, GPIO.LOW)
            logger.info("Motor activated successfully.")
        except Exception as e:
            logger.error(f"Failed to activate motor: {e}")
            raise MotorControlError("Motor activation failed.") from e
