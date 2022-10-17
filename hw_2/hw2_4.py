# Задача 4 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу, которая принимает на вход N,
# и координаты двух точек и находит расстояние между ними в N-мерном пространстве.

import math

def task_4():
    try:
        dimension = int(input(f"Введите размерность пространства: "))
        print()
        point1 = []
        for i in range(0, dimension):
            point1.append(float(input(f"Введите {i+1} координату первой точки: ")))

        print()
        point2 = []
        for i in range(0, dimension):
            point2.append(float(input(f"Введите {i+1} координату второй точки: ")))

        calculate_distance(point1, point2)

    except:
        print("Преобразование введенных значений не удалось")


def calculate_distance(point1, point2):
    dim = len(point1)
    sqr = 0
    for i in range(dim):
        sqr += math.pow(point1[i] - point2[i], 2)

    res = math.sqrt(sqr)

    print(f"\nРасстояние между двумя точками в {dim}-мерном пространстве: {res}")

task_4()