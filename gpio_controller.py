from flask import Flask, request
import RPi.GPIO as GPIO
import time
import threading

app = Flask(__name__)

IGNITION_PIN = 17
MOTOR_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(IGNITION_PIN, GPIO.OUT)
GPIO.setup(MOTOR_PIN, GPIO.OUT)

def turn_on_ignition():
    GPIO.output(IGNITION_PIN, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(IGNITION_PIN, GPIO.LOW)

def turn_on_motor():
    GPIO.output(MOTOR_PIN, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(MOTOR_PIN, GPIO.LOW)

@app.route('/launch', methods=['POST'])
def launch():
    countdown = request.form.get('countdown', type=int)
    if countdown is None or countdown <= 0:
        return "Invalid countdown time. Please enter a positive number."

    time.sleep(countdown)
    turn_on_ignition()
    turn_on_motor()
    return f"Rocket launched after {countdown} seconds!"

def initialize_gpio():
    flask_thread = threading.Thread(target=app.run, kwargs={'host': '0.0.0.0', 'port': 5000})
    flask_thread.daemon = True
    flask_thread.start()
