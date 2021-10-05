distancia= int(input('Digite a distancia(km): '))

'''if distancia <= 200:
    valor= distancia*(0.5)
    print(f'O valor cobrado será de R${valor} reais')
if distancia > 200:
    print(f'O valor cobrado será de R${distancia*(0.45)} reais')'''

preço = distancia*0.5 if distancia <= 200 else distancia*0.45
print(f'{preço}')