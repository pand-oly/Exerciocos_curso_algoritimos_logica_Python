poluicao = float(input('Digite o nivel de puluição; '))

if poluicao >= 0.3 and poluicao < 0.4:
    print("Atenção: Industrias do 1° Grupo devem suspender  as atividades.")
elif poluicao >= 0.4 and poluicao < 0.5:
    print("Atenção: Industrias do 2° Grupo devem suspender as atividades.")
elif poluicao >= 0.5:
    print("Atenção: TODOS OS GRUPOS DEVEM SUSPEMDER IMEDIATAMENTE AS ATIVIDADES.")
