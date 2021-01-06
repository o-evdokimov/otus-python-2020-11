import os

class BaseType(type):
    def __repr__(cls):
        print('### run basetype __repr__')
        return(f'{cls.name} : weight = {cls.weight} : carrying = {cls.carrying} : passengers = {cls.passengers}')

class Transport():
    name = 'transport'
    weight = 0
    carrying = 0
    beep = None

    def __init__(self, weight, carrying):
        print('### run base __init__')
        self.weight = weight
        self.carrying = carrying

    @classmethod
    def do_beep(cls):
        print(f'{cls.beep} beep...')
        code = os.system("afplay {}".format(cls.beep))
        if code==0: return True
        else: return False