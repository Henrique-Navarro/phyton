import random
n1= str(input('Digite o nome: '))
n2= str(input('Digite o nome: '))
n3= str(input('Digite o nome: '))
n4= str(input('Digite o nome: '))


print(f'O rescolhido foi: {random.choices([n1,n2,n3,n4])}')