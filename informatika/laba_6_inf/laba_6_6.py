card = input()
total = 0
for i in range(len(card)):
    d = int(card[i])
    if i % 2 == 0:       
        d *= 2
        if d > 9:
            d -= 9
    total += d
print('Yes' if total % 10 == 0 else 'NOT')