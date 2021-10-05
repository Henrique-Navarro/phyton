salario= float(input('Digite o valor do salario: '))

if salario > 1250:
    print(f'O novo salario é de: R${salario + (salario/10) } reais')
if salario <= 1250:
    aumento= salario + salario * 15 /100
    print('o novo salário é de: R${}' .format(aumento))