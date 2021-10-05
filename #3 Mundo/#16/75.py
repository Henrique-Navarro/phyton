n1= int(input('Digite um numero: '))
n2= int(input('Digite um numero: '))
n3= int(input('Digite um numero: '))
n4= int(input('Digite um numero: '))
numeros= (n1,n2,n3,n4)
cont=pares=tres=0
for n in range(0,4):
    if numeros[n]==9:
        cont+=1
    if numeros[n]==3:
        tres=1
    if numeros[n]%2==0:
        pares+=1
print(f'9 aparece {cont} vezes')
if tres==1:
    print(f'3 aparece na {numeros.index(3)}º posição')
else:
    print('3 não aparece')
print(f'{pares} numeros são pares, sendo eles:')
for n in range(0,4):
    if (numeros[n]%2==0) and pares>=1:
        print(f'{numeros[n]}', end=' ')
    elif pares==0:
        print('Não existe numeros pares')
        break
