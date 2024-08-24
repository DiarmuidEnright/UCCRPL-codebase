import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from typing import List, Tuple

class DataAnalyzer:
    def __init__(self, db_path: str = 'flight_data.db') -> None:
        self.conn: sqlite3.Connection = sqlite3.connect(db_path)

    def get_flight_data(self, flight_id: int) -> pd.DataFrame:
        query = """SELECT * FROM sensor_data WHERE flight_id = ?"""
        df: pd.DataFrame = pd.read_sql_query(query, self.conn, params=(flight_id,))
        return df

    def _plot_metric(self, df: pd.DataFrame, column: str, ylabel: str, title: str, subplot_position: Tuple[int, int]) -> None:
        plt.subplot(*subplot_position)
        plt.plot(df['timestamp'], df[column], label=column)
        plt.xlabel('Time')
        plt.ylabel(ylabel)
        plt.title(title)
        plt.legend()

    def plot_flight_data(self, flight_id: int) -> None:
        df: pd.DataFrame = self.get_flight_data(flight_id)
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')

        plt.figure(figsize=(14, 7))

        metrics: List[Tuple[str, str, str, Tuple[int, int]]] = [
            ('altitude', 'Altitude (m)', 'Altitude Over Time', (2, 2, 1)),
            ('speed', 'Speed (m/s)', 'Speed Over Time', (2, 2, 2)),
            ('acceleration', 'Acceleration (m/s²)', 'Acceleration Over Time', (2, 2, 3)),
            ('pressure', 'Pressure (Pa)', 'Pressure Over Time', (2, 2, 4))
        ]

        for column, ylabel, title, position in metrics:
            self._plot_metric(df, column, ylabel, title, position)

        plt.tight_layout()
        plt.show()

    def close_connection(self) -> None:
        self.conn.close()
