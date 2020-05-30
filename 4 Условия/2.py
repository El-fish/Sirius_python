k = int(input())
l = int(input())
m = int(input())
n = int(input())
if (k + l) % 2 == 0 and (m + n) % 2 == 0 or (k + l) % 2 != 0 and (m + n) % 2 != 0:
    print ("YES")
else:
    print ("NO")