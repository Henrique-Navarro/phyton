numeros=list()
while True:
    n=int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
    else:
        print('erro')
    op= str(input('Quer continuar?[s/n] ')).upper().strip()
    while op not in 'SN':
        op= str(input('Quer continuar?[s/n] ')).upper().strip()
    if op in 'N':
        break
numeros.sort()
print(numeros)