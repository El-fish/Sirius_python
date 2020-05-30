n = int(input())
d3 = n % 10
d2 = n // 10 % 10
d1 = n // 100 % 10
d99 = n // 100 % 1000
d0 = d99 // 10 % 10
print(d0 + d1 + d2 + d3)