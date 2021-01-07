from transport import Transport
from constants import Beeps, InMove, Stopped

class Trucks(Transport):
    type = 'Trucks'
    beep = Beeps[type]

    def __init__(self, passengers, wheels):
        print('### run trucks __init__')
        # new attr for class
        self.passengers = passengers
        self.wheels = wheels
        super().__init__()

    def check_status(self):
        if check_gps(): self.status = InMove
        else: self.status = Stopped

    # reloaded method
    def __repr__(self):
        print('### run truck __repr__')
        return (f'{self.type} : weight = {self.weight} : carrying = {self.carrying} : passengers = {self.passengers}')


class Truck(Trucks):
    type = 'Truck'

    def __init__(self, number, passengers, wheels):
        print('### run truck __init__')
        self.number = number
        self.status = None
        super().__init__(passengers, wheels)

    def check_status(self):
        if self.check_gps(): self.status = InMove
        else: self.status = Stopped

    def check_gps(self):
        pass
        return True

    # reloaded method
    def __repr__(self):
        print('### run truck __repr__')
        return (f'{self.type} : number = {self.number} : status = {self.status} ')