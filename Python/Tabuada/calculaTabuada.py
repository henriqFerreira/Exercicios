continua = True
while continua:
    valorTabuada = int(input("Tabuada do número: "))
    for num in range(1, 11):
        print("%d x %d = %d" % (valorTabuada, num, valorTabuada*num))
    continua = input("Deseja continuar?[S/n] ")
    if continua == "s" or continua == "S":
        continua = True
    elif continua == "n" or continua == "N":
        continua = False
    else:
        print("Valor inválido")
