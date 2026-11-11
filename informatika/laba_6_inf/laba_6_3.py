heights = input()
heights = list(map(int,heights.split(' ')))
x = int(input())
heights.append(x)
heights = sorted(heights, reverse = True)
cnt = 0
for i in range(len(heights)-1):
    cnt += 1
    if heights[i] == x:
        if heights[i] == heights[i+1]:
            print(cnt+1)
        else:
            print(cnt)
        break