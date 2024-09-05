from flask import Flask, request, jsonify
from gpio_controller import initialize_gpio, turn_on_ignition, turn_on_motor
from sensor_motor_dashboard import SensorMotorDashboard
from parachute_controller import initialize_parachute, release_parachute, check_and_release_parachute
from iot_client import IoTClient, iot_callback
from typing import Optional, Dict, Any
import time

app = Flask(__name__)

iot_client: Optional[IoTClient] = None

def initialize_iot() -> None:
    global iot_client
    iot_client = IoTClient(
        client_id="rocketClient",
        endpoint="your-endpoint.amazonaws.com",
        cert_path="cert.pem",
        key_path="private.key",
        root_ca_path="root-ca.pem"
    )
    iot_client.connect()
    iot_client.subscribe("rocket/control", iot_callback)


@app.route('/launch', methods=['POST'])
def launch() -> Any:
    countdown: Optional[int] = request.json.get('countdown')
    
    if countdown is None or countdown <= 0:
        return jsonify({"error": "Invalid countdown time. Please enter a positive number."}), 400

    print(f"Countdown started: {countdown} seconds")
    time.sleep(countdown)
    turn_on_ignition()
    turn_on_motor()
    return jsonify({"message": f"Rocket launched after {countdown} seconds!"}), 200

@app.route('/release_parachute', methods=['POST'])
def manual_parachute_release() -> Any:
    release_parachute()
    return jsonify({"message": "Parachute released!"}), 200

@app.route('/altitude_check', methods=['POST'])
def altitude_check() -> Any:
    data: Dict[str, Any] = request.json
    altitude: Optional[int] = data.get('altitude')
    threshold: int = data.get('threshold', 1000)
    
    if altitude is None:
        return jsonify({"error": "Altitude data missing."}), 400
    
    check_and_release_parachute(altitude, threshold)
    return jsonify({"message": f"Altitude checked: {altitude} meters."}), 200

if __name__ == "__main__":
    initialize_iot()
    initialize_gpio()
    initialize_parachute()
    app.run(host='0.0.0.0', port=5000)
    dashboard = SensorMotorDashboard()
    dashboard.mainloop()


#forgot to commit :skull: