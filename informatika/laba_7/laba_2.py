def func(x):
    return x ** 2 / 10 + 1
 
 
def trapezoids(a, b, n):
    h = (b - a) / n
    s = (func(a) + func(b)) / 2
    for i in range(1, n):
        s += func(a + i * h)
    return s * h
 
 
a, b = -2, 5
 
for n in (10, 100, 1000, 10000):
    s = trapezoids(a, b, n)
    print(f"{'N=' + str(n) + ':':<9}{s:.2f}")

 