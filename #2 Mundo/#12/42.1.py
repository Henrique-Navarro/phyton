a= int(input('Digite o lado 1: '))
b= int(input('Digite o lado 2: '))
c= int(input('Digite o lado 3: '))

if a< b+c and b< a+c and c< a+b:
    print('podem formar triangulo')
    if a==b==c:
        print('equilatero')
    elif a != b != c and a != c:
        print('escaleno')
    else:
        print('isosceles')
else:
    print('não é possivel')