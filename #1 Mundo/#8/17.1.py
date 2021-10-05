import math
ca= float(input('Digite o valor do cateto adjacente '))
co= float(input('Digite o valor do cateto opsoto '))
hi= math.hypot(co,ca)
print('valor da hipotenusa é: {:.2f}'. format(hi))