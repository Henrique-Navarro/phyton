'''lista= list()
primeiro=segundo=0
for c in range(0,5):
    n=int(input('Digite um valor: '))
    if c==0:
        primeiro=n
        lista.append(primeiro)
    if c==1:
        if n<primeiro:
            segundo=n
            lista.insert(0,segundo)
        else:
            segundo=n
            lista.insert(0,primeiro)
            lista.insert(4,segundo)

    if n> lista[0]:
        if n>lista[1]:
            if n>lista[2]:
                if n>lista[3]:
    else:
        lista.insert(0,n)
print(lista)