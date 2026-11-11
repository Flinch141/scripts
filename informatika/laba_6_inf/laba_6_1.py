from random import*
lst = [randint(1,49) for x in range(7)]
while len(lst) != len(set(lst)):
    lst = [randint(1,49) for x in range(7)]
print(*lst)


print(sample(range(1, 49), 6))