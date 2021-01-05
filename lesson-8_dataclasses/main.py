"""
1. написать базовый класс для средства передвижения, определить у него общие свойства. Например, вес, грузоподъемность.
Определить общие методы, например “издать звук”

2. сделать несколько наследников класса. Например: корабль, автомобиль, самолёт. Перегрузить у них методы, чтобы
соответствовать классу. Также добавить свойства, относящиеся к классу: водоизмещение, количество колёс, предельная высота и т.д.
базовые классы могут быть реализованы асбстрактными классами при помощи модуля abc

3. создать более конкретные классы. Например: “легковой автомобиль”, “парусная лодка” и тд.
Перегрузить общие свойства, а также добавить дополнительные свойства и методы

4. разнести все классы и исключения в отдельные модули

5. добавить методы, которые принимают параметры

6. добавить в инициализатор и другие методы классов выкидывание исключения при передаче неподходящих аргументов,
или не выполнении других внутренних условий (например, если бак пустой, то при попытке “завести” ТС
будет выкинуто исключение, что недостаточно топлива)
можно создать вспомогательные объекты при помощи датаклассов. Например, объект “двигатель”, у которого есть несколько свойств:
литраж, количество поршней, максимальное количество оборотов… на ваш выбор

7. сделать главный модуль, при запуске которого выполняется демонстрация работы всех классов (красивые принты приветствуются)
"""

# Imports
import os
from pathlib import Path
#from abc import ABC, abstractmethod

# Constants

UNKNOWN_TRANSPORT = 'Unknown'
LIB_DIR = Path(__file__).resolve().parent.joinpath('audio')
os.chdir(LIB_DIR)

Beeps = {
    'Car' : 'car.mp3',
    'Plane' : 'plane.mp3',
    'Truck' : 'truck.mp3',
    UNKNOWN_TRANSPORT : 'unknown.mp3'
}
Passengers = {
    'Car' : 4,
    'Plane' : 90,
    'Truck' : 2,
    UNKNOWN_TRANSPORT : None
}
Weight = {
    'Car' : 1.5,
    'Plane' : 10,
    'Truck' : 5,
    UNKNOWN_TRANSPORT : None
}
Carrying = {
    'Car' : 3,
    'Plane' : 5,
    'Truck' : 8,
    UNKNOWN_TRANSPORT : None
}

#1
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


class Truck(Transport):
    name = 'Truck'
    beep = Beeps[name]

    def __init__(self, weight, carrying, passengers):
        print('### run truck __init__')
        self.weight = weight
        self.carrying = carrying
        # new attr for class
        self.passengers = passengers

    # reloaded method
    def __repr__(self):
        print('### run truck __repr__')
        return (f'{self.name} : weight = {self.weight} : carrying = {self.carrying} : passengers = {self.passengers}')


# MAIN
if __name__ == "__main__":
    print('\n>> Create @classmethod classes:\n')
    transport_list = [k for k in Beeps.keys() if k is not UNKNOWN_TRANSPORT]
    print('You may select transport: ', transport_list)
    cls_name = input('Input your transport: ')
    if cls_name not in transport_list: cls_name = UNKNOWN_TRANSPORT

    ## use @classmethod decorator
    cls_params = {
        'name': cls_name,
        'beep': Beeps.get(cls_name),
        'weight': Weight.get(cls_name),
        'carrying': Carrying.get(cls_name),
        'passengers': Passengers.get(cls_name)}
    cls = BaseType(cls_name, (Transport,), cls_params)
    print(cls)
    cls.do_beep()
    ###

### use vanille classes
    print('\n\n>> Now create vanille class:\n')
    t = Truck(4,14, Passengers.get('Truck'))
    print(t)
    t.do_beep()
###


