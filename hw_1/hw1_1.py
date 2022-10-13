
# задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

def task_1():
    print('====== Start Task 1 ======')

    try:
        input_value = input('Введите номер дня недели: ')
        day = int(input_value)
        check_day(day)
    except:
        print("Преобразование введенного значения не удалось")
    
    print('====== End Task 1 ========')

def check_day(day):
    if(type(day) == int and day > 0 and day <=7):
        if day == 7 or day == 6:
            print("Это выходной день")
        else:
            print("Это рабочий день")
    else:
        print('Это очень странное значение для дня недели')

task_1()
