# задача 3. Напишите программу, которая принимает на вход координаты точки (X и Y), 
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

def task_3():
    print('====== Start Task 3 ======')

    try:
        coordinate_x = float(input('Введите координату X: '))
        coordinate_y = float(input('Введите координату Y: '))
        check_quarter(coordinate_x, coordinate_y)
    except:
        print("Преобразование введенных значений не удалось")

    print('====== End Task 3 ========')

def check_quarter(x, y):
    if(x > 0 and y > 0):
        print('Точка находится в I четверти')
    elif(x < 0 and y > 0):
        print('Точка находится во II четверти')
    elif(x < 0 and y < 0):
        print('Точка находится в III четверти')
    elif(x > 0 and y < 0):
        print('Точка находится в IV четверти')
    elif(x == 0 and y != 0):
        print('Точка находится на оси Y')
    elif(x != 0 and y == 0):
        print('Точка находится на оси X')
    else:
        print('Четверть не определена')

task_3()