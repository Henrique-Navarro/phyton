import random
import time
itens=('Pedra','Papel','Tesoura')
cpu= random.randint(0,2)
print(f'{cpu}')
op=int(input('0- Pedra\n1- Papel\n2- Tesoura\n'))
print('Processando...')
time.sleep(1)

if cpu==0:
    if op==0:
        print('empate')
    elif op==1:
        print('voce venceu')
    elif op==2:
        print('voce perdeu')
    else:
        print('invalido')

if cpu==1:
    if op==0:
        print('empate')
    elif op==1:
        print('voce venceu')
    elif op==2:
        print('voce perdeu')
    else:
        print('invalido')

if cpu==2:
    if op==0:
        print('empate')
    elif op==1:
        print('voce venceu')
    elif op==2:
        print('voce perdeu')
    else:
        print('invalido')