from matplotlib import pyplot as plt

tabMeteo1 = [((2022,1,20), 2, 16, 0),((2022,1,21), 1, 13, 0.2), ((2022,1,22), 7, 17, 0.01)]
meteo = []

def inserir():
    dias = int(input("De quantos dias vais inserir os dados meteorológicos? "))
    for _ in range (dias):
        dia = int(input("Diga o dia dos dados a introduzir: "))
        mes = int(input("Diga o mês do dia dos dados a introduzir: "))
        ano = int(input("Diga o ano do mês do dia dos dados a introduzir: "))
        data = (ano, mes, dia)
        tempmin = float(input("Diga a temperatura mínima: "))
        tempmax = float(input("Diga a temperatura máxima: "))
        prec = float(input("Diga a precipitação: "))
        meteo.append((data, tempmin, tempmax, prec))
    return meteo

def carregaTabMeteo(fnome):
    res = []
    file = open(fnome, "r")
    for line in file:
        partes = line.strip().split("|")
        ano, mes, dia = partes[0].split("-")
        res.append(((int(ano), int(mes), int(dia)), float(partes[1]), float(partes[2]), float(partes[3])))
    file.close()
    return res

def medias(tabMeteo1):
    res = []
    for x in tabMeteo1:
        data = x[0]        # data, tmin, tmax, *_ = x
        tmin = x[1]
        tmax = x[2]
        media = (tmin + tmax) / 2
        res.append((data, media))
    return res

def guardaTabMeteo(t, fnome):
    file = open(fnome, "w")
    for data, tmin, tmax, p in t:
        ano, mes, dia = data
        file.write(f"{ano}-{mes}-{dia}|{tmin}|{tmax}|{p}\n")
    file.close()
    return

def minMin(tabMeteo1):
    return min(i[1] for i in tabMeteo1)

def amplTerm(tabMeteo1):
    res = []
    for x in tabMeteo1:
        data = x[0]
        tmin = x[1]
        tmax = x[2]
        ampl = tmax - tmin
        res.append((data, ampl))
    return res 

def maxChuva(tabMeteo1):
    max_prec = 0
    max_data = None
    for x in tabMeteo1:
        data = x[0]
        prec = x[3]
        if prec > max_prec:
            max_prec = prec
            max_data = data
    return (max_data, max_prec)

def diasChuvosos(tabMeteo1, p):
    res = []
    for x in tabMeteo1:
        data = x[0]
        prec = x[3]
        if prec > p:
            res.append(data)
    return res

def maxPeriodoCalor(tabMeteo1, p):
    contador = 0
    maximo = 0
    for data, tmin, tmax, prec in tabMeteo1:
        if prec < p:
            contador = contador + 1
            if contador > maximo:
                maximo = contador
        else:
            contador = 0
    return maximo

def grafTabMeteo(t):    
    y_min = [ tmin for data, tmin, *_ in t]
    y_max = [ tmax for data, tmin, tmax, *_ in t]

    x = [f"{data[0]}-{data[1]}-{data[2]}" for data, *_ in t]
    print(y_min)
    print(x)

    plt.plot(x,y_min, color = "green", marker = "o", label = "Temperatura mínima em ºC")
    plt.plot(x,y_max, color = "red", marker = "o", label = "Temperatura máxima em ºC")

    plt.legend()
    plt.grid()
    plt.show()
    return

op = int(input("""Bem vindo ao programa de análise de dados meteorológicos.
Para começar, podes escolher um ficheiro com os dados (opção 1) ou introduzi-los tu (opção 2).
Preferes opção 1 ou opção 2: """))

if op == 1:
    fnome = input("Diz o nome do ficheiro tipo: 'nome.txt': ")
    meteo = carregaTabMeteo(fnome)
elif op == 2:
    meteo = inserir()
else:
    print("Opção inválida.")

modo = int(input("Agora escolhe uma operação a realizar com esses dados:\n" \
"1) Diz as temperaturas médias;\n" \
"2) Guarda os dados num ficheiro;\n" \
"3) Descobre a temperatura mínima mais baixa no conjunto de dados;\n" \
"4) Descobre a amplitude entre a temperatura máxima e mínima de cada dia;\n" \
"5) Descobre o dia em que ocorreu precipitação máxima;\n" \
"6) Define os dias em que a precipitação foi superior a um valor específico;\n" \
"7) Descobre quantos dias consecutivos a precipitação foi abaixo de um certo valor específico;\n" \
"8) Desenha os gráficos da temperatura mínima e máxima.\nOpção: "))

if modo == 1:
    print(medias(meteo))
elif modo == 2:
    fnome = input("Nome do ficheiro para guardar (ex: 'dados.txt'): ")
    guardaTabMeteo(meteo, fnome)
elif modo == 3:
    print("Temperatura mínima mais baixa:", minMin(meteo))
elif modo == 4:
    print(amplTerm(meteo))
elif modo == 5:
    print("Máximo de chuva (data, valor):", maxChuva(meteo))
elif modo == 6:
    limite = float(input("Indica o valor limite de precipitação: "))
    print(diasChuvosos(meteo, limite))
elif modo == 7:
    limite = float(input("Indica o valor limite de precipitação: "))
    print("Dias consecutivos:", maxPeriodoCalor(meteo, limite))
elif modo == 8:
    grafTabMeteo(meteo)
