CREATE TABLE flights (
    flight_id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    mission_name TEXT,
    rocket_id INTEGER
);

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
    temperature REAL,
    FOREIGN KEY(flight_id) REFERENCES flights(flight_id)
);

CREATE TABLE events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    flight_id INTEGER,
    timestamp TIMESTAMP,
    event_type TEXT,
    description TEXT,
    FOREIGN KEY(flight_id) REFERENCES flights(flight_id)
);
