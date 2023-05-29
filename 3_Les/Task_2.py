# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [3, 4, 5, 1, 2]

# k = k % n

list_1 = [int(i) for i in input().split()]
step = int(input("Введите кол-во сдвигов: "))  #K
result_list = [list_1[i - step] for i in range(len(list_1))]
print(result_list)

list_1 = [int(i) for i in input("Введите числа: ").split()]
step = int(input("Введите кол-во сдвигов: "))
step = step % len(list_1)
result_list = list()    # указали тип данных (список)
for i in range(len(list_1)):
    result_list.append(list_1[i - step])   # добавили эл-ты в новый список
print(result_list)