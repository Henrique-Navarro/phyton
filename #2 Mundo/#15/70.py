total=cont_prod=vez=0
barato=''
while True:
    if vez==0:
        nome= str(input('Qual o nome do produto? '))
        preço= int(input('Qual o preço do produto? '))
        menor=preço
        barato=nome
    if vez==1:
        nome= str(input('Qual o nome do produto? '))
        preço= int(input('Qual o preço do produto? '))
    total+= preço
    if preço>1000:
        cont_prod+=1
    if preço < menor:
        menor= preço
        barato= nome
    op= str(input('Deseja continuar[S/N]? ')).strip().upper()[0]
    if op != 'S' and op != 'N':
        print('Opção inválida')
        op= str(input('Deseja continuar[S/N]? ')).strip().upper()[0]
    if op == 'N':
        break
    vez=1
print(f'''
o total gasto foi de: R${total}
{cont_prod} produtos custam mais que R$1000
o produto mais barato é: {barato} que custa {menor}
''')