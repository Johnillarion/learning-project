# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление
# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!"

a = float(input())
b = float(input())
c = input()
if  c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == 'pow':
    print(pow(a,b))
elif c == '/':
    if b != 0:
        print(a / b)
    else:
        print('Деление на 0!')
elif c == 'div':
    if b != 0:
        print(a // b)
    else:
        print('Деление на 0!')
elif c == 'mod':
    if b != 0:
        print(a % b)
    else:
        print('Деление на 0!')












# print('Деление на 0!')
