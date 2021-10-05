numero= ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
op=''
while True:
    n= int(input('Digite um numero entre [0-20]: '))
    while (n<0) or (n>20):
        n=int(input('Opção inválida: '))
    print(f'Na posição {n} está o numero {numero[n]}')
    op= str(input('Quer continuar?[S/N] ')).strip().upper()

    while op not in 'SN':
        op= str(input('Quer continuar?[S/N] ')).strip().upper()
    if op == 'N':
        break
print('ACABOU!!!')