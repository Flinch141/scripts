n = 3
lst = [1,2,3,4,5,6,7,8,9,0]

def window(n,lst):
    res = []

    for i in range(len(lst)-n+1):
        res.append(tuple(lst[i:i+n]))

    return res
print(window(n,lst))
    