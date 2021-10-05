nome = input('QUal seu nome? ')
cores= {'limpa': '\033[m',
        'azul': '\033[34m',
        'amarelo': '\033[33m',
        'pretobranco': '\033[7;30m'}

print('Ola {}{}{}' .format(cores['pretobranco'], nome, cores['limpa']))