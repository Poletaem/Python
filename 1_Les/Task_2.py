# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.



countStudents1 = int(input("Введите кол-во учеников в 1-ом кабинете: "))
countStudents2 = int(input("Введите кол-во учеников в 2-ом кабинете: "))
countStudents3 = int(input("Введите кол-во учеников в 3-ом кабинете: "))
part = (countStudents1 // 2 + countStudents1 % 2) + (countStudents2 // 2 + countStudents2 % 2) + (countStudents3 // 2 + countStudents3 % 2)
print(part)

countStudents1 = int(input("Введите кол-во учеников в 1-ом кабинете: "))
countStudents2 = int(input("Введите кол-во учеников в 2-ом кабинете: "))
countStudents3 = int(input("Введите кол-во учеников в 3-ом кабинете: "))
part1 = (countStudents1 + 1) // 2
part2 = (countStudents2 + 1) // 2
part3 = (countStudents3 + 1) // 2
print(part1 + part2 + part3)