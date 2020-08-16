a = list(map(int, input().split()))
c = []
for i in range(0, len(a)):
    if a[i] % 2 == 0:
        c.append(a[i])
c = map(str, c)
print(" ".join(c))