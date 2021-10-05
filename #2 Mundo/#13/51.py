#le o primeiro termo, e a razão
x= int(input('Digite o primeiro termo: '))
r= int(input('Qual a razão? '))
#repetição começa no primeiro termo(x), vai até o ultimo(primeiro + 10* razão)= (1+ 10*3)=31 ou seja começa em 1 e o 11 termo sera 31, então o ultimo termo sera o 28, indo de tantos em tantos(razão)
for c in range(x,x+((10)*r),r):
    #printa c que recebe x c=x, dando um espaço entre os termos
    print(c, end=' ')