c = int(input("Digite seu codico: "))
n = int(input("Digite o numero de horas trabalhadas: "))

if n > 50:
    e = n -50
    n = n - e
else:
    e = 0

extra = e * 20
salario = n * 10
print(f'Salario: {salario}')
print(f'Extra: {extra}')
