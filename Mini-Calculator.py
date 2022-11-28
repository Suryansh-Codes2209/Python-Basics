a = input('Enter First Number:')
op = input('Enter operator (+,-,%,/,*):')
b = input('Enter First Number:')
a=int(a)
b=int(b)

if op == '+':
    print(a+b)
elif op == '-':
    print(a-b)
elif op == '*':
    print(a*b)
elif op == '/':
    print(a/b)
elif op == '%':
    print(a%b)
else:
    print('Chutiye No. ya operator toh enter kara')