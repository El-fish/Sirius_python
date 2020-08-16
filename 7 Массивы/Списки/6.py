c = list(map(int, input().split()))
a = 1000
for i in range(len(c)):
    if c[i] > 0 and c[i] <= a:
        a = c[i]
print(a)