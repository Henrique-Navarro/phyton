casa= int(input('Qual o valor da casa? '))
salario= int(input('Qual o valor do salário? '))
anos= int(input('Quantos anos? '))
anos= anos*12
mensal= casa/anos

if mensal <= (30*salario)/100:
    print('Voce pode pegar o empréstimo')
else:
    print('Empréstimo negado')