kvdr = [[0] * 3 for i in range(3)]

s = 0
r = 1
kvdr[s][r] = 1

size = 3
n = 2

while n <= 9:
    new_s = (s - 1) % size
    new_r = (r + 1) % size

    if kvdr[new_s][new_r] == 0:
        s, r = new_s, new_r
    else:
        s = (s + 1) % size

    kvdr[s][r] = n
    n += 1

for i in range(size):
    for j in range(size):
        print(f'{kvdr[i][j]} ',end='')

    print('')

for i in range(len(kvdr)):
    print(sum(kvdr[i]))
