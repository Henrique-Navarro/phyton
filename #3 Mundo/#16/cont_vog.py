palavras=('Regua', 'Compasso', 'Hamburguer', 'hurrasco', 'Estilete')
for pos in palavras:
    print(f'\nEm {pos} temos: ', end='')
    for letra in pos:
        if letra.upper() in 'AEIOU':
            print(f'{letra}', end=' ')
