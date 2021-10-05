while True:
    n= int(input('Digite um numero: '))
    if n < 0:
        break
    for c in range(1,11):
        print(f'{c:02} x {n} = \033[32m{c*n:<}\033[m')
print('Programa finalizado!!!')