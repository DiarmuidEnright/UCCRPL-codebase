from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import sqlite3

class FlightPredictor:
    def __init__(self, db_path: str = 'flight_data.db') -> None:
        self.conn: sqlite3.Connection = sqlite3.connect(db_path)

    def load_data(self) -> pd.DataFrame:
        query: str = """SELECT altitude, speed, acceleration_x, acceleration_y, acceleration_z, gyro_x, gyro_y, gyro_z, temperature
                        FROM sensor_data"""
        df: pd.DataFrame = pd.read_sql_query(query, self.conn)
        df['failure'] = (df['altitude'] < 500) & (df['speed'] < 10)
        return df

    def train_model(self) -> None:
        df: pd.DataFrame = self.load_data()
        X: pd.DataFrame = df.drop('failure', axis=1)
        y: pd.Series = df['failure']

        X_train: pd.DataFrame
        X_test: pd.DataFrame
        y_train: pd.Series
        y_test: pd.Series
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        model: RandomForestClassifier = RandomForestClassifier()
        model.fit(X_train, y_train)

        y_pred: pd.Series = model.predict(X_test)
        accuracy: float = accuracy_score(y_test, y_pred)
        print(f"Model Accuracy: {accuracy:.2f}")

    def close(self) -> None:
        self.conn.close()

if __name__ == "__main__":
    predictor = FlightPredictor()
    predictor.train_model()
    predictor.close()
