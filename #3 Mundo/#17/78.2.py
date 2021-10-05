lista= list()
for c in range(0,5):
    lista.append(int(input('Digite um valor: ')))
maior=menor=lista[0]
pm=pM=0
for p,v in enumerate(lista):
    if lista[p]>maior:
        maior=lista[p]
        pM=p
    if lista[p]<menor:
        menor=lista[p]
        pm=p
print(f'maior: {maior} posição: {pM}')
print(f'menor: {menor} posição: {pm}')