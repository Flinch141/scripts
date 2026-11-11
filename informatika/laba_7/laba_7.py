students = [
    ("Аня", 5), ("Борис", 3), ("Вера", 4),
    ("Глеб", 5), ("Дина", 2), ("Егор", 4),
    ("Жанна", 5), ("Зоя", 3)
]
students = list(filter(lambda x: x[1] > 3,students))
students = sorted(students,key = lambda x: x[1],reverse = True)
sredniy_ball = sum([students[x][1] for x in range(len(students))]) / len(students)
print(*students,sredniy_ball)