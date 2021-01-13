from pathlib import Path

UNKNOWN_TRANSPORT = 'Unknown'
INMOVE = 'In Move'
STOPPED = 'Stopped'
LIB_DIR = Path(__file__).resolve().parent.joinpath('audio')

class FuelError(BaseException):
    pass

# use constants for database simulation
Beeps = {
    'Car' : 'car.mp3',
    'Plane' : 'plane.mp3',
    'Truck' : 'truck.mp3',
    'Boeing737': 'boeing737.mp3',
    UNKNOWN_TRANSPORT : 'unknown.mp3'
}
Passengers = {
    'Car' : 4,
    'Plane' : 90,
    'Truck' : 2,
    UNKNOWN_TRANSPORT : None
}
Weight = {
    'Car' : 1500,
    'Plane' : 20000,
    'Truck' : 5000,
    UNKNOWN_TRANSPORT : None
}
Carrying = {
    'Car' : 3000,
    'Plane' : 40000,
    'Truck' : 8000,
    UNKNOWN_TRANSPORT : None
}
