import os
from constants import FuelError
from abc import ABC, abstractmethod

class BaseType(type):
    type = 'base_transport_meta'
    weight = 0
    carrying = 0
    beep = None
    fuel_filling = None

    def send_start_msg(self):
        print(f'{self.name} starts, passengers = {self.passengers} ...')

    def __repr__(cls):
        print(f'### run {cls.__class__} __repr__')
        return(f'*** {cls.type} : weight = {cls.weight} : carrying = {cls.carrying} : passengers = {cls.passengers}')

    @classmethod
    def start(cls, cls_instanse):
        if cls_instanse.check_ready():
            print(f'Start {cls_instanse.name}...')
            cls_instanse.send_start_msg()
            code = os.system("afplay {}".format(cls_instanse.beep))
            if code==0:
                return True
            else:
                return False
        else:
            raise FuelError('Fuel is not filled. Start is not possible.')

    @classmethod
    def refuel(cls):
        cls.fuel_filling = True

    def check_ready(self):
        if self.fuel_filling:
            return True
        raise FuelError(f'{self.__class__} is not ready')

class Transport(ABC):
    type = 'base_transport'
    weight = 0
    carrying = 0
    beep = None
    fuel_filling = None

    def __init__(self):
        print('### run base __init__')

    @abstractmethod
    def check_ready(self):
        pass

    @classmethod
    def start(cls, cls_instanse):
        print(f'Start {cls_instanse.name}...')
        if cls_instanse.check_ready():
            cls_instanse.send_start_msg()
            code = os.system("afplay {}".format(cls_instanse.beep))
            if code==0:
                return True
            else:
                return False
        else:
            raise FuelError('Fuel is not filled. Start is not possible.')

    def refuel(self):
        self.fuel_filling = True