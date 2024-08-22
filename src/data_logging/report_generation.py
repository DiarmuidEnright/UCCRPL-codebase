import sqlite3
import pandas as pd
from jinja2 import Environment, FileSystemLoader
import pdfkit
'''

class ReportGenerator:
    def __init__(self, db_path='flight_data.db'):
        self.conn = sqlite3.connect(db_path)
        self.env = Environment(loader=FileSystemLoader('templates'))

    def generate_report(self, flight_id):
        df = pd.read_sql_query(f"SELECT * FROM sensor_data WHERE flight_id={flight_id}", self.conn)
        template = self.env.get_template('report_template.html')
        html_report = template.render(data=df)
        pdfkit.from_string(html_report, f'flight_{flight_id}_report.pdf')

    def close(self):


'''

#Finish tomorrow