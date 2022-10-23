# Задача 3. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random


def init_poly(k, max_c):
    poly = []

    for degree in range(0, k + 1):
        c = random.randrange(0, max_c + 1)
        if c != 0:
            poly.insert(0, (degree, c))
    return poly


superscript_numbers = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']


def degree_string(degree):
    match degree:
        case 0:
            return superscript_numbers[0]
        case 1:
            return ''
        case _:
            result = ''
            while degree > 0:
                digit = degree % 10
                degree //= 10
                result = superscript_numbers[digit] + result

    return result


def poly_to_string(poly):
    result = ''
    separator = ''

    for n, c in poly:
        result += separator
        if c > 1 or n == 0:
            result += f"{c}"
        if n > 0:
            result += "x" + degree_string(n)
        separator = ' + '

    if separator != '':
        if len(poly) == 1 and poly[0][0] == 0 and poly[0][1] != 0:
            result += ' != 0'
        else:
            result += ' = 0'

    return result


def poly_to_file(file_name, k, max_c):
    poly_string = poly_to_string(init_poly(k, max_c))
    print(poly_string)
    with open(file_name, 'a', encoding='utf-8') as output_file:
        output_file.write(poly_string)
        output_file.write("\n")


max_c = 100
poly_to_file('file.txt', 1, max_c)
poly_to_file('file.txt', 3, max_c)
poly_to_file('file.txt', 20, max_c)
