valores= list()
valores.append(5)
valores.append(6)
valores.append(7)

#for c in valores:
    #print(c)
for n in range(0,5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'\nNa posição {c} está: {v}', end=' ')