import random
n1= str(input('Digite o nome: '))
n2= str(input('Digite o nome: '))
n3= str(input('Digite o nome: '))
n4= str(input('Digite o nome: '))

alunos = [n1,n2,n3,4]
print(f'Escolhido: {random.choices(alunos)}')