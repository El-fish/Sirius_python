a = int(input())
if a > 9:
    b = a % 10
    c = a % 100
    v = c - b 
    n = v // 10
    print(n)
else: 
    print(0)