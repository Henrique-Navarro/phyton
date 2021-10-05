from datetime import date
ano= int(input('Qual ano vc nasceu? '))
mes= int(input('Qual mes vc nasceu? '))

if mes>date.today().month:
    idade= date.today().year+(-ano-1)
    idade= idade*12
    aux= 12-mes
    real= idade+aux+date.today().month
    real= real//12
    print(f'Sua idade é: {real} anos')

elif mes<date.today().month:
    idade= date.today().year

if real<=9:
    print('mirim')
elif real<= 14:
    print('infantil')
elif real <=19:
    print('junior')
elif real<=25:
    print('senior')
elif real>20:
    print('master')