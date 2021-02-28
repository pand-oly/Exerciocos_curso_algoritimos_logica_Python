n = int(input('Digite o número entre 1 e 10: '))

while n < 1 or n > 10:
    n = int(input('Digite o número entre 1 e 10: '))
print(f'Tabuada de {n}')
for i in range(1, 11):
    print(f'{n} X {i} = {n * i}')
