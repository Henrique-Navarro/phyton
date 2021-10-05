sexo= str(input('Digite os sexo: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo= str(input('Invalido, digite novamente: ')).strip().upper()[0]
if sexo == 'F':
    print(f'Seu sexo é: feminino')
else:
    print(f'Seu sexo é: maculino')