n=int(input('Digite um numero: '))
primo=0
#começa em 2(pq 1 não é primo), vai até o numero informado+1(), indo de um em um
for c in range(1,n+1,+1):
    #se numero digitado foi divisível por 1, primo soma+1
    #se numero digitado foi divisível por 2, primo soma+1
    #se numero digitado foi divisível por 3, primo soma+1
    #se numero digitado foi divisível por n+1(for não pega ultimo termo, por isso +1), primo soma+1 [numero=ele mesmo]
    if n%c == 0:
        primo= primo+1
#se for ==2, significa que ele foi divisível apenas por si mesmo e por 1(é primo)
if primo==2:
    print('é primo')
else:
    print('não é primo')