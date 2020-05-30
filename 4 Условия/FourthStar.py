N = int(input())
M = int(input())
x = int(input())
y = int(input())
if M > N:   
  print(min(x, y, N - x, M - y))
elif N > M:
    print(min(x, y, N - y, M - x))
