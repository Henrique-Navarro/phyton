n= int(input('Qual o primeiro termo? '))
r= int(input('Qual a razão? '))
seq =0
termo= n
while(seq != 10):
    print(termo,end=' ')
    termo= termo + r
    seq+=1