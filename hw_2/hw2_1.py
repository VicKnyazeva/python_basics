# Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр. 
# Через строку нельзя решать.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def sum_of_digits(num):
    result = 0
    if num < 0:
        num = -num
    while num != 0:
        result += num % 10
        num //= 10
    return result


def task_1():
    input_value = input("Введите целое или вещественное число: ")

    num_arr = []
    result_sum = 0

    if is_number(input_value):
        num_arr = list(map(int, input_value.split(".")))

    if len(num_arr) == 0:
        print("Вы ввели не числовое значение")

    else:
        for e in num_arr:
            result_sum += sum_of_digits(e)

    print(f"Сумма цифр числа: {result_sum}")


task_1()
