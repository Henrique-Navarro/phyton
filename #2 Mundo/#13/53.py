frase= str(input('Digite uma frase: ')).strip()
frase=frase.lower().replace(" ", "")
print(frase)
print(len(frase))
i=0
j=(len(frase))
for c in range(i,j+1):
    inverte[j] = frase[i]
    if inverte[j] == frase[i]:
        cont= cont+1
    i=i+1
    j=j-1
if cont==len(frase):
    print('são palíndromos')

#31,52