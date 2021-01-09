import os
from constants import FuelError

class BaseType(type):

    def send_start_msg(self):
        print(f'{self.name} starts, passengers = {self.passengers} ...')

    def __repr__(cls):
        print(f'### run {cls.__class__} __repr__')
        return(f'{cls.type} : weight = {cls.weight} : carrying = {cls.carrying} : passengers = {cls.passengers}')

class Transport():
    type = 'transport'
    weight = 0
    carrying = 0
    beep = None
    fuel_filling = None

    def __init__(self):
        print('### run base __init__')

    @classmethod
    def start(cls, cls_i):
        if cls.fuel_filling:
            print(f'Start {cls.name}...')
            cls_i.send_start_msg()
            code = os.system("afplay {}".format(cls.beep))
            if code==0:
                return True
            else:
                return False
        else:
            raise FuelError('Fuel is not filled. Start is not possible.')

    @classmethod
    def fuel_fill(cls):
        cls.fuel_filling = True