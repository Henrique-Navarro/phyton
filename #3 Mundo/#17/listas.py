#lista definida
n= [1,2,3,4,5]

#mudar valor da lista
n[2]=10

#adicionar valor na ultima posição
n.append(7)

#organizar do maior para o menor
n.sort(reverse=True)

#organizar oredem crescente
n.sort()

#adicionar na posição 0 o valor -1
n.insert(0,-1)

#remover o ultimo elemento ou n.pop(2) remove o elemento da posição 2
n.pop()

#remove o primeiro 2 que ele achar na lista
n.remove(2)
if 500 in n:
    n.remove(500)
print(n)
print(f'A lista possui {len(n)} elementos')