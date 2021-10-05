n=soma=cont=0
while True:
    n= int(input('Digite um numero: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'A soma é de {soma}')
print(f'Foram somados {cont} numeros')
print('Acabou!!!')