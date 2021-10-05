maior=0
menor=0
for c in range(0,7):
    idade= int(input('Qual sua idade? '))
    if idade >= 18:
        maior= maior+1
    if idade < 18:
        menor= menor+1
print(f'{maior} pessoas são maiores {menor} pessoas são menores ')