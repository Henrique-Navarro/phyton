cont_idade=cont_homem=cont_muie=0
while True:
    idade= int(input('Quantos anos voce tem? '))
    if idade>18:
        cont_idade+=1

    sexo= str(input('Qual seu sexo?[M/F] ')).strip().upper()
    while sexo != 'M' and sexo != 'F':
        sexo= str(input('Qual seu sexo?[M/F] ')).strip().upper()
    if sexo == 'M':
        cont_homem+=1
    else:
        if idade<20:
            cont_muie+=1

    op= str(input('Quer continuar?[S/N] ')).strip().upper()
    while op != 'S' and op != 'N':
        op= str(input('Quer continuar?[S/N] ')).strip().upper()
    if op == 'N':
        break
print(f'''
{cont_idade} pessoas tem mais de 18 anos
{cont_homem} homens foram cadrastados
{cont_muie} mulheres tem menos de 20 anos
''')