from datetime import date
maior=0
menor=0
for c in range(0,7):
    nasc= int(input('Qual ano voce nasceu? '))
    idade= date.today().year - nasc
    if idade >= 21:
        maior= maior+1
    else:
        menor+=1
print(f'{maior} maiores {menor} menores')