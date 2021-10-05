n= int(input('Qual o primeiro termo? '))
r= int(input('Qual a razão? '))
valor=n
termos=10
seq=mais=0
while termos != 0:
    if seq !=0:
        mais= int(input('\nQuantos termos a mais? '))
    for c in range(n,termos+1):
        valor= valor+r
        print(valor, end=' ')
    termos= 10+ mais
    seq=1
print('ACABOU!!!')