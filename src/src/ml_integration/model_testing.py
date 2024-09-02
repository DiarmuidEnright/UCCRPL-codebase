from rocketpy import Environment, SolidMotor, Rocket, Flight
from settings.py import thrust_source
import datetime


'''
Environment setup
'''
env = Environment(latitude=51.89291, longitude=-8.49289, elevation=13)
tomorrow = datetime.date.today() + (datetime.timedelta(days = 1))
env.set_date((tomorrow.year, tomorrow.month, tomorrow.day, 12))
env.set_atmospheric_model(type = "Forecast", file = "GFS")
env.all_info()

PRO75L645 = SolidMotor(
    thrust_source="Cesaroni_3419L645-P.eng",
    dry_mass=1.607, 
    dry_inertia=(0.039, 0.039, 0.0015), 
    nozzle_radius = 37.5 / 1000, 
    grain_number=3, 
    grain_density=1815,
    grain_outer_radius = 37.5 / 1000, 
    grain_initial_inner_radius=29 / 1000,
    grain_initial_height=157 / 1000,
    grain_separation=5 / 1000,
    grains_center_of_mass_position=0.343,
    center_of_dry_mass_position=0.231,
    nozzle_position = 0.0,
    burn_time=5.3,
    throat_radius=12.5 / 1000,
    coordinate_system_orientation="nozzle_to_combustion_chamber"
)