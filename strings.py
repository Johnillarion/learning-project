a = int(input())
b = int(input())
c = int(input())
if (a >= b and a >= c) and (b <= a and b >= c) and (c <= a and c <= b):
    print(a,'\n',b,'\n',c)
elif (b >= a and b >= c) and (a <= b and a >= c) and (c <= a and c <= b):
    print(b,'\n',a,'\n',c)
elif (c >= a and c >= b) and (b <= c and b >= a) and (a <= c and a <= b):
    print(c, '\n', b, '\n', a)

a-b-c,c-b-a,b-a-c,a-c-b,b-c-a,