# Rocket Telemetry and Control System

## Welcome!
This repo is all about building a comprehensive telemetry and control system for UCC rocket propulsion lab's current and future projects.
## Project Structure

### 1. `data_logging`
- **`analysis.py`**: Analyze the data we’ve logged.
- **`data_logging_to_db.py`**: Directly logs data into our database.
- **`data_logging.py`**: The main script for data logging during flights.
- **`database_setup.sql`**: Sets up the database for storing flight data.
- **`flight_data.db`**: Our database file containing all the flight data.
- **`flight_model_training.py`**: Trains models based on flight data.
- **`logging_config.py`**: Configures how we log all our data.
- **`report_generation.py`**: Generates reports from the flight data.
- **`sensor_logs.csv`**: CSV file with all the raw sensor logs.

### 2. `profiling`
- **`line_profiler_script.py`**: Profiles the time taken by each line of code.
- **`memory_profiler_script.py`**: Keeps an eye on memory usage.
- **`profiler_main.py`**: The main script for running profiles.
- **`py_spy_profiling.sh`**: A handy shell script for using `py-spy` to profile.

### 3. `scripts`
- **`deploy.sh`**: For deploying the system.
- **`run_tests.sh`**: Runs all our tests to make sure everything is working.
- **`setup.sh`**: Sets up the environment for development.

### 4. `camera_content`
- **`camera_capture.py`**: Captures images or video during flight.
- **`camera_conversion.sh`**: Converts the captured media into the right format.

### 5. `controllers`
- **`bmp280_reader.py`**: Reads atmospheric pressure from the BMP280 sensor.
- **`failsafe.py`**: Implements safety mechanisms in case something goes wrong.
- **`gpio_controller.py`**: Controls the GPIO pins.
- **`gps_reader.py`**: Gets GPS data to know where we are.
- **`i2c_controller.py`**: Handles I2C communication with sensors.
- **`iot_client.py`**: Manages IoT connectivity, keeping us connected.
- **`motor.py`**: Controls the rocket's motors.
- **`mpu6050_reader.py`**: Reads motion data from the MPU6050 sensor.
- **`parachute_controller.py`**: Controls the deployment of the parachute.
- **`sensor_data.py`**: General handler for sensor data.

### 6. `dashboards`
- **`app.py`**: The main application for our dashboard.
- **`auth.py`**: Manages who gets access to the dashboard.
- **`exceptions.py`**: Handles errors gracefully.
- **`sensor_motor_dashboard.py`**: Monitors sensors and motor performance.
- **`stats_monitor.py`**: Keeps an eye on vital stats during flight.

### 7. `ml_integration`
- **`ai_decision_making.py`**: Trained model for in-flight adjustments
- **`autopilot.py`**: Movement towards waypoints if needed
- **`rth.py`**: Return to home (Useless until the end of time)


### 8. `telemetry`
- **`sd_receiver.py`**: Receives data from SD cards.
- **`sd_transmitter.py`**: Sends data out.

### 9. `tracking`
- **`tracker.py`**: The main script for tracking.

### 10. `tests`
- **`test_ai_decision_making.py`**: Tests our AI decision-making algorithms.
- **`test_analysis.py`**: Ensures our data analysis scripts are solid.
- **`test_auth.py`**: Tests the authentication system.
- **`test_autopilot.py`**: Checks if the autopilot works as expected.
- **`test_data_logging_to_db.py`**: Makes sure data logging to the database is smooth.
- **`test_failsafe.py`**: Verifies that the failsafe mechanisms work.
- **`test_flight_model_training.py`**: Tests the flight model training process.
- **`test_gpio_controller.py`**: Ensures the GPIO controller functions correctly.
- **`test_iot_client.py`**: Tests IoT connectivity.
- **`test_parachute_controller.py`**: Ensures the parachute controller deploys the chute properly.
- **`test_report_generation.py`**: Checks the report generation process.
- **`test_rth.py`**: Tests the return-to-home functionality.
- **`test_sensor_motor_dashboard.py`**: Tests the dashboard for sensor and motor data.

### Other Important Files
- **`Dockerfile`**: For containerizing the application.
- **`LICENSE`**: Details about the project’s license.
- **`README.md`**: You're reading it!
- **`requirements.txt`**: All the Python dependencies you'll need.
- **`rocket_1.py`**: The main script to run the rocket’s control system.
- **`settings.py`**: Configuration settings for the entire project.

## Getting Started
1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd rocket_code

2. **Install dependancies**:
   ```bash
   pip install -r requirements.txt

3. **Testing**:
   ```bash
   bash scripts/run_tests.sh

4. **Deployment**:
   ```bash
   bash scripts/deploy.sh
