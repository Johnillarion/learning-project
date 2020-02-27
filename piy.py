a = int(input())
b = int(input())
c = a
d = b
while a % c == 0 and b % d == 0:
    c += a
    d += b
    print(c, d)
