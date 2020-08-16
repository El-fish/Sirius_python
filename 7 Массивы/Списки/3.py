s = list(map(int, input().split()))
a = []
for i in range(len(s)):
    if i % 2 == 0:
        a.append(str(s[i]))
print(" ".join(a))