from random import randint
computador= randint(0,10)
acertou =False
palpites=0

while not acertou:
    jogador= int(input('Qual seu palpite? '))
    palpites +=1
    if jogador== computador:
        acertou= True
    else:
        if jogador > computador:
            print('Muito alto')   
        elif jogador < computador:
            print('Muito baixo')
print(f'Vc acertou com {palpites} palpites')