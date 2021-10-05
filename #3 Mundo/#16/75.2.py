num= (int(input('Digite um numero: ')),
    int(input('Digite um numero: ')),
    int(input('Digite um numero: ')),
    int(input('Digite um numero: ')))
print(f'Vc digitou: {num}')
print(f'9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'3 aparece na {num.index(3)+1}º posição')
else:
    print('3 não aparece')
print(f'Os valores pares foram: ', end='')
for n in num:
    if n%2==0:
        print(n,end=' ')

