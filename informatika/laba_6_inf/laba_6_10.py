n, k = map(int, input().split())

people = list(range(1, n + 1))
res = []
i = 0

while len(people) > 1:
    i = (i + k - 1) % len(people)
    res.append(people.pop(i))


print(*res)
print(people[0])
