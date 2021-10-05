import math
#ou form math import sqrt, floor (mais especifico)

a= int(input('Digite um numero: '))
raiz = math.sqrt(a)
print(f'A raiz de {a} é: {raiz}')
print(f'2 casas decimais {a} é: {raiz :.2f}')
print(f'Arredondando pra cima {math.ceil(raiz)}')
print(f'Arredondando pra baixo {math.floor(raiz)}')