from math import (sqrt,pow)

ca= float(input('Digite o valor do cateto adjacente '))
co= float(input('Digite o valor do cateto opsoto '))

h= sqrt((pow(ca,2) + pow(co,2)))

print(f'Hipotenusa vale: {h :.2f}')
