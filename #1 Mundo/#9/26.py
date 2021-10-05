nome= str(input('Digite um nome: ')).strip()
print('A letra a aparece {} vezes' .format(nome.lower().count('a')))
print('A letra a aparece na primeira vez na posição {}' .format(nome.lower().find('a')+1))
print('A letra a aparece na ultima vez na posição {}' .format(nome.lower().rfind('a')+1))