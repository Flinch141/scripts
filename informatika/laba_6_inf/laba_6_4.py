from random import*
i = 0
j = 0
cnt = 0
while i != 3 or j != 3:
    cnt += 1
    per = randint(1,2)
    if per == 1:
        i += 1
        j = 0
    else:
        j += 1
        i = 0
    print(per,end = '')
    if i == 3 or j == 3:
        break
print(" попыток: ",cnt)