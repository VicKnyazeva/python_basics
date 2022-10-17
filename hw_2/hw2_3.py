# Задача 3. Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

def task_3():
    s1 = input("Введите строку, в которой будем искать: ")
    s2 = input("Введите строку, которую будем искать: ")

    counter = 0
    str_length = len(s1)
    search_str_length = len(s2)

    for cur_index in range(str_length - search_str_length + 1):
        if s1[cur_index:cur_index + search_str_length] == s2:
            counter += 1

    print(f"Количество вхождений строки '{s2}' в первую строку: {counter}")


task_3()
