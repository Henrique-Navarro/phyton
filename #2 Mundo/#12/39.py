from datetime import date
ano= int(input('Qual ano vc nasceu? '))
mes= int(input('Em que mes vc nasceu? '))

if mes>6:
    idade= date.today().year - ano -1
    aux=12-mes
    m=date.today().month+aux
elif mes<6:
    idade= date.today().year - ano
    m=date.today().month - mes

print(f'Sua idade é de {idade} anos e {m} meses')
if idade==18:
    print('Está na hora de voce se alistar')
elif idade < 18:
    print('Ainda não está na hora de se alistar, ainda faltam {} anos para voce se alistar' .format(18-idade))
elif idade > 18:
    print('Já passou {} anos da hora de se alistar' .format(idade-18))