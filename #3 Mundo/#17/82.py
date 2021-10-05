lista=list()
par=list()
impar=list()
while True:
    lista.append(int(input('Digite um valor: ')))
    op=input('Quer continuar? ').strip().upper()
    while op not in 'SN':
        op=input('\033[31mOpção inválida: \033[m').strip().upper()
    if op in 'N':   
        break
for c in range(0,len(lista)):
    if lista[c] %2 ==0:
        par.append(lista[c])
    elif lista[c] %2 !=0:
        impar.append(lista[c])
par.sort()
impar.sort()
print(f'A lista: \033[34m{lista}\033[m')
print(f'A lista par: \033[32m{par}\033[m')
print(f'A lista impar: \033[33m{impar}\033[m')