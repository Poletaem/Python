# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию .split()

word = input("Введите строку: ").split()
result = {}             # слово сложили в словарь ключами
for i in word:          # 1.проходимся по каждому символу
    if i in result:     # 2.если i уже есть в словаре
        print(f'{i}_{result[i]}', end=' ')
    else:
        print(i, end=' ')
    result[i] = result.get(i, 0) + 1


    word = input("Введите строку: ").split()
result = {}
for i in word:
    if i in result:
        print(f'{i}_{result[i]}', end=' ')
        result[i] += 1
    else:
        print(i, end=' ')
        result[i] = 1