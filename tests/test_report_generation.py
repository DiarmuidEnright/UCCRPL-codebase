import unittest
import os
from report_generation import ReportGenerator

class TestReportGenerator(unittest.TestCase):
    def setUp(self) -> None:
        self.db_path = ":memory:"
        self.report_gen = ReportGenerator(db_path=self.db_path)
        self.report_path = 'test_report.pdf'
        self.report_gen.cursor.execute("""
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
        self.report_gen.conn.commit()
        self.report_gen.cursor.execute("""
        INSERT INTO sensor_data (flight_id, timestamp, altitude, speed, acceleration_x, acceleration_y, acceleration_z, gyro_x, gyro_y, gyro_z, temperature)
        VALUES (1, strftime('%s','now'), 1000, 300, 9.8, 0, 0, 0.1, 0.2, 0.3, 25)""")
        self.report_gen.conn.commit()

    def test_generate_report(self) -> None:
        self.report_gen.generate_report(1)
        self.assertTrue(os.path.exists(self.report_path))
        os.remove(self.report_path)

    def tearDown(self) -> None:
        self.report_gen.close()

if __name__ == '__main__':
    unittest.main()
