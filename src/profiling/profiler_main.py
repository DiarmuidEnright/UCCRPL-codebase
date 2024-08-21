import cProfile
import pstats
from sensor_motor_dashboard import SensorMotorDashboard

def main():
    dashboard = SensorMotorDashboard()
    dashboard.mainloop()

if __name__ == "__main__":
    cProfile.run('main()', 'profiling_results')
    with open('profiling_stats.txt', 'w') as f:
        p = pstats.Stats('profiling_results', stream=f)
        p.sort_stats('cumulative').print_stats(10)
