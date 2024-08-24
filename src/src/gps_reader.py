import serial
import time
from gps import gps, WATCH_ENABLE, WATCH_NEWSTYLE
from typing import Optional, Dict

gps_port: serial.Serial = serial.Serial('/dev/serial0', baudrate=9600, timeout=1)
session: gps = gps(mode=WATCH_ENABLE | WATCH_NEWSTYLE)

def read_gps() -> None:
    report: Optional[Dict[str, float]] = session.next()
    
    if report and report.get('class') == 'TPV':
        lat: Optional[float] = report.get('lat')
        lon: Optional[float] = report.get('lon')
        
        if lat is not None and lon is not None:
            print(f"Latitude: {lat}, Longitude: {lon}")

while True:
    read_gps()
    time.sleep(1)
