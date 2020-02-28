number_ticket = input()
a = int(number_ticket[0])
b = int(number_ticket[1])
c = int(number_ticket[2])
d = int(number_ticket[3])
e = int(number_ticket[4])
f = int(number_ticket[5])

if a + b + c == d + e + f:
    print('Счастливый')
else:
    print('Обычный')