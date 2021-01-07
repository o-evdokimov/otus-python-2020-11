import os
from constants import Beeps, Passengers, Weight, Carrying, UNKNOWN_TRANSPORT

class BaseType(type):
    def __repr__(cls):
        print('### run basetype __repr__')
        return(f'{cls.type} : weight = {cls.weight} : carrying = {cls.carrying} : passengers = {cls.passengers}')

class Transport():
    type = 'transport'
    weight = 0
    carrying = 0
    beep = None

    def __init__(self):
        print('### run base __init__')

    @classmethod
    def do_beep(cls):
        print(f'{cls.beep} beep...')
        code = os.system("afplay {}".format(cls.beep))
        if code==0: return True
        else: return False