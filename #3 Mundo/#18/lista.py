galera= list()
dado= list()
for c in range(0,3):
    dado.append(str(input('nome: ')))
    dado.append(int(input('idade:')))
    #galera recebe apenas uma cópia de 'dado', usando: [:]
    #se fosse apenas galera.append(dado) criaria uma ligação entre ambos, sendo assim
    galera.append(dado[:])
    #sendo assim o dado.clear(), limparia a 'galera' tambem
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
    else:
        print(f'{p[1]} é menor de idade')