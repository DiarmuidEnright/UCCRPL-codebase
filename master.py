from src.ml_integration.autopilot import Autopilot
from src.ml_integration.rth import ReturnToHome
from src.ml_integration.ai_decision_making import AIDecisionMaker
from src.tracking.tracker import Tracker
from src.telemetry.sd_receiver import SDReceiver
from src.telemetry.sd_transmitter import SDTransmitter
from src.dashboards.sensor_motor_dashboard import SensorMotorDashboard
from src.data_logging.data_logging import DataLogger
from src.data_logging.flight_model_training import FlightModelTrainer
from src.data_logging.report_generation import ReportGenerator

autopilot = Autopilot()
return_to_home = ReturnToHome()
ai_decision_maker = AIDecisionMaker()
tracker = Tracker()
sd_receiver = SDReceiver()
sd_transmitter = SDTransmitter()
sensor_motor_dashboard = SensorMotorDashboard()
data_logger = DataLogger()
flight_model_trainer = FlightModelTrainer()
report_generator = ReportGenerator()

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

def pre_flight_operations():
    print("Initiating Pre-Flight Operations...")
    # implement something here at some point

def post_flight_operations():
    print("Initiating Post-Flight Operations...")
    data_logger.initialize()
    flight_model_trainer.train_model()
    report_generator.generate()
    print("Post-Flight Operations Complete.")

if __name__ == "__main__":
    execute_flight()
    # Uncomment the line below to run post-flight operations after the flight
    # post_flight_operations()
    # pre_flight_operations()