a= int(input('Digite um numero: '))
b= int(input('Digite um numero: '))
c= int(input('Digite um numero: '))

if a<b and a<c:
    print(f'O menor é {a}')
if b<a and b<c:
    print(f'O menor é {b}')
if c<a and c<b:
    print(f'O menor é {c}')

if a>b and a>c:
    print(f'O maior é {a}')
if b>a and b>c:
    print(f'O maior é {b}')
if c>a and c>b:
    print(f'O maior é {c}')