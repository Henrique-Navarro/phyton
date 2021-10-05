med=0
maior=0
menor=0
mulher=0
for c in range(1,5):
    print(f'---- {c} PESSOA ----')
    nome= input('Digite um nome: ').strip()
    idade= int(input('Digite a idade: '))
    sexo= input('Digite o sexo [M/F]: \n').strip().upper()

    med= med + idade
    if sexo in 'M':
        if c == 1:
            maior =idade
            velho= nome
        else:
            if idade > maior:
                maior = idade
                velho= nome
    if sexo in 'F':
        if idade < 20:
            mulher += 1

print(f'A média de idade é: {med/4}')
print(f'O homem mais velho é o {velho} com {maior} anos')
print(f'A quantidade de mulheres com menos de 20 anos é: {mulher}')