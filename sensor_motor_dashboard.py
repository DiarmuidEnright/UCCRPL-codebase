import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import time
import random
from threading import Thread
from flask import Flask, request
import RPi.GPIO as GPIO
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from gpio_controller import trigger_delay_charge, release_parachute, initialize_gpio, cleanup_gpio
from motor import Motor
from sensor_data import get_sensor_readings
from failsafe import start_failsafe_monitoring
from auth import authenticate

class SensorMotorDashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rocket Dashboard")
        self.geometry("1200x600")
        
        self.bg_color = "#221a0e"
        self.fg_color = "#d4d4d4"
        self.accent_color = "#569cd6"
        
        self.configure(bg=self.bg_color)
        
        self.default_font = ("Menlo", 14)

        self.sensor_frame = ttk.LabelFrame(self, text="Sensor Data", padding=(10, 5))
        self.sensor_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.motor_frame = ttk.LabelFrame(self, text="Motor Information", padding=(10, 5))
        self.motor_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.sensor_labels = {
            "Acceleration X": tk.Label(self.sensor_frame, text="Acceleration X: 0", bg="#403C3C", fg=self.fg_color, font=self.default_font),
            "Acceleration Y": tk.Label(self.sensor_frame, text="Acceleration Y: 0", bg="#403C3C", fg=self.fg_color, font=self.default_font),
            "Acceleration Z": tk.Label(self.sensor_frame, text="Acceleration Z: 0", bg="#403C3C", fg=self.fg_color, font=self.default_font),
            "Gyroscope X": tk.Label(self.sensor_frame, text="Gyroscope X: 0", bg="#403C3C", fg=self.fg_color, font=self.default_font),
            "Gyroscope Y": tk.Label(self.sensor_frame, text="Gyroscope Y: 0", bg="#403C3C", fg=self.fg_color, font=self.default_font),
            "Gyroscope Z": tk.Label(self.sensor_frame, text="Gyroscope Z: 0", bg="#403C3C", fg=self.fg_color, font=self.default_font),
        }
        
        for index, (label_text, label_widget) in enumerate(self.sensor_labels.items()):
            label_widget.grid(row=index, column=0, sticky="w")
        
        self.motor_labels = {
            "Power": tk.Label(self.motor_frame, text="Power: 0 HP", bg="#403C3C", fg=self.fg_color, font=self.default_font),
            "Torque": tk.Label(self.motor_frame, text="Torque: 0 Nm", bg="#403C3C", fg=self.fg_color, font=self.default_font),
            "Efficiency": tk.Label(self.motor_frame, text="Efficiency: 0%", bg="#403C3C", fg=self.fg_color, font=self.default_font),
            "Weight": tk.Label(self.motor_frame, text="Weight: 0 kg", bg="#403C3C", fg=self.fg_color, font=self.default_font),
        }
        
        for index, (label_text, label_widget) in enumerate(self.motor_labels.items()):
            label_widget.grid(row=index, column=0, sticky="w")
        
        self.figure = Figure(figsize=(8, 6), dpi=100, facecolor=self.bg_color)
        self.ax_accel = self.figure.add_subplot(211, facecolor=self.bg_color)
        self.ax_gyro = self.figure.add_subplot(212, facecolor=self.bg_color)
        
        self.ax_accel.set_title("Acceleration Data Over Time", color=self.fg_color, fontsize=12, fontname="Menlo")
        self.ax_accel.set_xlabel("Time", color=self.fg_color, fontsize=12, fontname="Menlo")
        self.ax_accel.set_ylabel("Acceleration (m/s^2)", color=self.fg_color, fontsize=12, fontname="Menlo")
        
        self.ax_gyro.set_title("Gyroscope Data Over Time", color=self.fg_color, fontsize=12, fontname="Menlo")
        self.ax_gyro.set_xlabel("Time", color=self.fg_color, fontsize=12, fontname="Menlo")
        self.ax_gyro.set_ylabel("Angular Velocity (deg/s)", color=self.fg_color, fontsize=12, fontname="Menlo")
        
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.get_tk_widget().grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")
        
        self.sensor_data = {
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

        start_failsafe_monitoring()  # Start monitoring altitude for failsafe

    def update_sensor_data(self):
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
        self.after(1000, self.update_sensor_data)

    def update_motor_stats(self):
        motor = Motor()
        self.motor_labels["Power"].config(text=f"Power: {motor.power:.2f} HP")
        self.motor_labels["Torque"].config(text=f"Torque: {motor.torque:.2f} Nm")
        self.motor_labels["Efficiency"].config(text=f"Efficiency: {motor.efficiency:.2f}%")
        self.motor_labels["Weight"].config(text=f"Weight: {motor.weight:.2f} kg")
        self.after(1000, self.update_motor_stats)
    
    def trigger_delay_charge(self):
        self.request_authorization()
        if self.is_authorized:
            trigger_delay_charge()

    def release_parachute(self):
        self.request_authorization()
        if self.is_authorized:
            release_parachute()

    def request_authorization(self):
        username = simpledialog.askstring("Authentication", "Enter Username:", parent=self)
        password = simpledialog.askstring("Authentication", "Enter Password:", parent=self, show='*')

        if authenticate(username, password):
            self.is_authorized = True
        else:
            self.is_authorized = False
            messagebox.showerror("Authentication Failed", "Incorrect username or password")


if __name__ == "__main__":
    initialize_gpio()
    try:
        dashboard = SensorMotorDashboard()
        dashboard.mainloop()
    finally:
        cleanup_gpio()
