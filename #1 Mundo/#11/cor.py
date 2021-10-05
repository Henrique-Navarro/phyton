print('\033[1;33;44mOla mundo\033[m')
print('\033[7;33;44mOla mundo\033[m')
print('\033[1;30mOla mundo\033[m')

a=3
b=5
print(f'Os valores são \033[1;36;41m{a}\033[me \033[1;34;43m{b}\033[m')

nome= input('Qual seu nome? ')
print('Muito prazer {}{}{}' .format('\033[4;34m',nome,'\033[m'))