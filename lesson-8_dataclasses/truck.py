from transport import Transport
from constants import Beeps, InMove, Stopped
from dataclasses import dataclass


class Trucks(Transport):
    type = 'Truck'
    beep = Beeps[type]

    def __init__(self, passengers):
        print(f'### run {self.__class__} __init__')
        # new attr for class
        self.passengers = passengers
        super().__init__()

    def check_status(self):
        if check_gps(): self.status = InMove
        else: self.status = Stopped

    # reloaded method
    def __repr__(self):
        print(f'### run {self.__class__} __repr__')
        return (f'{self.type} : weight = {self.weight} : carrying = {self.carrying} : passengers = {self.passengers}')


class Truck(Trucks):
    type = 'Truck'
    name = 'Truck'
    def __init__(self, number, passengers, route):
        print(f'### run {self.__class__} __init__')
        self.number = number
        self.route = route
        self.status = None
        super().__init__(passengers)

    def check_status(self):
        if self.check_gps(): self.status = InMove
        else: self.status = Stopped

    def check_gps(self):
        pass
        return True

    def send_start_msg(self):
        print(f'{self.name} by number {self.number} starts from {self.route.source} to {self.route.destination}...')

    # reloaded method
    def __repr__(self):
        print(f'### run {self.__class__} __repr__')
        return (f'{self.type} : number = {self.number} : status = {self.status} ')


@dataclass
class Route:
    source: str = None
    destination: str = None

