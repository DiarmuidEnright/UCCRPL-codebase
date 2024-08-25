import tkinter as tk
from tkinter import ttk
import time
import random
from threading import Thread
from flask import Flask, request
import RPi.GPIO as GPIO
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from typing import Tuple, Dict

def initialize_gpio() -> None:
    global app, turn_on_ignition, turn_on_motor

    app = Flask(__name__)

    IGNITION_PIN: int = 17
    MOTOR_PIN: int = 18
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(IGNITION_PIN, GPIO.OUT)
    GPIO.setup(MOTOR_PIN, GPIO.OUT)

    def turn_on_ignition() -> None:
        print("Ignition turned on")
        GPIO.output(IGNITION_PIN, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(IGNITION_PIN, GPIO.LOW)
        print("Ignition turned off")

    def turn_on_motor() -> None:
        print("Motor turned on")
        GPIO.output(MOTOR_PIN, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(MOTOR_PIN, GPIO.LOW)
        print("Motor turned off")

    @app.route('/launch', methods=['POST'])
    def launch() -> str:
        countdown: int = request.form.get('countdown', type=int)
        if countdown is None or countdown <= 0:
            return "Invalid countdown time. Please enter a positive number."

        print(f"Countdown started: {countdown} seconds")
        time.sleep(countdown)
        turn_on_ignition()
        turn_on_motor()
        return f"Rocket launched after {countdown} seconds!"

    def run_flask() -> None:
        app.run(host='0.0.0.0', port=5000)

    flask_thread = Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

def initialize_i2c() -> None:
    pass  # Placeholder for I2C initialization code

def get_sensor_readings() -> Tuple[float, float, float, float, float, float]:
    accel_x: float = random.uniform(-10, 10)
    accel_y: float = random.uniform(-10, 10)
    accel_z: float = random.uniform(-10, 10)
    gyro_x: float = random.uniform(-180, 180)
    gyro_y: float = random.uniform(-180, 180)
    gyro_z: float = random.uniform(-180, 180)
    return accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z

class Motor:
    def __init__(self, power_hp: float, torque_nm: float, efficiency_percent: float, weight_kg: float) -> None:
        self.power_hp: float = power_hp
        self.torque_nm: float = torque_nm
        self.efficiency_percent: float = efficiency_percent
        self.weight_kg: float = weight_kg

    def set_power(self, new_power_hp: float) -> None:
        self.power_hp = new_power_hp

    def set_torque(self, new_torque_nm: float) -> None:
        self.torque_nm = new_torque_nm

    def set_efficiency(self, new_efficiency_percent: float) -> None:
        self.efficiency_percent = new_efficiency_percent

    def set_weight(self, new_weight_kg: float) -> None:
        self.weight_kg = new_weight_kg

    def get_stats(self) -> Dict[str, str]:
        return {
            "Power": f"{self.power_hp} HP",
            "Torque": f"{self.torque_nm} Nm",
            "Efficiency": f"{self.efficiency_percent}%",
            "Weight": f"{self.weight_kg} kg"
        }

motor = Motor(power_hp=500, torque_nm=700, efficiency_percent=85, weight_kg=350)

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
        
        self.sensor_labels: Dict[str, tk.Label] = {
            "Acceleration X": tk.Label(self.sensor_frame, text="Acceleration X: 0", bg="#403C3C", fg=self.fg_color, font=self.default_font),
            "Acceleration Y": tk.Label(self.sensor_frame, text="Acceleration Y: 0", bg="#403C3C", fg=self.fg_color, font=self.default_font),
            "Acceleration Z": tk.Label(self.sensor_frame, text="Acceleration Z: 0", bg="#403C3C", fg=self.fg_color, font=self.default_font),
            "Gyroscope X": tk.Label(self.sensor_frame, text="Gyroscope X: 0", bg="#403C3C", fg=self.fg_color, font=self.default_font),
            "Gyroscope Y": tk.Label(self.sensor_frame, text="Gyroscope Y: 0", bg="#403C3C", fg=self.fg_color, font=self.default_font),
            "Gyroscope Z": tk.Label(self.sensor_frame, text="Gyroscope Z: 0", bg="#403C3C", fg=self.fg_color, font=self.default_font),
        }
        
        for index, (label_text, label_widget) in enumerate(self.sensor_labels.items()):
            label_widget.grid(row=index, column=0, sticky="w")
        
        self.motor_labels: Dict[str, tk.Label] = {
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
        
        self.sensor_data: Dict[str, list[float]] = {
            "accel_x": [],
            "accel_y": [],
            "accel_z": [],
            "gyro_x": [],
            "gyro_y": [],
            "gyro_z": [],
        }
        
        self.grid_columnconfigure(1, weight=1)
        
        self.update_sensor_data()
        self.update_motor_stats()

    def update_sensor_data(self) -> None:
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
        
        max_length: int = 50
        for key in self.sensor_data:
            if len(self.sensor_data[key]) > max_length:
                self.sensor_data[key].pop(0)
        
        self.ax_accel.clear()
        self.ax_gyro.clear()
        
        colors_accel: list[str] = ["#DC3958", "#F79A32", "#D3AF86"]
        colors_gyro: list[str] = ["#F79A32", "#889B4A", "#088649"]
        
        self.ax_accel.plot(self.sensor_data["accel_x"], label="Accel X", color=colors_accel[0])
        self.ax_accel.plot(self.sensor_data["accel_y"], label="Accel Y", color=colors_accel[1])
        self.ax_accel.plot(self.sensor_data["accel_z"], label="Accel Z", color=colors_accel[2])
        self.ax_accel.legend(loc="upper right", frameon=True, fontsize='small', prop={'family': 'Menlo'})
        self.ax_accel.grid(True, color=self.fg_color, linestyle='--', linewidth=0.5)
        self.ax_accel.tick_params(axis='both', colors=self.fg_color)
        
        self.ax_gyro.plot(self.sensor_data["gyro_x"], label="Gyro X", color=colors_gyro[0])
        self.ax_gyro.plot(self.sensor_data["gyro_y"], label="Gyro Y", color=colors_gyro[1])
        self.ax_gyro.plot(self.sensor_data["gyro_z"], label="Gyro Z", color=colors_gyro[2])
        self.ax_gyro.legend(loc="upper right", frameon=True, fontsize='small', prop={'family': 'Menlo'})
        self.ax_gyro.grid(True, color=self.fg_color, linestyle='--', linewidth=0.5)
        self.ax_gyro.tick_params(axis='both', colors=self.fg_color)
        
        self.canvas.draw()
        self.after(100, self.update_sensor_data)
    
    def update_motor_stats(self) -> None:
        stats: Dict[str, str] = motor.get_stats()
        for stat_name, stat_value in stats.items():
            self.motor_labels[stat_name].config(text=f"{stat_name}: {stat_value}")
        
        self.after(1000, self.update_motor_stats)

if __name__ == "__main__":
    initialize_gpio()
    initialize_i2c()
    dashboard = SensorMotorDashboard()
    dashboard.mainloop()