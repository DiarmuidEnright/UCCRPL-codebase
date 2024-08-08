import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sensor_data import get_sensor_readings
from motor import motor
from parachute_controller import release_parachute

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
            "Acceleration X": tk.Label(self.sensor_frame, text="Acceleration X: 0", bg=self.bg_color, fg=self.fg_color, font=self.default_font),
            "Acceleration Y": tk.Label(self.sensor_frame, text="Acceleration Y: 0", bg=self.bg_color, fg=self.fg_color, font=self.default_font),
            "Acceleration Z": tk.Label(self.sensor_frame, text="Acceleration Z: 0", bg=self.bg_color, fg=self.fg_color, font=self.default_font),
            "Gyroscope X": tk.Label(self.sensor_frame, text="Gyroscope X: 0", bg=self.bg_color, fg=self.fg_color, font=self.default_font),
            "Gyroscope Y": tk.Label(self.sensor_frame, text="Gyroscope Y: 0", bg=self.bg_color, fg=self.fg_color, font=self.default_font),
            "Gyroscope Z": tk.Label(self.sensor_frame, text="Gyroscope Z: 0", bg=self.bg_color, fg=self.fg_color, font=self.default_font),
        }
        
        for index, label_widget in enumerate(self.sensor_labels.values()):
            label_widget.grid(row=index, column=0, sticky="w")
        
        self.motor_labels = {
            "Power": tk.Label(self.motor_frame, text="Power: 0 HP", bg=self.bg_color, fg=self.fg_color, font=self.default_font),
            "Torque": tk.Label(self.motor_frame, text="Torque: 0 Nm", bg=self.bg_color, fg=self.fg_color, font=self.default_font),
            "Efficiency": tk.Label(self.motor_frame, text="Efficiency: 0%", bg=self.bg_color, fg=self.fg_color, font=self.default_font),
            "Weight": tk.Label(self.motor_frame, text="Weight: 0 kg", bg=self.bg_color, fg=self.fg_color, font=self.default_font),
        }
        
        for index, label_widget in enumerate(self.motor_labels.values()):
            label_widget.grid(row=index, column=0, sticky="w")
        
        # Adding the parachute release button
        self.parachute_button = tk.Button(self.motor_frame, text="Release Parachute", command=self.release_parachute, bg=self.accent_color, fg=self.fg_color, font=self.default_font)
        self.parachute_button.grid(row=4, column=0, pady=10, sticky="w")
        
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
        self.ax_gyro.clear()
        
        colors_accel = ["#DC3958", "#F79A32", "#D3AF86"]
        colors_gyro = ["#F79A32", "#889B4A", "#088649"]
        
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
    
    def update_motor_stats(self):
        stats = motor.get_stats()
        self.motor_labels["Power"].config(text=f"Power: {stats['Power']}")
        self.motor_labels["Torque"].config(text=f"Torque: {stats['Torque']}")
        self.motor_labels["Efficiency"].config(text=f"Efficiency: {stats['Efficiency']}")
        self.motor_labels["Weight"].config(text=f"Weight: {stats['Weight']}")
        
        self.after(1000, self.update_motor_stats)
    
    def release_parachute(self):
        release_parachute()
        print("Parachute released via dashboard.")

if __name__ == "__main__":
    dashboard = SensorMotorDashboard()
    dashboard.mainloop()
