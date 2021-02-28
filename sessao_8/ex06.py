vetor = []

codico = int(input('Iforme o codico: '))

if codico != 0:
    for i in range(0, 5):
        num = float(input('Informe um número real: '))
        vetor.append(num)

    if codico == 1:
        for i in vetor:
            print(i)
        
    if codico == 2:
        vetor.reverse()
        for i in vetor:
            print(i)
