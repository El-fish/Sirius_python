#all minutes
n = int(input())
#часы
hours = n // 60
MinInHour = hours * 60
#minutes
minutes = n - MinInHour
print(hours, minutes)