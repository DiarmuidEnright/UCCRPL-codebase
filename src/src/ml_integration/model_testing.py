from rocketpy import Environment, SolidMotor, Rocket, Flight
import datetime

'''
Environment setup
'''
env = Environment(latitude=51.89291, longitude=-8.49289, elevation=13)
tomorrow = datetime.date.today() + (datetime.timedelta(days = 1))
env.set_date((tomorrow.year, tomorrow.month, tomorrow.day, 12))
env.set_atmospheric_model(type = "Forecast", file = "GFS")
env.all_info()

