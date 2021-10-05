a= int(input('Digite um numero: '))
b= int(input('Digite um numero: '))
c= int(input('Digite um numero: '))

#verificando menor
menor=a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c
print(f'O menor valor é: {menor}')

#verificando maior
maior=a
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior=c
print(f'O maior valor é: {maior}')