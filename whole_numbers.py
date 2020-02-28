a = int(input())
while a > 10 or a < 100:
    if a < 10:
        a = int(input())
        continue
    elif a > 100:
        break
    print(a)
    a = int(input())