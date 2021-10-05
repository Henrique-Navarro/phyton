frase= str(input('Digite uma frase: ')).strip().upper()
palavras= frase.split()
junto= ''.join(palavras)
inverso= junto[::-1]
if inverso == junto:
    print(f'{junto} == {inverso}')
    print('Temos um palindromo')
else:
    print(f'{junto} != {inverso}')
    print('não temos um palindromo')