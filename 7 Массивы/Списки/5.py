c = list(map(int, input().split()))
for i in range(1, len(c)):
    if c[i] > 0 and c[i - 1] > 0 or c[i] < 0 and c[i - 1] < 0: 
        print(c[i - 1], c[i])
        break
