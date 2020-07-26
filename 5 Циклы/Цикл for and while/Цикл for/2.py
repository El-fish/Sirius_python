A = int(input())
B = int(input())
if A > B:
    for V in range (A, B - 1, -1):
        print(V)
else:
    for G in range (A, B + 1, 1):
        print(G)