num=int(input('Digite um numero: '))
print('Digite 1 para binario')
print('Digite 2 para octal')
print('Digite 3 para hexadecimal')
op= int(input('Digite a opção '))

if op==1:
    print('{} em binario: {}' .format(num, bin(num)[2:]))
elif op==2:
    print('{} em octal: {}' .format(num, oct(num)[2:]))
elif op==3:
    print('{} em hexa: {}' .format(num, hex(num)[2:]))
else:
    print('Opção inválida')