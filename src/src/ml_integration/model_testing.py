from rocketpy import Environment, SolidMotor, Rocket, Flight
from google.colab import files
import datetime

#Environment setup

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

rocket = Rocket(
    radius=106 / 2000,
    mass=5.109,
    inertia=(3.8 , 3.8, 0.01),

    power_off_drag = "DragOffCSV.csv",

    power_on_drag = "DragOnCSV.csv",

    center_of_mass_without_motor=86.7 / 100,

    coordinate_system_orientation="tail_to_nose"
)

rail_buttons = rocket.set_rail_buttons(
    upper_button_position=0.618,
    lower_button_position=0.230,
    angular_position=45,
)

rocket.add_motor(PRO75L645, position=0)

nose_cone = rocket.add_nose(length=0.484, kind="vonKarman", position=1.77)

fin_set = rocket.add_trapezoidal_fins(
    n=3, #fin num
    root_chord=0.25,
    tip_chord=0.098,
    span=0.15,
    position=0.32,
    cant_angle=0,
    airfoil=("AirfoilDegreesCSV.csv", "degrees"),
)

tail = rocket.add_tail(
    top_radius = 106 / 2000,
    bottom_radius=0.04,
    length=0.07,
    position=0.07
)

rocket.all_info()


Main = rocket.add_parachute(
    "Main",
    cd_s = 1.0,
    trigger = 200,
    sampling_rate = 105,
    lag = 1.5,
    noise = (0, 8.3, 0.5),
)

Drogue = rocket.add_parachute(
    "Drogue",
    cd_s = 0.313,
    trigger = "apogee",
    sampling_rate = 105,
    lag = 1.5,
    noise = (0, 8.3, 0.5),
)

#simulating a flight

test_flight = Flight(
    rocket=rocket,
    environment=env,
    rail_length=4,
    inclination=70,
    heading = 170
)

test_flight.all_info()

from google.colab import files

test_flight.export_kml(
    file_name="Trajectory.kml",
    extrude=True,
    altitude_mode="relative_to_ground",
)

files.download('Trajectory.kml')