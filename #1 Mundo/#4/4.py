a= input('Digite algo: ')

print ('O tipo primitivo é: ', type(a))

print ('Tem espaços?? ',a.isspace())

print ('É numerico? {}{}{}'.format('\033[30m',a.isnumeric(),'\033[m'))
print ('É alfabético? {}{}{}'.format('\033[31m',a.isalpha(),'\033[m'))
print ('É alfanumérico? {}{}{}'.format('\033[32m',a.isalnum(),'\033[m'))
print ('É decimal? {}{}{}'.format('\033[33m',a.isdecimal(),'\033[m'))
print ('Está em maíscula? {}{}{}'.format('\033[35m',a.isupper(),'\033[m'))

print(f'Só tem espaços? {a.isspace()}')
print(f'É numérico? {a.isnumeric()}')
print(f'É alfabético? {a.isalpha()}')
print(f'É alfanumérico? {a.isalnum()}')
print(f'Está em letras maiúsculas?{a.isupper()}')
print(f'Está em letras minúsculas? {a.islower()}')
print(f'Está capitalizada? {a.istitle()}')