# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
# 1 2 3 4 5
# 6
# -> 5

from random import randint


n = int(input('Введите количество элементов: '))
list_1 = [randint(1, 10) for i in range(n)]
print(list_1)
X = int(input('Введите число: '))
delta = abs(X - list_1[0])
min = list_1[0]
for i in range(1, n):
    dif = abs(X - list_1[i]) 
    if dif <= delta:
        delta = dif
        min = list_1[i]
print(f'Ближе всего к указанному числу {min}')



n = int(input("Введите кол-во элементов: "))
array = [int(i) for i in input("Введите значения массива: ").split()] 
x = int(input("Введите число, которое нужно подсчитать: "))
count = x - array[0]
if count < 0:
    count *= (-1)
numbers = array[0]
for el in range(1, n):
    temp = x - array[el]
    if temp < 0:
        temp *= (-1)
    if count > temp:
        count = temp
        numbers = array[el]
print(numbers)


n = int(input("Введите кол-во элементов: "))
array = [int(i) for i in input("Введите значения массива: ").split()] 
x = int(input("Введите число, которое нужно подсчитать: "))
count = abs(x - array[0])
numbers = array[0]
for el in range(1, n):
    temp = abs(x - array[el])
    if count > temp:
        count = temp
        numbers = array[el]
print(numbers)
    
