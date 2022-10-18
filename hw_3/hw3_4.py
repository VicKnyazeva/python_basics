# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное. Нельзя использовать готовые функции.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def task3_4():
    try:
        number = int(input("Введите число: "))
        convert_to_binary(number)
    except ValueError:
        print("Преобразование введенного числа не удалось")


def convert_to_binary(number):
    result = ""

    if number < 0:
        sign = "-";
        n = -number
    else:
        sign = ""
        n = number

    base = 2

    while n != 0:
        digit = n % base
        n //= base
        result = str(digit) + result

    print(f"{number} -> {sign}{result}")


task3_4()
