#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
#10 -> 1 2 4 8


n = int(input("Введите число: "))
a = 2
while a < n:
    print (a, end=' ')
    a *= 2


#n = int(input())
#i = 0
#while 2 ** i <= n:
    #print(2 ** i)
    #i += 1    //Более адекватное решение
