n = int(input())
s = 0
prev = int(input())
for i in range(n - 1):
    a = int(input())
    s += a * prev
    prev = a
print(s)