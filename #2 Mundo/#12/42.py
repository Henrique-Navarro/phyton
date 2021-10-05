a= int(input('Digite o lado 1: '))
b= int(input('Digite o lado 2: '))
c= int(input('Digite o lado 3: '))
e=0
if a< (b+c):
    if b< (a+c):
        if c< (b+a):
            print('Pode se construir um triangulo com os lados {},{},{}' .format(a,b,c))
            e= e+1
        else:
            print('Não é possível contruir um triangulo')
    else:
        print('Não é possível contruir um triangulo')
else:
    print('Não é possível contruir um triangulo')

if e==1:
    if a==b and b==c:
        print('equilatero')
    elif a==b or b==c or c==a:
        print('isosceles')
    elif a!=b and b!=c and a!=c:
        print('escaleno')
else:
    print('Não é possível contruir um triangulo')