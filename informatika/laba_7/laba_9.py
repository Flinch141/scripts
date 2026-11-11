strings = int(input())
raws = int(input())

 
matrix = [[1] * raws]

for i in range(strings-1):
    matrix.append([0]*raws)

for i in range(strings):
    matrix[i][0] = 1

for s in range(1,strings):
    for r in range(1,raws):
        matrix[s][r] = matrix[s-1][r] + matrix[s][r-1]

for i in range(strings):
    print(*matrix[i])
