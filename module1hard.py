grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort() # Сортировка по алфавиту
gr1 = sum(grades[0]) / len(grades[0]) # Решил ввести дополнительные переменные, так проще отслеживать, меньше ошибок.
gr2 = sum(grades[1]) / len(grades[1])
gr3 = sum(grades[2]) / len(grades[2])
gr4 = sum(grades[3]) / len(grades[3])
gr5 = sum(grades[4]) / len(grades[4])
dict_students = {students[0]: gr1, students[1]: gr2, students[2]: gr3, students[3]: gr4, students[4]: gr5}
print('Средний балл: ', dict_students)
