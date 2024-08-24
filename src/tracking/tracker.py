import serial
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from typing import Optional, Dict

class GPSTracker:
    def __init__(self, port: str = '/dev/ttyS0', baudrate: int = 9600) -> None:
        self.port = port
        self.baudrate = baudrate
        try:
            self.ser = serial.Serial(self.port, self.baudrate, timeout=1)
        except Exception as e:
            print(f"Error opening serial port {self.port}: {e}")
            raise e
        self.last_known_position: Dict[str, Optional[float]] = {"latitude": None, "longitude": None}

    def parse_gps_data(self, data: str) -> None:
        if data.startswith('$GPRMC'):
            parts = data.split(',')
            if len(parts) > 5:
                latitude = float(parts[3][:2]) + float(parts[3][2:])/60
                if parts[4] == 'S':
                    latitude = -latitude
                longitude = float(parts[5][:3]) + float(parts[5][3:])/60
                if parts[6] == 'W':
                    longitude = -longitude
                self.last_known_position = {"latitude": latitude, "longitude": longitude}

    def get_location(self) -> Dict[str, Optional[float]]:
        return self.last_known_position

    def stop(self) -> None:
        self.ser.close()

class GPSPlotter(tk.Tk):
    def __init__(self, gps_tracker: GPSTracker) -> None:
        super().__init__()
        self.gps_tracker = gps_tracker
        self.title("GPS Tracker")
        
        self.fig, self.ax = plt.subplots(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        self.ax.set_title("GPS Location")
        self.ax.set_xlabel("Longitude")
        self.ax.set_ylabel("Latitude")
        
        self.update_plot()

    def update_plot(self) -> None:
        location = self.gps_tracker.get_location()
        lat = location["latitude"]
        lon = location["longitude"]

        self.ax.clear()
        self.ax.set_title("GPS Location")
        self.ax.set_xlabel("Longitude")
        self.ax.set_ylabel("Latitude")
        if lat is not None and lon is not None:
            self.ax.plot(lon, lat, 'ro')
        
        self.canvas.draw()
        
        self.after(1000, self.update_plot)

def main():
    gps_tracker = GPSTracker()
    app = GPSPlotter(gps_tracker)
    try:
        print("GPS Tracker started. Press Ctrl+C to stop.")
        app.mainloop()
    except KeyboardInterrupt:
        print("GPS Tracker stopped.")
    finally:
        gps_tracker.stop()

if __name__ == "__main__":
    main()
