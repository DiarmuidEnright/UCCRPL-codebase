import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

class DataAnalyzer:
    def __init__(self, db_path='flight_data.db'):
        self.conn = sqlite3.connect(db_path)

    def get_flight_data(self, flight_id):
        query = """SELECT * FROM sensor_data WHERE flight_id = ?"""
        df = pd.read_sql_query(query, self.conn, params=(flight_id,))
        return df

    def plot_flight_data(self, flight_id):
        df = self.get_flight_data(flight_id)
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
        
        plt.figure(figsize=(14, 7))

        plt.subplot(2, 2, 1)
        plt.plot(df['timestamp'], df['altitude'], label="Altitude")
        plt.xlabel('Time')
        plt.ylabel('Altitude (m)')
        plt.title('Altitude Over Time')

        plt.subplot(2, 2, 2)
        plt.plot(df['timestamp'], df['speed'], label="Speed")
        plt.xlabel('Time')
        plt.ylabel('Speed (m/s)')
        plt.title('Speed Over Time')

        plt.subplot(2, 2, 3)
        plt.plot(df['timestamp'], df['acceleration_x'], label="Accel X")
        plt.plot(df['timestamp'], df['acceleration_y'], label="Accel Y")
        plt.plot(df['timestamp'], df['acceleration_z'], label="Accel Z")
        plt.xlabel('Time')
        plt.ylabel('Acceleration (m/s^2)')
        plt.title('Acceleration Over Time')
        plt.legend()

        plt.subplot(2, 2, 4)
        plt.plot(df['timestamp'], df['gyro_x'], label="Gyro X")
        plt.plot(df['timestamp'], df['gyro_y'], label="Gyro Y")
        plt.plot(df['timestamp'], df['gyro_z'], label="Gyro Z")
        plt.xlabel('Time')
        plt.ylabel('Angular Velocity (deg/s)')
        plt.title('Gyroscope Over Time')
        plt.legend()

        plt.tight_layout()
        plt.show()

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    analyzer = DataAnalyzer()
    analyzer.plot_flight_data(1)
    analyzer.close()
