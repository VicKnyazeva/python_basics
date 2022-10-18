# Задача 3. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import math
import sys


def task3_1():
    input_list = [1.1, 1.2, 3.1, 5, 10.01]
    diff_fractional_value(input_list)


def diff_fractional_value(input_list):
    min_value = sys.float_info.max
    max_value = sys.float_info.min

    for i in input_list:
        fractional_part = i - math.trunc(i)
        # fractional_part, _ = math.modf(i)

        if min_value > fractional_part:
            min_value = fractional_part

        if max_value < fractional_part:
            max_value = fractional_part

    print(f"Максимальный и минимальный элементы:\n\t{max_value:+.17F}\n\t{min_value:+.17f}")
    print(f"Разница между максимальным и минимальным элементом:\n\t{max_value - min_value:+.17f}")


task3_1()
