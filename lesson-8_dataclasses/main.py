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

# my modules
from transport import BaseType, Transport
from plane import Board
from truck import Truck
from constants import Beeps, Passengers, Weight, Carrying, UNKNOWN_TRANSPORT

# Constants

LIB_DIR = Path(__file__).resolve().parent.joinpath('audio')
os.chdir(LIB_DIR)


# MAIN
if __name__ == "__main__":
    print('################################')
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
    print('################################')
    cls.do_beep()
    ###

### use vanille classes
    print('\n\n>> Now create vanille class:\n')
    ###
    print('################################')
    truck_number = 'K2804UZ'
    t = Truck(truck_number, Passengers.get('Trucks'), 6)
    t.check_status()
    print(t)
    print('################################')
    t.do_beep()
    ###
    input('Press ENTER to continue...')
    ##
    print('################################')
    flight_number = 'UK9212'
    b = Board('S7', flight_number, 'DOMODEDOVO')
    print(b)
    print("\n>> Change Board's binding:\n")
    new_flight_number = 'KS5521'
    airport = 'VNUKOVO'
    b.change_binding((new_flight_number, airport))
    print(b)
    print('################################')
    b.do_beep()

###


