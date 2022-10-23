# Задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

import math


def check_factor(factors_list, num, factor):
    degree = 0  # сколько раз factor делит num нацело

    while num % factor == 0:
        degree += 1
        num = num // factor

    if degree > 0:
        factors_list.append((factor, degree))

    return num


def prime_factors(number):
    factors_list = []

    num = check_factor(factors_list, number, 2)

    for factor in range(3, int(math.sqrt(num)) + 1, 2):
        num = check_factor(factors_list, num, factor)

    if num > 2:
        factors_list.append((num, 1))

    return factors_list


def calc_and_print_prime_factors(number):
    factors_list = prime_factors(number)

    print(number, "= ", end='')
    prefix = ''
    for factor, degree in factors_list:
        print(prefix, end='')
        if degree == 1:
            print(factor, end='')
        else:
            print(factor, '^', degree, end='', sep='')
        prefix = ' + '
    print()


calc_and_print_prime_factors(2)
calc_and_print_prime_factors(16)
calc_and_print_prime_factors(27)
calc_and_print_prime_factors(36 * 5)
calc_and_print_prime_factors(271)
calc_and_print_prime_factors(272)
