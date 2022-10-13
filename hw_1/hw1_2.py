
# задача 2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def task_2():
    print('====== Start Task 2 ======')

    bool_array = [ False, True ]

    for X in bool_array:
        for Y in bool_array:
            for Z in bool_array:
                print('(', X, ',', Y, ',', Z, ') = ', check_predicate(X, Y, Z))

    print('====== End Task 2 ========')

def check_predicate(X, Y, Z):
    left = not(X and Y and Z)
    right = (not X) or (not Y) or (not Z)
    return left == right

task_2()