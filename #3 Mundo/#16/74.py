from random import randint
tupla=(randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print(tupla)
maior=menor=tupla[0]
n=0
while n<5:
    if tupla[n]>maior:
        maior= tupla[n]
    if tupla[n]<menor:
        menor= tupla[n]
    n+=1
print(f'O maior: {maior} o menor: {menor}')