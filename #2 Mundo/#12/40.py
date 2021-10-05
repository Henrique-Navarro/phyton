nota1= float(input('Digite a primeira nota: '))
nota2= float(input('Digite a segunda nota: '))
med= (nota1+nota2)/2

if med<5:
    print('reprovado')
if med>5 and med<6.9:
    print('recuperation')
if med>7:
    print('parabens espertão')