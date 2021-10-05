from random import randint
n=soma=venceu=0
while True:
    n= int(input('Digite um valor: '))
    if n>10 or n<0:
        n= int(input('Opção inválida, digite novamente: '))
    op= input('Par ou ímpar? ').strip().upper()
    cpu= randint (0,10)
    soma= cpu + n
    if soma % 2 ==0:
        if op == 'P':
            venceu+=1
            print(f'VENCEU!\nVoce jogou {n} e o cpu {cpu}, a soma deu {soma} que é par')
        else:
            print(f'PERDEU!\nVoce jogou {n} e o cpu {cpu}, a soma deu {soma} que é ímpar')
            break
    else:
        if op == 'I':
            venceu+=1
            print(f'VENCEU!\nVoce jogou {n} e o cpu {cpu}, a soma deu {soma} que é ímpar')
        else:
            print(f'PERDEU!\nVoce jogou {n} e o cpu {cpu}, a soma deu {soma} que é par')
            break
print(f'Voce venceu {venceu} vezes')
