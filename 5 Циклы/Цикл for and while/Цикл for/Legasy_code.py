N = int(input())
s = 1
while s <= N:
    s += 1
    if N % s == 0:
        break
if N % s == 0:
    print(1)
