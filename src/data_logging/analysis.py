import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from typing import Optional

class DataAnalyzer:
    def __init__(self, db_path: str = 'flight_data.db') -> None:
        self.conn: sqlite3.Connection = sqlite3.connect(db_path)

    def get_flight_data(self, flight_id: int) -> pd.DataFrame:
        query = """SELECT * FROM sensor_data WHERE flight_id = ?"""
        df: pd.DataFrame = pd.read_sql_query(query, self.conn, params=(flight_id,))
        return df

    def plot_flight_data(self, flight_id: int) -> None:
        df: pd.DataFrame = self.get_flight_data(flight_id)
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
        plt.plot(df['timestamp'], df['acceleration'], label="Acceleration")
        plt.xlabel('Time')
        plt.ylabel('Acceleration (m/s²)')
        plt.title('Acceleration Over Time')

        plt.subplot(2, 2, 4)
        plt.plot(df['timestamp'], df['pressure'], label="Pressure")
        plt.xlabel('Time')
        plt.ylabel('Pressure (Pa)')
        plt.title('Pressure Over Time')

        plt.tight_layout()
        plt.show()

    def close_connection(self) -> None:
        self.conn.close()
