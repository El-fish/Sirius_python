i = int(input())
t = int(input())
v = 4
if i > t:
    v = 1
elif t > i:
    v = 2
elif t == i:
    v = 0
print (v)