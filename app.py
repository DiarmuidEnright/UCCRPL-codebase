from flask import Flask, request
from gpio_controller import initialize_gpio
from sensor_motor_dashboard import SensorMotorDashboard
from parachute_controller import initialize_parachute, release_parachute, check_and_release_parachute
import time

app = Flask(__name__)

@app.route('/launch', methods=['POST'])
def launch():
    from gpio_controller import turn_on_ignition, turn_on_motor
    
    countdown = request.json.get('countdown')
    if countdown is None or countdown <= 0:
        return "Invalid countdown time. Please enter a positive number.", 400

    print(f"Countdown started: {countdown} seconds")
    time.sleep(countdown)
    turn_on_ignition()
    turn_on_motor()
    return f"Rocket launched after {countdown} seconds!", 200

@app.route('/release_parachute', methods=['POST'])
def manual_parachute_release():
    release_parachute()
    return "Parachute released!", 200

@app.route('/altitude_check', methods=['POST'])
def altitude_check():
    altitude = request.json.get('altitude')
    threshold = request.json.get('threshold', 1000)
    
    if altitude is None:
        return "Altitude data missing.", 400
    
    check_and_release_parachute(altitude, threshold)
    return f"Altitude checked: {altitude} meters.", 200

if __name__ == "__main__":
    initialize_gpio()
    initialize_parachute()
    app.run(host='0.0.0.0', port=5000)
    dashboard = SensorMotorDashboard()
    dashboard.mainloop()
