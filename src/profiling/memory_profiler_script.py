from memory_profiler import profile
from sensor_data import process_sensor_data

@profile
def profiled_process_sensor_data():
    process_sensor_data()

if __name__ == "__main__":
    profiled_process_sensor_data()

#mprof run memory_profiler_script.py
#mprof plot