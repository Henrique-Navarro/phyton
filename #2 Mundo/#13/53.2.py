frase= str(input('Digite uma frase: ')).strip().upper()
palavras= frase.split()
junto= ''.join(palavras)
inverso= ''
#começa em quantidade de letras -1 (casa-> 4 letras) c[0] a[1] s[2] a[3], começa pela ultima [3]
#limite= -1 então vai até [0] (primeira posição)
#indo de -1 em -1, para varrer a frase de tras pra frente
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
if inverso == junto:
    print(f'{junto} == {inverso}')
    print('Temos um palindromo')
else:
    print(f'{junto} != {inverso}')
    print('não temos um palindromo')