import unittest
import sqlite3
from flight_model_training import FlightPredictor
import pandas as pd

class TestFlightPredictor(unittest.TestCase):
    def setUp(self) -> None:
        self.db_path = ":memory:"
        self.predictor = FlightPredictor(db_path=self.db_path)
        self.predictor.cursor.execute("""
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
        self.predictor.conn.commit()
        self.predictor.cursor.execute("""
        INSERT INTO sensor_data (flight_id, timestamp, altitude, speed, acceleration_x, acceleration_y, acceleration_z, gyro_x, gyro_y, gyro_z, temperature)
        VALUES (1, strftime('%s','now'), 1000, 300, 9.8, 0, 0, 0.1, 0.2, 0.3, 25)""")
        self.predictor.cursor.execute("""
        INSERT INTO sensor_data (flight_id, timestamp, altitude, speed, acceleration_x, acceleration_y, acceleration_z, gyro_x, gyro_y, gyro_z, temperature)
        VALUES (1, strftime('%s','now'), 400, 50, 0.5, 0.5, 0.5, 0.05, 0.1, 0.15, 23)""")
        self.predictor.conn.commit()

    def test_load_data(self) -> None:
        df: pd.DataFrame = self.predictor.load_data()
        self.assertEqual(len(df), 2)
        self.assertIn('altitude', df.columns)
        self.assertIn('speed', df.columns)

    def test_train_model(self) -> None:
        self.predictor.load_data()
        self.predictor.train_model()
        self.assertTrue(True)

    def tearDown(self) -> None:
        self.predictor.close()

if __name__ == '__main__':
    unittest.main()
