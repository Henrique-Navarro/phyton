palavras=('Regua', 'Compasso', 'Hamburguer', 'hurrasco', 'Estilete')
vogal=('aeiou')
cont=0
print()
for p in palavras:
    print(f'\nNa palavra \033[32m{p.upper()}\033[m temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'\033[34m{letra.lower()}\033[m', end=' ')
            cont+=1