inicio=fim=0
exp=str(input('Digite a expressão: ')).strip()
exp.split()
for c in range(0,len(exp)):
    if '(' in exp[c]:
        inicio+=1
    if ')' in exp[c]:   
        fim+=1
if inicio==fim:
    print('A expressão é válida')
else:
    print('Expressão inválida')