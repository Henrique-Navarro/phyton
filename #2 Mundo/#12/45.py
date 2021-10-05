import random
import time
itens=('Pedra','Papel','Tesoura')
cpu= random.randint(0,2)
print(f'{cpu}')
op=int(input('0- Pedra\n1- Papel\n2- Tesoura\n'))
print('Processando...')
time.sleep(1)
if cpu==op:
    print('O coputador jogou {} e voce tambem' .format(itens[cpu]))
    print('Empate, ambos jogaram iguais')

elif cpu==0 and op==1:
    print('O coputador jogou {}' .format(itens[cpu]))
    print('Voce jogou {} '.format(itens[op]))
    print('Voce ganhou!')
elif cpu==0 and op==2:
    print('O coputador jogou {}' .format(itens[cpu]))
    print('Voce jogou {} '.format(itens[op]))
    print('Voce perdeu')
    
elif cpu==1 and op==0:
    print('O coputador jogou {}' .format(itens[cpu]))
    print('Voce jogou {} '.format(itens[op]))
    print('Voce perdeu')
elif cpu==1 and op==2:
    print('O coputador jogou {}' .format(itens[cpu]))
    print('Voce jogou {} '.format(itens[op]))
    print('Voce ganhou!')

elif cpu==2 and op==0:
    print('O coputador jogou {}' .format(itens[cpu]))
    print('Voce jogou {} '.format(itens[op]))
    print('Voce ganhou!')
elif cpu==2 and op==1:
    print('O coputador jogou {}' .format(itens[cpu]))
    print('Voce jogou {} '.format(itens[op]))
    print('Voce perdeu!')