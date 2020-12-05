# 1. написать функцию, которая принимает N целых чисел и возвращает список квадратов этих чисел.
#    Бонусом будет сделать keyword аргумент для выбора степени, в которую будут возводиться числа
#
# 2. написать функцию, которая на вход принимает список из целых чисел, и возвращает только чётные/нечётные/простые числа
#    (выбор производится передачей дополнительного аргумента)
#
# 3. создать декоратор для замера времени выполнения функции


#1
def power_list(init_list, N):
    res = []
    for item in init_list:
        res.append(item ** N)
    return res

#2
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

N = 2
my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print('init list: {}\n'. format(my_list))
print('возведение в степень {}: {}'.format(N, power_list(my_list, N)))
print('чётные числа: {}'.format(get_part_list(my_list, 0)))
print('НЕчётные числа: {}'.format(get_part_list(my_list, 1)))
print('простые числа: {}'.format(get_part_list(my_list, 2)))