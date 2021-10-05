#41:19
nome= str(input('Digite um nome: ')).strip()

print('Seu nome maíusculo é: {}'.format(nome.upper()))
print(f'Seu nome minúsculo é: {nome.lower()}')
print('seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras' .format(nome.find(' ')))
divide= nome.split()
print('Seu primeiro nome é {} e tem {} letras' .format(divide[0], len(divide[0])))