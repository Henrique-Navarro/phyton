lanche= ('hamburguer', 'Suco', 'pizza', 'pudim')
#           [0]         [1]      [2]      [3]
print(lanche) 
print(lanche[1])

#segundo elemento do final ate o inicio
print(lanche[-2])
print(lanche[1:3])

#do primeiro ate o ultimo elemento
print(lanche[1:])

for comida in lanche:
    print(f'Vou comer {comida}')
print('Comi por bosta')

#ouu

for cont in range(0, len(lanche)):  
    print(f'Vou comer {lanche[cont]}')

#ouu

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

#ordem
print(sorted(lanche))
