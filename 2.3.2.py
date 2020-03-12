a = int(input())
b = int(input())
c = 0
d = 0

for i in range(a, b + 1):
    if i % 3 == 0:
        c += i
        i += 1
print(i / c)
