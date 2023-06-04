# Вводится десятичное число. 
# Реализовать алгоритм его перевода в двоичную систему счисления через рекурсию. 
# Нельзя использовать функцию bin()

# *Пример:*
#     10
#     *Вывод:*
#     1010

A = int(input("Введите число: "))
list = []
def convert(n):
    if (n == 0):
        return list
    dig = n % 2
    list.append(dig)
    convert(n // 2)
convert(A)
list.reverse()
print("Двоичная форма числа: ")
for i in list:
    print(i)