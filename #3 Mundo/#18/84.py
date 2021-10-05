pessoas= list()
dados= list()
pesadas=list()
leves=list()
vez=1
while True:
    dados.append(str(input('Qual seu nome? ')))
    dados.append(int(input('Qual seu peso? ')))
    pessoas.append(dados[:])
    dados.clear()
    op=str(input('Quer continuar?[s/n] ')).upper().strip()[0]
    while op not in 'SN':
        op=str(input('Opção inválida: ')).upper().strip()[0]
    if op in 'N':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas')
if len(pessoas) <= 1:
    print('Numero insuficiente de pessoas')
for p in pessoas:
    if vez==1:
        maior=menor=p[1]
    if p[1]>=maior:
        maior=p[1]
        pesadas.append(p[0])
        pesadas.append(p[1])
    if p[1]<=menor:
        menor=p[1]
        leves.append(p[0])
        leves.append(p[1])
    vez=0
print(maior,menor)
print(f'A pessoa mais leve é {leves[0]} com {leves[1]}kg')
print(f'A pessoa mais pesada é {pesadas[0]} com {pesadas[1]}kg')