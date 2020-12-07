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

from datetime import datetime
from functools import wraps

DEPTH = 0

#1.3
def time_interval(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        t1 = datetime.now()
        result = fn(*args, **kwargs)
        t2 = datetime.now()
        print('Время выполнения функции {} = {}'.format(fn.__name__, t2-t1))
        return result
    return wrapper

#1.1
@time_interval
def power_list(init_list, n):
    res = []
    for item in init_list:
        res.append(item ** n)
    return res

#1.2
def get_part_list(init_list, A):
    res = []
    for item in init_list:
        if A==0:
            if item % 2 == 0:
                res.append(item)
        elif A==1:
            if item % 2 != 0:
                res.append(item)
        else:
            simple = True
            if item > 0:
                for i in range(2, item):
                    if item % i == 0:
                        simple = False
                        break
                if simple:
                    res.append(item)
    return res



N = int(input('Введите степень числа: '))
my_list = [int(x) for x in input('Введите массив чисел(через запятую или пробел): ').split()]
print(my_list)
#exit(13)
print('возведение в степень {}: {}'.format(N, power_list(my_list, N)))
print('чётные числа: {}'.format(get_part_list(my_list, 0)))
print('НЕчётные числа: {}'.format(get_part_list(my_list, 1)))
print('простые числа: {}'.format(get_part_list(my_list, 2)))

#2.1

def trace(fn):
    @wraps(fn)
    def wrapper(*args):
        #print('-> {}({})'.format(fib.__name__, *args))
        x, depth = args[0], args[1]

        print('{} {}({}) ->'.format('.' * 4* depth, fib.__name__, x).strip())
        result = fn(*args)
        #if depth==0: depth=1
        print('{} {}({}) <- {}'.format('_' * 4*depth, fib.__name__, x, result).strip())
        return result
    return wrapper


@trace
def fib(x, depth):
    depth+=1
    if x>=0 and x<=1: return x
    return fib(x-1, depth) + fib(x-2, depth)


# main

X = int(input('Введите индекс ряда Фибоначчи: '))
print('\nЧисло Фибоначчи для индекса "{}" = {}'.format(X, fib(X, 0)))