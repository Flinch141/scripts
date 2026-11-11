def func(x):
    return x ** 2 / 10 + 1
N = 10
while N != 100000:
    
    a, b = -2, 5
    h = (b - a) / N

    values = []
    for i in range(N):
        x_i = a + i * h
        values.append(func(x_i))

    S = 0
    
    for v in values:
        S += v * h
    
    print(N,f"S = {S:.2f}")
    N *= 10