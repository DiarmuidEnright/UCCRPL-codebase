import threading
from gpio_controller import initialize_gpio
from i2c_controller import initialize_i2c
from sensor_motor_dashboard import SensorMotorDashboard

def run_flask():
    from gpio_controller import app
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    initialize_gpio()
    initialize_i2c()
    
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    dashboard = SensorMotorDashboard()
    dashboard.mainloop()
