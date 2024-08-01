import time
import board
import busio
from adafruit_bmp280 import Adafruit_BMP280_I2C

class TemperaturePressureMonitor:
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.bmp280 = Adafruit_BMP280_I2C(self.i2c)

    def get_temperature(self):
        return self.bmp280.temperature

    def get_pressure(self):
        return self.bmp280.pressure

    def display_readings(self):
        temperature = self.get_temperature()
        pressure = self.get_pressure()
        print(f"Temperature: {temperature:.2f} C")
        print(f"Pressure: {pressure:.2f} hPa")

    def run(self):
        try:
            print("Temperature and Pressure Monitor started. Press Ctrl+C to stop.")
            while True:
                self.display_readings()
                time.sleep(5)  # Adjust the interval as needed
        except KeyboardInterrupt:
            print("Temperature and Pressure Monitor stopped.")

if __name__ == "__main__":
    monitor = TemperaturePressureMonitor()
    monitor.run()
