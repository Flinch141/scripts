n = int(input("Количество сокровищ: "))

lst = []
koor_alex = []
for i in range(n):
    s = input('Координаты сокровищ: ')
    lst.append(list(map(int,s.split())))

s = input("Где саня? ")
koor_alex = list(map(int,s.split()))

ranges = []
for i in range(n):
    x,y = lst[i][0],lst[i][1]
    xa,ya = koor_alex[0],koor_alex[1]

    x -= xa
    y -= ya

    ranges.append(round(((x ** 2 + y ** 2) ** 0.5),2))

print("Ближайшее сокровище:",*lst[ranges.index(min(ranges))])
print(min(ranges))
