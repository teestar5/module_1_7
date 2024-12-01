students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

sorted_students = sorted(students)    #сортируем студентов в алфавитном порядке вариант 1
print(sorted_students)

students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)
sorted_students_list = sorted(students_list)   #сортируем студентов в алфавитном порядке вариант 2

print(sorted_students_list)



avr = [5, 3, 3, 5, 4]
avr_ = sum(avr)/len(avr)

print(avr_)

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

print(grades[0])
print(grades[1])
print(grades[2])
print(grades[3])
print(grades[4])
# находим стреднеарифметическое
avr_A = sum(grades[0])/len(grades[0])
avr_B = sum(grades[1])/len(grades[1])
avr_J = sum(grades[2])/len(grades[2])
avr_K = sum(grades[3])/len(grades[3])
avr_S = sum(grades[4])/len(grades[4])



print(avr_A)
print(avr_B)
print(avr_J)
print(avr_K)
print(avr_S)

dict_avr = {}                 #выводим словарь
dict_avr["Aaron"] = avr_A
dict_avr["Bilbo"] = avr_B
dict_avr["Johnny"] = avr_J
dict_avr["Khendrik"] = avr_K
dict_avr["Steve"] = avr_S
print(dict_avr)