n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
n4 = int(input('Digite o quarto número: '))

q1 = n1 ** 2
q2 = n2 ** 2
q3 = n3 ** 2
q4 = n4 ** 2

if q3 > 1000:
    print(q3)
else:
    print(f'{n1} e {q1}\n{n2} e {q2}\n{n3} e {q3}\n{n4} e {q4}')