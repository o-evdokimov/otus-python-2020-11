from transport import Transport
from constants import Beeps, Passengers, Weight, Carrying, UNKNOWN_TRANSPORT

class Plane(Transport):
    type = 'Plane'
    beep = Beeps[type]
    aviacompany = None

    def __init__(self):
        print(f'### run {self.__class__} __init__')
        weight = self.get_data().get('weight')
        carrying = self.get_data().get('carrying')
        if isinstance(self.weight, int) and isinstance(self.carrying, int):
            if not self.weight and not self.carrying:
                self.weight = weight
                self.carrying = carrying
        else:
            raise ValueError(f"Invalid parameters for {self.__class__}")
        super().__init__()

    def get_data(self):
        print(f'Class Type: {self.type}')
        weight = Weight.get(self.type)
        carrying = Carrying.get(self.type)
        return {'weight': weight, 'carrying': carrying}

    # reloaded method
    def __repr__(self):
        print(f'### run {self.__class__} __repr__')
        return (f'{self.type} : weight = {self.weight} : carrying = {self.carrying} : passengers = {self.passengers}')


class Boeing737(Plane):
    name = 'Boeing737'
    type = 'Plane'
    beep = Beeps[type]
    fuel = 20
    max_passengers = 120
    max_speed = 900
    weight = 0
    carrying = 0

    def __init__(self):
        print('### run Boeing737 __init__')
        super().__init__()

    # reloaded method
    def __repr__(self):
        print(f'### run {self.__class__} __repr__')
        return (f'{self.name} : passengers = {self.max_passengers} : max_speed = {self.max_speed}')

class Board(Boeing737):
    name = 'Board'
    def __init__(self, aviacompany, flight_number, airport):
        print('### run Board __init__')
        self.aviacompany = aviacompany
        self.flight_number = flight_number
        self.airport = airport
        super().__init__()

    def change_binding(self, new_binding):
        self.flight_number, self.airport = new_binding

    def show_aviacompany(self):
        return self.aviacompany

    def send_start_msg(self):
        print(f'start {self.flight_number} from {self.airport} by {self.aviacompany}...')

    # reloaded method
    def __repr__(self):
        print(f'### run {self.__class__} __repr__')
        print(f'{self.weight} {self.carrying}')
        return (f'{self.name} : aviacompany = {self.show_aviacompany()} : flight_number = {self.flight_number} : airport = {self.airport}')