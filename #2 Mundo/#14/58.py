from random import randint
palpite=0
cpu= randint(0,10)
n=-1
while n!=cpu:
    n= int(input('Digite um numero: '))
    palpite +=1
print(f'Foram necessárias {palpite} tentativas')