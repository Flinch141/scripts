stroka = input()
lst = stroka.split('/')
k = lst.pop(0)
k = int(k) - 1
res = []
for i in range(len(lst)):
    if len(lst[i]) > 10:
        res.append(lst[i][0] + str(len(lst[i][1:-1])) + lst[i][-1])
    else:
        res.append(lst[i])
for j in range(len(res)):
    if j < k:
        print(res[j],end='/')
    else: print(res[j])

