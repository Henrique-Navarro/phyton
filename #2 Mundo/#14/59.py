from time import sleep
maior=menor=op=0
x= int(input('Digite primeiro numero: '))
y= int(input('Digite segundo numero: '))
while op != 5:
    print('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos numeros\n[5] sair')
    op= int(input('Qual a opção? '))

    if op ==1:
        soma= x+y
        print(f'A soma de {x} + {y} = {soma}')
    elif op ==2:
        multi= x*y
        print(f'A multiplicação de {x} * {y} = {multi}')
    elif op ==3:
        if x > y:
            maior = x
        if y > x:
            maior = y
        print(f'O maior é: {maior}')
    elif op ==4:
        x= int(input('Digite primeiro numero: '))
        y= int(input('Digite segundo numero: '))
print('FINALIZANDO...')
sleep(1)
print('PROGRAMA FINALIZADO !!!')