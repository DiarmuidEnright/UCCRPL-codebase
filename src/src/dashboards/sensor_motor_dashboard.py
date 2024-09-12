import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import RPi.GPIO as GPIO
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import logging
from gpio_controller import trigger_delay_charge, release_parachute, initialize_gpio, cleanup_gpio
from motor import Motor
from sensor_data import get_sensor_readings
from failsafe import start_failsafe_monitoring
from auth import authenticate
from camera_capture import RocketCamera

logging.basicConfig(filename="rocket_dashboard.log", level=logging.DEBUG, 
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

class SensorMotorDashboard(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Rocket Dashboard")
        self.geometry("1200x600")
        
        self.bg_color: str = "#221a0e"
        self.fg_color: str = "#d4d4d4"
        self.accent_color: str = "#569cd6"
        
        self.configure(bg=self.bg_color)
        
        self.default_font: tuple[str, int] = ("Menlo", 14)

        self.sensor_frame: ttk.LabelFrame = ttk.LabelFrame(self, text="Sensor Data", padding=(10, 5))
        self.sensor_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.motor_frame: ttk.LabelFrame = ttk.LabelFrame(self, text="Motor Information", padding=(10, 5))
        self.motor_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.sensor_labels: dict[str, tk.Label] = {
            "Acceleration X": tk.Label(self.sensor_frame, text="Acceleration X: 0", bg="#403C3C", fg=self.fg_color, font=self.default_font),
            "Acceleration Y": tk.Label(self.sensor_frame, text="Acceleration Y: 0", bg="#403C3C", fg=self.fg_color, font=self.default_font),
            "Acceleration Z": tk.Label(self.sensor_frame, text="Acceleration Z: 0", bg="#403C3C", fg=self.fg_color, font=self.default_font),
            "Gyroscope X": tk.Label(self.sensor_frame, text="Gyroscope X: 0", bg="#403C3C", fg=self.fg_color, font=self.default_font),
            "Gyroscope Y": tk.Label(self.sensor_frame, text="Gyroscope Y: 0", bg="#403C3C", fg=self.fg_color, font=self.default_font),
            "Gyroscope Z": tk.Label(self.sensor_frame, text="Gyroscope Z: 0", bg="#403C3C", fg=self.fg_color, font=self.default_font),
        }
        
        for index, (label_text, label_widget) in enumerate(self.sensor_labels.items()):
            label_widget.grid(row=index, column=0, sticky="w")
        
        self.motor_labels: dict[str, tk.Label] = {
            "Power": tk.Label(self.motor_frame, text="Power: 0 HP", bg="#403C3C", fg=self.fg_color, font=self.default_font),
            "Torque": tk.Label(self.motor_frame, text="Torque: 0 Nm", bg="#403C3C", fg=self.fg_color, font=self.default_font),
            "Efficiency": tk.Label(self.motor_frame, text="Efficiency: 0%", bg="#403C3C", fg=self.fg_color, font=self.default_font),
            "Weight": tk.Label(self.motor_frame, text="Weight: 0 kg", bg="#403C3C", fg=self.fg_color, font=self.default_font),
        }
        
        for index, (label_text, label_widget) in enumerate(self.motor_labels.items()):
            label_widget.grid(row=index, column=0, sticky="w")
        
        self.figure: Figure = Figure(figsize=(8, 6), dpi=100, facecolor=self.bg_color)
        self.ax_accel = self.figure.add_subplot(211, facecolor=self.bg_color)
        self.ax_gyro = self.figure.add_subplot(212, facecolor=self.bg_color)
        
        self.ax_accel.set_title("Acceleration Data Over Time", color=self.fg_color, fontsize=12, fontname="Menlo")
        self.ax_accel.set_xlabel("Time", color=self.fg_color, fontsize=12, fontname="Menlo")
        self.ax_accel.set_ylabel("Acceleration (m/s^2)", color=self.fg_color, fontsize=12, fontname="Menlo")
        
        self.ax_gyro.set_title("Gyroscope Data Over Time", color=self.fg_color, fontsize=12, fontname="Menlo")
        self.ax_gyro.set_xlabel("Time", color=self.fg_color, fontsize=12, fontname="Menlo")
        self.ax_gyro.set_ylabel("Angular Velocity (deg/s)", color=self.fg_color, fontsize=12, fontname="Menlo")
        
        self.canvas: FigureCanvasTkAgg = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.get_tk_widget().grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")
        
        self.sensor_data: dict[str, list[float]] = {
            "accel_x": [],
            "accel_y": [],
            "accel_z": [],
            "gyro_x": [],
            "gyro_y": [],
            "gyro_z": [],
        }
        
        self.grid_columnconfigure(1, weight=1)
        
        self.is_authorized: bool = False
        
        try:
            self.update_sensor_data()
            self.update_motor_stats()
            self.rocket_camera: RocketCamera = RocketCamera()
            start_failsafe_monitoring()
            logging.info("Dashboard initialized successfully.")
        except Exception as e:
            logging.error(f"Error initializing dashboard: {e}")
            messagebox.showerror("Initialization Error", f"Failed to initialize the dashboard: {e}")

    def update_sensor_data(self) -> None:
        try:
            accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z = get_sensor_readings()
            self.sensor_labels["Acceleration X"].config(text=f"Acceleration X: {accel_x:.2f}")
            self.sensor_labels["Acceleration Y"].config(text=f"Acceleration Y: {accel_y:.2f}")
            self.sensor_labels["Acceleration Z"].config(text=f"Acceleration Z: {accel_z:.2f}")
            self.sensor_labels["Gyroscope X"].config(text=f"Gyroscope X: {gyro_x:.2f}")
            self.sensor_labels["Gyroscope Y"].config(text=f"Gyroscope Y: {gyro_y:.2f}")
            self.sensor_labels["Gyroscope Z"].config(text=f"Gyroscope Z: {gyro_z:.2f}")
            
            self.sensor_data["accel_x"].append(accel_x)
            self.sensor_data["accel_y"].append(accel_y)
            self.sensor_data["accel_z"].append(accel_z)
            self.sensor_data["gyro_x"].append(gyro_x)
            self.sensor_data["gyro_y"].append(gyro_y)
            self.sensor_data["gyro_z"].append(gyro_z)
            
            max_length = 50
            for key in self.sensor_data:
                if len(self.sensor_data[key]) > max_length:
                    self.sensor_data[key].pop(0)
            
            self.ax_accel.clear()
            self.ax_accel.plot(self.sensor_data["accel_x"], label="Acceleration X", color="#1f77b4")
            self.ax_accel.plot(self.sensor_data["accel_y"], label="Acceleration Y", color="#ff7f0e")
            self.ax_accel.plot(self.sensor_data["accel_z"], label="Acceleration Z", color="#2ca02c")
            self.ax_accel.legend(loc="upper left", fontsize=10)
            self.ax_accel.grid(True)
            
            self.ax_gyro.clear()
            self.ax_gyro.plot(self.sensor_data["gyro_x"], label="Gyroscope X", color="#d62728")
            self.ax_gyro.plot(self.sensor_data["gyro_y"], label="Gyroscope Y", color="#9467bd")
            self.ax_gyro.plot(self.sensor_data["gyro_z"], label="Gyroscope Z", color="#8c564b")
            self.ax_gyro.legend(loc="upper left", fontsize=10)
            self.ax_gyro.grid(True)
            
            self.canvas.draw()
            logging.debug("Sensor data updated successfully.")
            self.after(1000, self.update_sensor_data)
        except Exception as e:
            logging.error(f"Error updating sensor data: {e}")
            messagebox.showerror("Sensor Error", f"Failed to update sensor data: {e}")

    def update_motor_stats(self) -> None:
        try:
            motor = Motor()
            self.motor_labels["Power"].config(text=f"Power: {motor.power_hp:.2f} HP")
            self.motor_labels["Torque"].config(text=f"Torque: {motor.torque_nm:.2f} Nm")
            self.motor_labels["Efficiency"].config(text=f"Efficiency: {motor.efficiency_percent:.2f}%")
            self.motor_labels["Weight"].config(text=f"Weight: {motor.weight_kg:.2f} kg")
            logging.debug("Motor stats updated successfully.")
            self.after(1000, self.update_motor_stats)
        except Exception as e:
            logging.error(f"Error updating motor stats: {e}")
            messagebox.showerror("Motor Error", f"Failed to update motor stats: {e}")

    def trigger_delay_charge(self) -> None:
        try:
            self.request_authorization()
            if self.is_authorized:
                trigger_delay_charge()
                logging.info("Delay charge triggered successfully.")
            else:
                logging.warning("Unauthorized attempt to trigger delay charge.")
        except Exception as e:
            logging.error(f"Error triggering delay charge: {e}")
            messagebox.showerror("Charge Error", f"Failed to trigger delay charge: {e}")

    def release_parachute(self) -> None:
        try:
            self.request_authorization()
            if self.is_authorized:
                release_parachute()
                logging.info("Parachute released successfully.")
            else:
                logging.warning("Unauthorized attempt to release parachute.")
        except Exception as e:
            logging.error(f"Error releasing parachute: {e}")
            messagebox.showerror("Parachute Error", f"Failed to release parachute: {e}")

    def launch_rocket(self) -> None:
        self.rocket_camera.start_recording(duration=120)

    def request_authorization(self) -> None:
        try:
            username: str = simpledialog.askstring("Authentication", "Enter Username:", parent=self)
            password: str = simpledialog.askstring("Authentication", "Enter Password:", parent=self, show='*')

            if authenticate(username, password):
                self.is_authorized = True
                logging.info(f"User '{username}' authenticated successfully.")
            else:
                self.is_authorized = False
                logging.warning(f"Failed authentication attempt for user '{username}'.")
                messagebox.showerror("Authentication Failed", "Incorrect username or password")
        except Exception as e:
            logging.error(f"Error during authentication: {e}")
            messagebox.showerror("Authentication Error", f"Failed to authenticate: {e}")
            #I forgot

if __name__ == "__main__":
    initialize_gpio()
    try:
        dashboard = SensorMotorDashboard()
        dashboard.mainloop()
    except Exception as e:
        logging.critical(f"Critical error: {e}")
    finally:
        cleanup_gpio()
        logging.info("GPIO cleanup complete.")
