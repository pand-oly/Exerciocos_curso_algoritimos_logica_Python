maior = -999
menor = 999
soma = 0

for i in range(1, 11):
    valor = int(input('Informe um valor: '))
    if valor > 0:
        if valor > maior:
            maior = valor
        elif valor < menor:
            menor = valor
        soma = soma + valor
    else:
        valor = int(input('Informe um valor: '))

print(f'Maior: {maior}')
print(f'Menor: {menor}')
print(f'Media: {soma / 10}')