from random import randint
v=0
while True:
    jogador= int(input('Digite um valor: '))
    cpu= randint(0,10)
    total= cpu+jogador
    tip=' '
    while tip not in 'PI':
        tip= str(input('Par ou impar? ')).strip().upper()[0]
    print(f'Vc jogou {jogador} e o computador {cpu}, total de {total}')
    if tip== 'P':
        if total%2==0:
            print('VC ganhou')
            v+=1
        else:
            print('Vc perdeu')
            break
    if tip== 'I':
        if total%2==1:
            print('Vc ganhou')
            v+=1
        else:
            print('VC perdeu')
            break
print(f'Vc venceu {v} vezes')