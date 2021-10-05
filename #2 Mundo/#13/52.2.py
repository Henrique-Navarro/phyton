tot=0
n=int(input('\033[mDigite um numero: '))
for c in range(1, n+1):
    if n%c==0:
        print('\033[34m',end='')
        tot+=1
    else:
        print('\033[31m',end='')
    print('{} '.format(c), end='')
print(f'\033[m\nO numero {n} foi divisível {tot} vezes')