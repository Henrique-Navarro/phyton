maior= 0
menor= 0
#peso em for comça em =1 (5 pessoas)
for peso in range(1,6):
    peso= int(input('Qual seu peso? '))
    #peso == 1, primeira vez do programa
    if peso == 1:
        maior= peso
        menor= peso
    else: 
        if peso > maior:
            maior= peso

        if peso < menor:
            menor= peso
print(f'o maior é: {maior} e o menor é: {menor}')