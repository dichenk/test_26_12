import random
import copy

'''
Реализуйте алгоритм, который принимает массив 
и перемещает нули в конец, 
сохраняя порядок остальных элементов
'''
mass = [random.randint(0, 4) for x in range(20)]
print(mass)
for index, item in enumerate(mass):
    if item == 0:
        del mass[index]
        mass.append(0)
print(mass)

'''
2. Посчитайте сумму n-го ряда пирамиды нечетных чисел (начало с 1)
    #     1
    #    3 5
    #   7 9 11
    # 13 15 17 19
    #21 23 25 27 29
    #...
'''
n = int(input('input n: '))
amount = int(n*(n-1) / 2) ## чисел во всех предыдущих рядах
result = [x for x in range(amount * 2 + 1, amount * 2 + n * 2, 2)] ## искомый ряд
result = sum(result)
print(result)
