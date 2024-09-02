from src.ml_integration.autopilot import Autopilot
from src.ml_integration.rth import ReturnToHome
from src.ml_integration.ai_decision_making import AIDecisionMaker
from src.tracking.tracker import Tracker
from src.telemetry.sd_receiver import SDReceiver
from src.telemetry.sd_transmitter import SDTransmitter
from src.dashboards.sensor_motor_dashboard import SensorMotorDashboard

autopilot = Autopilot()
return_to_home = ReturnToHome()
ai_decision_maker = AIDecisionMaker()
tracker = Tracker()
sd_receiver = SDReceiver()
sd_transmitter = SDTransmitter()
sensor_motor_dashboard = SensorMotorDashboard()

def execute_flight():
    print("Initiating Rocket Flight Sequence...")
    ai_decision_maker.decide()
    autopilot.activate()
    tracker.start_tracking()
    sd_receiver.receive_data()
    sd_transmitter.transmit_data()
    sensor_motor_dashboard.launch()
    return_to_home.setup()
    print("Rocket Flight Sequence Active.")

if __name__ == "__main__":
    execute_flight()
