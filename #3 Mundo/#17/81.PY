lista=list()
cont=0
while True:
    lista.append(int(input('Digite um valor: ')))
    op=str(input('Quer continuar?[s/n] ')).upper().strip()[0]
    cont+=1
    while op not in 'SN':
        op=str(input('Opção inválida: ')).upper().strip()[0]
    if op == 'N':
        break
print(f'Foram digitados {cont} valores')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print(f'O valor 5 aparece na lista na posição {lista.index(5)}')
else:
    print('5 não está na lista')