# 1.
    # 1. написать функцию, которая принимает N целых чисел и возвращает список квадратов этих чисел.
    #    Бонусом будет сделать keyword аргумент для выбора степени, в которую будут возводиться числа
    #
    # 2. написать функцию, которая на вход принимает список из целых чисел, и возвращает только чётные/нечётные/простые числа
    #    (выбор производится передачей дополнительного аргумента)
    #
    # 3. создать декоратор для замера времени выполнения функции

# 2.
    # 1. создать декоратор, который показывает вложенные входы в функцию. Применить на примере вычисления чисел Фибоначчи

import re
from datetime import datetime
from functools import wraps
from functools import partial

#1.3
def time_interval(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        t1 = datetime.now()
        result = fn(*args, **kwargs)
        t2 = datetime.now()
        print('Время выполнения функции {} = {}'.format(fn.__name__, str(t2-t1)))
        return result
    return wrapper

#1.1
@time_interval
def power_list(init_list, n = 2):
    res = []
    for item in init_list:
        res.append(item ** n)
    return res

@time_interval
def power_list_map(init_number, n = 2):
    def apply(number):
        return number**n
    return list(map(apply, init_number))

#1.2
def get_part_list(init_list, filter_type):
    res = []
    for item in init_list:
        if filter_type=='even':
            if item % 2 == 0:
                res.append(item)
        elif filter_type == 'odd':
            if item % 2 != 0:
                res.append(item)
        elif filter_type=='simple':
            simple = True
            if item > 0:
                for i in range(2, item):
                    if item % i == 0:
                        simple = False
                        break
                if simple:
                    res.append(item)
    return res

def get_filter_list(filter_type, item):
    if filter_type=='even':
        if item % 2 == 0:
            return True
    elif filter_type == 'odd':
        if item % 2 != 0:
            return True
    elif filter_type=='simple':
        simple = True
        if item > 0:
            for i in range(2, item):
                if item % i == 0:
                    simple = False
                    break
            if simple:
                return True

#2.1
def trace(fn):
    @wraps(fn)
    def wrapper(*args):
        x, depth = args[0], args[1]
        print('{} {}({}) ->'.format('.' * 4* depth, fn.__name__, x).strip())
        result = fn(*args)
        print('{} {}({}) <- {}'.format('_' * 4*depth, fn.__name__, x, result).strip())
        return result
    return wrapper


@trace
def fib(x, depth):
    depth+=1
    if x>=0 and x<=1: return x
    return fib(x-1, depth) + fib(x-2, depth)


# MAIN

N = int(input('Введите степень числа: '))
my_list = list(map(int, re.split(',| ', input('Введите массив чисел(через запятую или пробел): ').strip())))

print('возведение в степень {}: {}'.format(N, power_list(my_list, N)))
print('возведение в степень {}: {}  <- функция {} с map: '.format(N, power_list_map(my_list, N), power_list_map.__name__))

FILTER_TYPE='even'
print('чётные числа: {}'.format(get_part_list(my_list, FILTER_TYPE)))
print('чётные числа (via filter): {}'.format(list(filter(partial(get_filter_list, FILTER_TYPE), my_list))))

FILTER_TYPE='odd'
print('НЕчётные числа: {}'.format(get_part_list(my_list, FILTER_TYPE)))
print('НЕчётные числа (via filter): {}'.format(list(filter(partial(get_filter_list, FILTER_TYPE), my_list))))

FILTER_TYPE='simple'
print('простые числа: {}'.format(get_part_list(my_list, FILTER_TYPE)))
print('простые числа (via filter): {}'.format(list(filter(partial(get_filter_list, FILTER_TYPE), my_list))))

X = int(input('Введите индекс для ряда Фибоначчи: '))
print('\nЧисло Фибоначчи для индекса "{}" = {}'.format(X, fib(X, 0)))