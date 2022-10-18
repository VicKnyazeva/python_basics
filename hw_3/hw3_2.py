# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

def print_list(input_list):
    print(f"Исходный список: {input_list}")


def pairs_multiply(input_list):
    i = 0
    j = len(input_list) - 1
    new_list = []

    while i <= j:
        ni = input_list[i]
        nj = input_list[j]
        new_list.append(ni * nj)

        i += 1
        j -= 1

    print(f"Произведение пар чисел: {new_list}", end=" ")


def task2_1():
    print("Test 1")
    input_list = [2, 3, 4, 5, 6]
    print_list(input_list)
    pairs_multiply(input_list)

    print("\n\nTest 2")
    input_list = [2, 3, 5, 6]
    print_list(input_list)
    pairs_multiply(input_list)


task2_1()
