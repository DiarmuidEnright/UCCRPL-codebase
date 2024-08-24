from line_profiler import LineProfiler
from sensor_motor_dashboard import SensorMotorDashboard
from sensor_data import process_sensor_data
from typing import Any

def main() -> None:
    dashboard: SensorMotorDashboard = SensorMotorDashboard()
    dashboard.mainloop()

if __name__ == "__main__":
    profile: LineProfiler = LineProfiler()
    profile.add_function(process_sensor_data)
    profile.run('main()')
    profile.print_stats(output_unit=1e-3)
