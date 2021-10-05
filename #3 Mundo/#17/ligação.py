a=[1,2,3,4]
#ligação                    #copia:
b=a                         b=a[:]
b[2]=100    
print(f'Lista A: {a}')
print(f'Lista B: {b}')