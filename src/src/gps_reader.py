import serial
import time
from gps import *

gps_port = serial.Serial('/dev/serial0', baudrate=9600, timeout=1)
session = gps(mode=WATCH_ENABLE | WATCH_NEWSTYLE)

def read_gps():
    report = session.next()
    if report['class'] == 'TPV':
        if hasattr(report, 'lat'):
            lat = report.lat
            lon = report.lon
            print(f"Latitude: {lat}, Longitude: {lon}")

while True:
    read_gps()
    time.sleep(1)

