# задача 4 необязательная Даны два многочлена. Задача - сформировать их сумму.
# например, 5*x^3 + 2*x^2 + 6 и 7*x^2+6*x+3 , Тогда их сумма будет равна 5*x^3 + 9*x^2 + 6*x + 9

import random

superscript_numbers = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
degree_map = {}
for i in range(0, len(superscript_numbers)):
    degree_map[superscript_numbers[i]] = i


def init_poly(k):
    poly = []

    for degree in range(0, k + 1):
        c = random.randrange(0, 101)
        if c != 0:
            poly.insert(0, (degree, c))
    return poly


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


def poly_to_file(file_name, poly):
    poly_string = poly_to_string(poly)
    print(poly_string)
    with open(file_name, 'w', encoding='utf-8') as output_file:
        output_file.write(poly_string)


def parse_number(str, start):
    # print('\tNUM', str[start:], end='|')
    number = None
    buffer = ''
    position = start
    for c in str[position:]:
        if number == None and c.isspace():
            position += 1
            continue
        if c == 'x':
            if buffer == '':
                number = 1
            else:
                number = int(buffer)
            break
        if c.isdigit():
            buffer += c
            position += 1
        else:
            number = int(buffer)
            break
    return (position, number)


def parse_degree(str, start):
    # print('\tDEG', str[start:], end='|')
    if str[start] != 'x':
        return (start, 0)

    number = None
    position = start + 1
    for c in str[position:]:
        if number == None and c.isspace():
            position += 1
            continue
        digit = degree_map.get(c)
        if digit != None:
            if number == None:
                number = digit
            else:
                number = number * 10 + digit
            position += 1
        else:
            if number == None:
                number = 1
            break;

    return (position, number)


def parse_op(str, start):
    # print('\tOP ', str[start:], end='|')
    number = None
    buffer = 0
    position = start
    for c in str[position:]:
        position += 1
        if c.isspace():
            continue
        if c == '=':
            return (position, False, None)  # прочитали всё
        if c == '+':
            return (position, True, None)  # есть ещё ...

        break

    return (position - 1, False, "Ожидался символ + или = ")  # есть ещё ...


def parse_poly(str):
    poly = []
    continue_parse = True
    pos = 0
    while (continue_parse):
        pos, c1 = parse_number(str, pos)
        pos, d1 = parse_degree(str, pos)
        poly.append((d1, c1))
        pos, continue_parse, err = parse_op(str, pos)
    poly.sort(key=lambda tup: tup[0], reverse=True)
    return poly


def poly_from_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as input_file:
        return parse_poly(input_file.read())


def sum_poly(p1, p2):
    result_poly = []
    i1 = 0
    i2 = 0
    while True:
        if i1 >= len(p1):
            if i2 >= len(p2):
                break;
            result_poly.append(p2[i2])
            i2 += 1
        elif i2 >= len(p2):
            if i1 >= len(p1):
                break;
            result_poly.append(p1[i1])
            i1 += 1
        else:
            d1, c1 = p1[i1]
            d2, c2 = p2[i2]
            if d1 == d2:
                result_poly.append((d1, c1 + c2))
                i1 += 1
                i2 += 1
            elif d1 < d2:
                result_poly.append((d2, c2))
                i2 += 1
            else:
                result_poly.append((d1, c1))
                i1 += 1

    return result_poly


poly_to_file('file1.txt', init_poly(2))
p1 = poly_from_file('file1.txt')

poly_to_file('file2.txt', init_poly(5))
p2 = poly_from_file('file2.txt')

print('---')
p3 = sum_poly(p1, p2)
poly_to_file('file3.txt', p3)
print('---')