n= int(input('Qual o primeiro termo? '))
r= int(input('Qual a razão? '))
posicao=0
numero = n
termomais=10
vez=0   
cont=0
while termomais != 0:
    if vez ==0:
        qtd= termomais

    if vez ==1:
        qtd=0
        qtd = termomais + 10

    while posicao != qtd:
        print(numero, end=' ')
        numero= numero + r
        posicao += 1
        
    termomais= int(input('\nQuantos termos a mais? '))
    vez=1
    posicao=0
    numero=n
    cont= cont+termomais
print('\033[1;32mPrograma finalizado com sucesso')
print(f'Foram mostrados {cont+10} numeros\033[m')