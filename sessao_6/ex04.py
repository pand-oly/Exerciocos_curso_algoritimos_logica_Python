altura = float(input('informe sua altura: '))
sexo = input('informe seu genero m/f ')

if sexo.lower() == 'm':
    PesoIdeal = (72.7 * altura) - 58
elif sexo.lower() == 'f':
    PesoIdeal = (62.1 * altura) - 44.7
else:
    PesoIdeal = 0
    print('sexo não reconhecido')
print(f'seu peso ideal é {"%.2f" % PesoIdeal}')