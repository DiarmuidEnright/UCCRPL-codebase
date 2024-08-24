import sqlite3
import time
from sensor_data import get_sensor_readings
from typing import Dict, Any

class DataLogger:
    def __init__(self, db_path: str = 'flight_data.db') -> None:
        self.conn: sqlite3.Connection = sqlite3.connect(db_path)
        self.cursor: sqlite3.Cursor = self.conn.cursor()

    def log_sensor_data(self, flight_id: int, sensor_data: Dict[str, Any]) -> None:
        timestamp: float = time.time()
        query: str = """INSERT INTO sensor_data (flight_id, timestamp, altitude, speed, acceleration_x, acceleration_y, acceleration_z, gyro_x, gyro_y, gyro_z, temperature)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        self.cursor.execute(query, (
            flight_id,
            timestamp,
            sensor_data['altitude'],
            sensor_data['speed'],
            sensor_data['acceleration_x'],
            sensor_data['acceleration_y'],
            sensor_data['acceleration_z'],
            sensor_data['gyro_x'],
            sensor_data['gyro_y'],
            sensor_data['gyro_z'],
            sensor_data['temperature']
        ))
        self.conn.commit()

    def log_event(self, flight_id: int, event_type: str, description: str) -> None:
        timestamp: float = time.time()
        query: str = """INSERT INTO events (flight_id, timestamp, event_type, description)
                        VALUES (?, ?, ?, ?)"""
        self.cursor.execute(query, (flight_id, timestamp, event_type, description))
        self.conn.commit()

    def close(self) -> None:
        self.conn.close()

if __name__ == "__main__":
    logger = DataLogger()
    flight_id: int = 1

    try:
        while True:
            sensor_data: Dict[str, Any] = get_sensor_readings()
            logger.log_sensor_data(flight_id, sensor_data)
            time.sleep(1)
    except KeyboardInterrupt:
        logger.close()
