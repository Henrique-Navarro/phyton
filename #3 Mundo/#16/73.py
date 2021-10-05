times= ('Palmeiras','Santos','Vasco da Gama','Grêmio','Flamengo','Chapeco','Internacional','Cruzeiro','São Paulo','Atlético Mineiro','Botafogo','Fluminense','Coritiba','Bahia','Goiás','Guarani','Sport','Portuguesa','Atlético Paranaense','Vitória')
p=1
for n in range(0,5):
    print(f'{p}: {times[n]}')
    p+=1
p=17
for n in range(15,19):
    print(f'{p}: {times[n+1]}')
    p+=1
print(sorted(times))
print(f'Chapeco esta na posição: {times.index("Chapeco")+1}')