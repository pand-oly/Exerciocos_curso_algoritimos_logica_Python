ContadorTotal = 0
ContadorSit1 = 0
ContadorSit2 = 0
ContadorSit3 = 0
ContadorSit4 = 0

identificacao = int(input('Iforme a identificação: '))

while identificacao != 0:
    print("1 - Necessita de esfera.\n")
    print("2 - Necessita de limpeza.\n")
    print("3 - Necessita detroca de cabo ou conector.\n")
    print("4 - Quebrado ou defeituoso.\n")
    
    defeito = int(input("Informe o tipo de defeito "))

    if defeito == 1:
        ContadorSit1 = ContadorSit1 + 1 
    elif defeito == 2:
        ContadorSit2 = ContadorSit2 + 1
    elif defeito == 3:
        ContadorSit3 = ContadorSit3 + 1
    elif defeito == 4:
        ContadorSit4 = ContadorSit4 + 1

ContadorTotal = ContadorTotal + 1

    identificacao = int(input("Informe a identificação: "))

p1 = ContadorSit1 / ContadorTotal * 100.0
p2 = ContadorSit2 / ContadorTotal * 100.0
p3 = ContadorSit3 / ContadorTotal * 100.0
p4 = ContadorSit4 / ContadorTotal * 100.0

print(f"Quantidade de Mouses {ContadorTotal}");
print(f"Situação                                 Quatidade          percentual");
print(f'1-Necessita de esfera                     {ContadorSit1}               {"%.2f" % p1}')
print(f"2-Necessita de limpeza                    {ContadorSit2}               {'%.2f' %  p2}")
print(f"3-Necessita troca de cabo ou conctor      {ContadorSit3}               {'%.2f' % p3}")
print(f"4-quebrado ou inutilizado                 {ContadorSit4}               {'%.2f' % p4}")