from random import randint
from time import sleep

chute= int(input('Digite um numero: '))
rand= randint(0,5)
print(f'{rand}')

print('PROCESSANDO....')
sleep(3)

if rand == chute:
    print('Voce acertou o numero {}'.format(chute))
else:
    print('Voce errou o numero')