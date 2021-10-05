lista= ('Pão', 1, 'Leite', 3.50, 'Frango', 12, 'Refrigerante', 5.40, 'Shampoo', 8, 'Livro', 30.80, 'Estojo', 25.70)
print('\033[34m=-'*20)
print(f'\033[32m{"Lista de Preços":^40}\033[m')
print('\033[34m=-'*20)
for c in range(0,len(lista)-1,+2):
    print(f'\033[33m{lista[c]:.<32}\033[mR${lista[c+1]:>6.2f}')
print('\033[34m=-\033[m'*20)