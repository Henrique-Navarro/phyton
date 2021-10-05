n1= float(input('Digite a nota 1: '))
n2= float(input('Digite a nota 2: '))
media = (n1+n2)/2

print(f'Sua media foi: {media}')

if media <6:
    print('estude mais')
else:
    print('sua nota está boa')

print('PARABENS' if media >6 else 'ESTUDE MAIS')