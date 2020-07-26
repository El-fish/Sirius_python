s = input()
s = s.replace("h", "H")
s = s.replace("H", "h", 1)
s = s[::-1]
s = s.replace("H", "h", 1)
s = s[::-1]
print(s)
