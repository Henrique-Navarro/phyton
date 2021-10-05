from random import randint
tupla=(randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
for n in tupla:
    print(f'{n}', end=' ')
print(f'\nO maior: {max(tupla)}')
print(f'O menor: {min(tupla)}')