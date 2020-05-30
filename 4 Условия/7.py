a = int(input())
# последняя цифра
t = a % 10
# последние две цифры
v = a % 100
# вторая цифра
b = v // 10
if b == 1:
    print(a, "bochek")
elif b != 1:
    if t == 1:
        print(a, "bochka")
    elif t >= 2 and t <= 4:
        print(a, "bochki")
    elif t >= 5 and t <= 9 or t == 0:
        print(a, "bochek")