n= int(input('Digite um numero: '))
soma=0
cont=0
while n != 999:
    soma = soma + n
    cont = cont +1
    n= int(input('Digite um numero: '))
print(f'Soma foi de: {soma}')
print(f'Foram contados {cont} numeros')