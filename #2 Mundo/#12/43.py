peso= float(input('Qual seu peso? '))
altura= float(input('Qual sua altura? '))
if altura>50:
    altura= altura/100

imc= peso/(altura**2)
print(f'{imc}')

if imc<18.5:
    print('abaixo do peso')
elif 18.5<= imc<25:
    print('peso ideal')
elif imc>=25 and imc<30:
    print('sobrepeso')
elif imc<=30 and imc <=40:
    print('obesidade')
elif imc>40:
    print('obesidade morbida')