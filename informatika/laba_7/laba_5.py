nums = [12, -5, 0, 7, 18, -3, 9, 24, 6, 15]
even = list(filter(lambda x: x % 2 == 0, nums))
print(*even)
positive = list(filter(lambda x: x > 0, nums))
print(*positive)
pestrunchik = list(filter(lambda x: x % 3 == 0 and x > 5,nums))
print(*pestrunchik)