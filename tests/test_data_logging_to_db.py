import unittest
import sqlite3
from data_logging_to_db import DataLogger

class TestDataLogger(unittest.TestCase):
    def setUp(self):
        self.db_path = ":memory:"
        self.logger = DataLogger(db_path=self.db_path)
        self.flight_id = 1
        self.logger.cursor.execute("""
        CREATE TABLE sensor_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            flight_id INTEGER,
            timestamp TIMESTAMP,
            altitude REAL,
            speed REAL,
            acceleration_x REAL,
            acceleration_y REAL,
            acceleration_z REAL,
            gyro_x REAL,
            gyro_y REAL,
            gyro_z REAL,
            temperature REAL
        )""")
        self.logger.conn.commit()

    def test_log_sensor_data(self):
        sensor_data = {
            'altitude': 1000.0,
            'speed': 300.0,
            'acceleration_x': 9.8,
            'acceleration_y': 0.0,
            'acceleration_z': 0.0,
            'gyro_x': 0.1,
            'gyro_y': 0.2,
            'gyro_z': 0.3,
            'temperature': 25.0
        }
        self.logger.log_sensor_data(self.flight_id, sensor_data)
        self.logger.cursor.execute("SELECT * FROM sensor_data")
        row = self.logger.cursor.fetchone()
        self.assertIsNotNone(row)
        self.assertEqual(row[1], self.flight_id)
        self.assertAlmostEqual(row[3], sensor_data['altitude'])
        self.assertAlmostEqual(row[4], sensor_data['speed'])

    def tearDown(self):
        self.logger.close()

if __name__ == '__main__':
    unittest.main()
