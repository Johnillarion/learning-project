st = str(input())
if st == 'прямоугольник':
    a = float(input())
    b = float(input())
    print(float(a * b))
elif st == 'круг':
    a = float(input())
    c = 3.14
    d = (c * a) * a
    print(float(d))
elif st == 'треугольник':
    x = float(input())
    y = float(input())
    z = float(input())
    p = (x + y + z) / 2
    S = p * ((p - x) * (p - y) * (p - z))
    print(float(pow(S, 0.5)))

