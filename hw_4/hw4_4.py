# Найдите корни квадратного уравнения, уравнение вводит через строку пользователь.
# Например, 6*x^2+5*x+6=0 . Само собой, уравнение может и не иметь решения. Предусмотреть все варианты, сделать обработку исключений.

import cmath
import math


def input_coefficients():
    a = input('Введите значение a: ')
    b = input('Введите значение b: ')
    c = input('Введите значение c: ')

    try:
        a = float(a)
        if a == 0:
            print("Коэффициент 'a' не должен быть равен 0. Попробуйте еще раз.")
            return None
        b = float(b)
        c = float(c)
        return a, b, c
    except ValueError:
        print("Не удалось преобразовать введенные значения. попробуйте еще раз.")


def calc_equation(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    print('\nДискриминант = ' + str(discriminant))

    # example: a = 2 b = 4 c = -7
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print('\nКорни уравнения в действительных числах:')
        print('x₁ = ' + str(x1))
        print('x₂ = ' + str(x2))

    # example: a = 1 b = 6 c = 9
    elif discriminant == 0:
        x = -b / (2 * a)
        print('\nКорень уравнения в действительных числах')
        print('x = ' + str(x))

    # example: a = 2 b = 4 c = 7
    else:
        print('\nКорни уравнения в комплексных числах:')
        x1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        x2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        print('x₁ = ' + str(x1))
        print('x₂ = ' + str(x2))


def task4_4():
    print('Решаем уравнение вида a•x²+b•x+c=0')
    coefficients = input_coefficients()
    if coefficients is not None:
        calc_equation(coefficients[0], coefficients[1], coefficients[2])


task4_4()
