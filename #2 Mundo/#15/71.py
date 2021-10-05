resto=0
while True:
    valor= int(input('Qual o valor a ser sacado? '))
    notas= valor // 50
    resto = valor % 50
    print(f'{notas} notas de R$50')
    if resto>=20:
        notas = resto // 20
        resto = resto % 20
        print(f'{notas} notas de R$20')
    if resto>=10:
        notas = resto // 10
        resto = resto % 10
        print(f'{notas} notas de R$10')
    if resto<10:
        notas=resto
        print(f'{notas} notas de R$1')
print('Programa finalizado!!!')