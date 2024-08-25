#failsafe
ALTITUDE_THRESHOLD = 1000  # meters
CHECK_INTERVAL = 1  # seconds

# camera_capture
CAMERA_RESOLUTION = (1920, 1080)
CAMERA_FRAMERATE = 30
OUTPUT_DIR = "rocket_footage"
RECORDING_DURATION = 60

# flight model training
TEST_SIZE = 0.2 
RANDOM_STATE = 42

# database settings
DB_PATH = 'flight_data.db'

# failure condition settings
ALTITUDE_THRESHOLD = 500  #meters
SPEED_THRESHOLD = 10
