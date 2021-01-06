from transport import Transport
from constants import Beeps, Passengers, Weight, Carrying, UNKNOWN_TRANSPORT

class Plane(Transport):
    name = 'Plane'
    beep = Beeps[name]
    weight = Weight.get('Plane')
    carrying = Carrying.get('Plane')
    aviacompany = None

    def __init__(self, weight, carrying):
        print('### run plane __init__')
        super().__init__(self.weight, self.carrying)

    # reloaded method
    def __repr__(self):
        print('### run truck __repr__')
        return (f'{self.name} : weight = {self.weight} : carrying = {self.carrying} : passengers = {self.passengers}')


class Boeing737(Plane):
    name = 'Boeing737'
    beep = Beeps[name]
    fuel = 20
    max_passengers = 120
    max_speed = 900
    weight = 27700
    carrying = 49400

    def __init__(self):
        print('### run Boeing737 __init__')
        # new attr for class
        super().__init__(self.weight, self.carrying)

    # reloaded method
    def __repr__(self):
        print('### run Boeing737 __repr__')
        return (f'{self.name} : passengers = {self.max_passengers} : max_speed = {self.max_speed}')

class Board(Boeing737):
    name = 'Board'
    def __init__(self, aviacompany, flight_number):
        print('### run Board __init__')
        self.aviacompany = aviacompany
        self.flight_number = flight_number
        # new attr for class
        super().__init__()

    def show_aviacompany(self):
        return self.aviacompany

    # reloaded method
    def __repr__(self):
        print('### run Board __repr__')
        return (f'{self.name} : aviacompany = {self.show_aviacompany()} : flight_number = {self.flight_number}')