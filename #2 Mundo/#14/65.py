continuar = 'S'
vez=0
while (continuar == 'SIM') or (continuar == 'S'):
    n= int(input('Digite um numero: '))
    if vez==0:
        soma=0
        maior=n
        menor=n
        cont=0
        vez=1
    soma = soma + n
    cont = cont + 1
    if n > maior:
        maior=n
    if n < menor:
        menor=n
    continuar= input('Voce quer continuar? ').strip().upper()
print(f'A media foi: {soma/cont}')
print(f'O maior foi: {maior}')
print(f'O menor foi: {menor}')
print(f'O programa foi executado {cont} vezes')
