s = input()
s = list(map(int,s.split(' ')))
res = []
ind = []
for i in range(1,len(s)-1):
    if s[i-1] < s[i] > s[i+1]:
        res.append(s[i])
        ind.append(i)
s.remove(max(res))
print("Сакровища на индексах -> ",ind)
print("С такими значениями -> ",res)
print("Измененный список -> ",s)