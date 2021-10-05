preçonormal= float(input('Qual o preço normal? '))
op= float(input('Qual sera a opção de pagamento?\n1- a vista\n2- a vista(cartão)\n3- 2x no cartão\n4- 3x ou mais no cartão\n'))
if op ==1:
    preço= preçonormal-((preçonormal*10)/100)
elif op ==2:
    preço= preçonormal-((preçonormal*5)/100)
elif op ==3:
    total= preçonormal
    total= preçonormal/2
    print(f'2 parcelas de R${total}')
    preço= total*2
elif op ==4:
    vezes=int(input('Quantas prestações ? '))
    preço= preçonormal+((preçonormal*20)/100)
    preço= preço/vezes
    print(f'{vezes} parcelas de R${preço}')
    preço= preço*vezes
else:
    print('opção invalida')
print(f'O preço total a ser pago será R${preço}: pois a forma de pagamento foi a {op}')
