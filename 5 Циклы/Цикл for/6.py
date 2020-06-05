A = int(input())
B = int(input())
for c in range(A + A % 2, B + 1, 2):
    print(c)