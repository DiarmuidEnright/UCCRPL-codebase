import RPi.GPIO as GPIO
import time

class FanController:
    def __init__(self, fan_pin: int = 22):
        self.fan_pin = fan_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.fan_pin, GPIO.OUT)
        self.fan_on = False

    def turn_on_fan(self) -> None:
        if not self.fan_on:
            print("Cooling fan turned on")
            GPIO.output(self.fan_pin, GPIO.HIGH)
            self.fan_on = True

    def turn_off_fan(self) -> None:
        if self.fan_on:
            print("Cooling fan turned off")
            GPIO.output(self.fan_pin, GPIO.LOW)
            self.fan_on = False

    def cleanup(self):
        GPIO.output(self.fan_pin, GPIO.LOW)
        GPIO.cleanup()

    def control_fan_based_on_temperature(self, threshold: float = 50.0) -> None:
        """
        Monitor CPU temperature and control the fan.
        This function can be run in a separate thread.
        """
        while True:
            cpu_temp = self.get_cpu_temperature()
            if cpu_temp > threshold:
                self.turn_on_fan()
            else:
                self.turn_off_fan()
            time.sleep(5)

    @staticmethod
    def get_cpu_temperature() -> float:
        """
        Reads the CPU temperature from the Raspberry Pi.
        """
        try:
            with open("/sys/class/thermal/thermal_zone0/temp", "r") as file:
                temp_str = file.read()
                return float(temp_str) / 1000.0
        except FileNotFoundError:
            print("Could not read CPU temperature")
            return 0.0
