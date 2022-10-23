# Задача 2. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

num_list = [5, 1, 2, 3, 4, 5, 2, 2, 4, 5, 6]
print("Исходный список значений:", num_list)
print()

# строим отображение (число -> количество вхождений в список)

num_dict = {}
for n in num_list:
    count = num_dict.get(n)
    if count is None:
        num_dict[n] = 1
    else:
        num_dict[n] = count + 1

# строим результирующие способом 1

list_of_unique = []
list_of_single = []
for n, count in num_dict.items():
    list_of_unique.append(n)
    if count == 1:
        list_of_single.append(n)

print("Список уникальных значений:", list_of_unique)
print("Список неповторяющихся значений:", list_of_single)
print()

# строим результирующие способом 2

list_of_unique = list(map(lambda e: e[0], num_dict.items()))
list_of_single = list(map(lambda e: e[0], filter(lambda e: e[1] == 1, num_dict.items())))

print("Список уникальных значений:", list_of_unique)
print("Список неповторяющихся значений:", list_of_single)
print()
