a = int(input())
b = int(input())
c = int(input())
if a >= b and a >= c:
    if b >= c:
        (a, b, c) = (b, c, a)
        print(a, b, c)
    elif c >= b:
        (a, b, c) = (b, c, a)
        print(a, b, c)
elif b >= c and b >= a:
    if c >= a:
        (a, b, c) = (a, c, b)
        print(a, b, c)
    elif a >= c:
        (a, b, c) = (c, a, b)
        print(a, b, c)
elif c >= b and c >= a:
    if b >= a:
        (a, b, c) = (a, b, c)
        print(a, b, c)
    elif a >= b:
        (a, b, c) = (b, a, c)
        print(a, b, c)