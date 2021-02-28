vetor = []
MaiorQue50 = False

for i in range (0, 10):
    num = int(input(f'Informe o valor par o vetor {i + 1}/10:'))
    vetor.append(num)
for i in vetor:
    if i > 50:
        print(f"O número {i} está na posição {vetor.index(i)}")
        MaiorQue50 = True
if MaiorQue50 == False:
    print('Não existe nenhum número maior que 50.')
    