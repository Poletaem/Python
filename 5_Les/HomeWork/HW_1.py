#  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 


A = int(input("Введите число: "))
B = int(input("Введите степень числа: "))

def pov(A, B):
    if B == 1:
        return A             Лучше поставить точку остановки if b == 0: return 1 так как a^0 = 1(любое число в степени 0 равно 1)
    return A * pov(A, B - 1)
print(pov(A, B))

