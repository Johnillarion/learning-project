a = int(input())
b = 'программистов'
c = 'программист'
d = 'программиста'
if a >= 0:
    if a == 0:
        print(a, b)
    elif a % 100 >= 10 and a % 100 <= 20:
        print(a, b)
    elif a % 10 == 1:
        print(a, c)
    elif a % 10 >= 2 and a % 10 <= 4:
        print(a, d)
    else:
        print(a, b)
