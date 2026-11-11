s = input()
nm = list(map(int,s.split()))

lst = []

for i in range(nm[0]):
    s = input()
    lst.append(list(map(int,s.split())))

n = int(input())
ans = 0

for i in range(len(lst)):
    cnt = 0
    for seat in lst[i]:
        if seat == 0:
            cnt += 1
        else:
            cnt = 0
        if cnt == n:
            ans = i + 1
            break
    if ans:
        break

print(ans)
    