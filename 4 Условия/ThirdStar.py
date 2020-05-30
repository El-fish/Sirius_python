x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
# 1
if x1 + 1 == x2 and y1 + 2 == y2:
    print("YES")
# 2
elif x1 + 2 == x2 and y1 + 1 == y2:
    print("YES")
# 3
elif x1 + 2 == x2 and y1 - 1 == y2:
    print ("YES")
# 4
elif x1 + 1 == x2 and y1 - 2 == y2:
    print ("YES")
# 5
elif x1 - 1 == x2 and y1 - 2 == y2:
    print ("YES")
# 6
elif x1 - 2 == x2 and y1 - 1 == y2:
    print("YES")
# 7
elif x1 - 2 == x2 and y1 + 1 == y2:
    print("YES")
# 8
elif x1 - 1 == x2 and y1 + 2 == y2:
    print ("YES")
else:
    print("NO")
