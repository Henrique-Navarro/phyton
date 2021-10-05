lista= list()
for c in range(0,5):
    lista.append(int(input('Digite um valor: ')))
print(f'Maior: \033[32m{max(lista)}\033[m na posição: \033[34m{lista.index(max(lista))}\033[m')
print(f'Menor: \033[32m{min(lista)}\033[m na posição: \033[34m{lista.index(min(lista))}\033[m')