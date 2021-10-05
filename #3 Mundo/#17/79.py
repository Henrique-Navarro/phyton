op='S'
vez=n=0
lista= list()
while True:
    if vez==1:
        op=str(input('Quer continuar?[s/n] ')).upper().strip()
    while op not in 'SN':
        op=str(input('Opção inválida: ')).upper().strip()
    if op in 'N':
        break
        print('Programa encerrado!!!')
    else:
        n=(int(input('\033[3mDigite um valor: \033[m')))
    if n in lista:
        print('\033[31mNumero ja existente!!!\033[m')
    else:
        lista.append(n)
        print('\033[32mNumero adicionado com sucesso!!\033[m')
    vez=1
    n+=1
print('Programa Encerrado!!!')
lista.sort()
print(f'Lista oprganizada: \033[33m{lista}\033[m')