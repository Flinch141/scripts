words = ["яблоко", "кот", "программирование", "дом", "молоко"]
students = [("Аня", 20), ("Борис", 18), ("Вера", 22), ("Глеб", 19)]
nums = [33, 12, 45, 21, 8, 99]
print(sorted(words,key = lambda x: len(x)))
print(sorted(students, key = lambda x: x[1]))
print(sorted(nums, key = lambda x: x % 10))