w = list(map(int, input().split()))
a = w[0]
s = 0
for i in range(1, len(w) - 1):
    if w[i] > w[i - 1] and w[i] > w[i + 1]:
        s += 1
    if i + 1 == len(w) - 1:
        break
print(s)
