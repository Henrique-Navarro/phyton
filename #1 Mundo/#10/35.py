a= int(input('Digite o lado 1: '))
b= int(input('Digite o lado 2: '))
c= int(input('Digite o lado 3: '))

if a< (b+c):
    if b< (a+c):
        if c< (b+a):
            print('Pode se construir um triangulo com os lados {},{},{}' .format(a,b,c))
        else:
            print('Não é possível contruir um triangulo')
    else:
        print('Não é possível contruir um triangulo')
else:
    print('Não é possível contruir um triangulo')