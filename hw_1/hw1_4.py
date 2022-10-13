# задача 4.Напишите простой калькулятор, который считывает с пользовательского ввода три строки: 
# первое число, второе число и операцию, после чего применяет операцию к введённым числам 
# ("первое число" "операция" "второе число") и выводит результат на экран.
# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.
# 
# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
# Обратите внимание, что на вход программе приходят вещественные числа.

def task_4():
    print('====== Start Task 4 ======')

    try:
        number1 = float(input('Введите первое число: '))
        number2 = float(input('Введите второе число: '))
        operation = input('Введите операцию над числами: ')

        calculate(number1, operation, number2)
    except:
        print("Преобразование введенных значений не удалось")
        
    print('====== End Task 4 ========')

def calculate(num1, operation, num2):
    if(operation == '+'):
        print(f"{num1} + {num2} = {num1 + num2}")

    elif(operation == '-'):
        print(f"{num1} - {num2} = {num1 - num2}")

    elif(operation == '/'):
        if(num2 != 0):
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Деление на 0!")

    elif(operation == '*'):
        print(f"{num1} * {num2} = {num1 * num2}")

    elif(operation == 'mod'):
        if(num2 != 0):
            print(f"{num1} mod {num2} = {num1 % num2}")
        else:
            print("Деление на 0!")

    elif(operation == 'pov'):
        print(f"{num1} pov {num2} = {num1 ** num2}")

    elif(operation == 'div'):
        if(num2 != 0):
            print(f"{num1} div {num2} = {num1 // num2}")
        else:
           print("Деление на 0!")

    else:
        print("Выполнить вычисления не удалось")

task_4()


