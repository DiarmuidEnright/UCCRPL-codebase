import unittest
import sqlite3
from analysis import DataAnalyzer
from pandas import DataFrame

class TestDataAnalyzer(unittest.TestCase):
    def setUp(self) -> None:
        self.db_path: str = ":memory:"
        self.analyzer: DataAnalyzer = DataAnalyzer(db_path=self.db_path)
        self.analyzer.cursor.execute("""
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
        self.analyzer.conn.commit()
        self.analyzer.cursor.execute("""
        INSERT INTO sensor_data (flight_id, timestamp, altitude, speed, acceleration_x, acceleration_y, acceleration_z, gyro_x, gyro_y, gyro_z, temperature)
        VALUES (1, strftime('%s','now'), 1000, 300, 9.8, 0, 0, 0.1, 0.2, 0.3, 25)""")
        self.analyzer.conn.commit()

    def test_get_flight_data(self) -> None:
        df: DataFrame = self.analyzer.get_flight_data(1)
        self.assertEqual(len(df), 1)
        self.assertEqual(df['altitude'][0], 1000)

    def tearDown(self) -> None:
        self.analyzer.close()

if __name__ == '__main__':
    unittest.main()
