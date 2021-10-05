total=totH=totM=0
while True:
    idade= int(input('Qual a idade? '))
    sexo=' '
    while sexo not in 'MF':
        sexo= str(input('Qual o sexo? ')).strip().upper()[0]
    if idade >= 18:
        total+=1
    if sexo == 'M': 
        totH+=1
    if sexo == 'F' and idade<20:
        totM+=1
    op=' '
    while op not in 'SN':
        op= str(input('Quer continuar? ')).strip().upper()[0]
    if op == 'N':
        break
print(f'''
{total} pessoas tem mais de 18 anos
{totH} homens foram cadrastados
{totM} mulheres tem menos de 20 anos
''')
