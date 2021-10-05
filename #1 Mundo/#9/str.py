frase= 'Curso em Video Python'
print(frase[3:13])
print(frase[:7])
print(frase[7:])
print(frase[1:15:2])
print(frase.upper().count('O'))
print(len(frase.strip()))
#len conta os caracteres
#strip tira os espaços
print('Curso' in frase)
print(frase.lower().find('Video'))

print(frase.split())
dividido= frase.split()
print(dividido[0])
print(dividido[3][1])

print(""" em uma sequência de números de 1 a 15
o computador escolhe um de maneira aleatória
sendo assim, o usuário tem que adivinhar qual número foie escolhido
se maneira linear, se o usuário escolher o número 1, depois o 2, e assim sucessivamente
em determiando momento, ele acertará o resultado """)