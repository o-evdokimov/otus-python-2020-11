from transport import Transport
from constants import Beeps, Passengers, Weight, Carrying, UNKNOWN_TRANSPORT

class Truck(Transport):
    name = 'Truck'
    beep = Beeps[name]
    weight = Weight.get('Truck')
    carrying = Carrying.get('Truck')

    def __init__(self, passengers, wheels):
        print('### run truck __init__')
        # new attr for class
        self.passengers = passengers
        self.wheels = wheels
        super().__init__(self.weight, self.carrying)

    # reloaded method
    def __repr__(self):
        print('### run truck __repr__')
        return (f'{self.name} : weight = {self.weight} : carrying = {self.carrying} : passengers = {self.passengers}')