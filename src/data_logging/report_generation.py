import sqlite3
import pandas as pd
from jinja2 import Environment, FileSystemLoader, Template
import pdfkit

class ReportGenerator:
    def __init__(self, db_path: str = 'flight_data.db') -> None:
        self.conn: sqlite3.Connection = sqlite3.connect(db_path)
        self.env: Environment = Environment(loader=FileSystemLoader('templates'))

    def generate_report(self, flight_id: int) -> None:
        df: pd.DataFrame = pd.read_sql_query(f"SELECT * FROM sensor_data WHERE flight_id={flight_id}", self.conn)
        template: Template = self.env.get_template('report_template.html')
        html_report: str = template.render(data=df)
        pdfkit.from_string(html_report, f'flight_{flight_id}_report.pdf')

    def close(self) -> None:
        self.conn.close()

if __name__ == "__main__":
    report_gen = ReportGenerator()
    report_gen.generate_report(1)
    report_gen.close()

#buh

class ReportAnalyzer:
    def __init__(self, db_path: str = 'flight_data.db') -> None:
        self.conn: sqlite3.Connection = sqlite3.connect(db_path)

    def analyze_report(self, flight_id: int) -> None:
        df: pd.DataFrame = pd.read_sql_query(f"SELECT * FROM sensor_data WHERE flight_id={flight_id}", self.conn)
        # Perform some analysis on the data
        print(df.describe())

    def close(self) -> None:
        self.conn.close()

    def process_report(self, flight_id: int) -> None:
        self.analyze_report(flight_id)
        report_gen = ReportGenerator()
        report_gen.generate_report(flight_id)
        report_gen.close()



class something():
    def __init__(self):
        self.random()

    def do_something(self):
        pass

    def do_something_else(self):
        pass

    def __str__():
        return "something"

something().do_something()