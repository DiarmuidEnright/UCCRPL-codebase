from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import sqlite3

class FlightPredictor:
    def __init__(self, db_path='flight_data.db'):
        self.conn = sqlite3.connect(db_path)

    def load_data(self):
        query = """SELECT altitude, speed, acceleration_x, acceleration_y, acceleration_z, gyro_x, gyro_y, gyro_z, temperature
                   FROM sensor_data"""
        df = pd.read_sql_query(query, self.conn)
        df['failure'] = (df['altitude'] < 500) & (df['speed'] < 10)
        return df

    def train_model(self):
        df = self.load_data()
        X = df.drop('failure', axis=1)
        y = df['failure']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        model = RandomForestClassifier()
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Model Accuracy: {accuracy:.2f}")

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    predictor = FlightPredictor()
    predictor.train_model()
    predictor.close()
