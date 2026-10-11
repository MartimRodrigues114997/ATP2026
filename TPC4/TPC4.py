import random
#esta função cria uma lista de num números e gera essa lista com random com numeros entre 1 e 100 e depois devolve essa lista
def criarLista():
    num = int(input("Quantos elementos queres na lista? "))
    while num <= 0:

        num = int(input("Quantos elementos queres na lista? "))

    lista_nova = []
    for i in range(num):
        lista_nova.append(random.randint(1, 100))
    return lista_nova

#esta cria uma lista com os números introduzidos pelo utilizador que podem ser <0 ou >0 exceto o número de elementos que é smp >0
def lerLista():
    n = int(input("Quantos elementos quer inserir? "))
    while num <= 0:
    
        num = int(input("Quantos elementos queres na lista? "))
    lista_nova = []
    for i in range(n):
        num = int(input(f"Elemento {i + 1}: "))
        lista_nova.append(num)
    return lista_nova

#esta função pega na última lista guardada e soma todos os elementos da lista
def soma(lista):
    total = 0
    for num in lista:
        total += num
    return total

#esta função faz a média com todos os elementos da lista, utilizei a função soma (salvaguardei o facto de a lista estar vazia)
def media(lista):
    if len(lista) == 0:
        return 0
    return soma(lista) / len(lista)

#esta função descobre o maior elemento 
def maior(lista):
    if len(lista) == 0:
        return None
    m = lista[0] #assumi que o primeiro era o maior e depois comparei com os outros
    for num in lista:
        if num > m:
            m = num
    return m

#esta faz o mesmo da de cima
def menor(lista):
    if len(lista) == 0:
        return None
    m = lista[0]
    for num in lista:
        if num < m:
            m = num
    return m

#aula prática P3
def estaOrdCres(lista):
    if len(lista) <= 1:
        return "Sim"
    crescente = True
    i = 0
    while i < len(lista) - 1 and crescente:
        if lista[i] > lista[i + 1]:
            crescente = False
        i += 1
    return "Sim" if crescente else "Não"

#aula prática P3
def estaOrdDecres(lista):
    if len(lista) <= 1:
        return "Sim"
    decrescente = True
    i = 0
    while i < len(lista) - 1 and decrescente:
        if lista[i] < lista[i + 1]:
            decrescente = False
        i += 1
    return "Sim" if decrescente else "Não"


def procElem(lista, numero):
    posicao = -1 # valor que devolve caso o elem nao esteja na lista
    encontrado = False
    i = 0 # contador
    while i < len(lista) and not encontrado:
        if lista[i] == numero:
            posicao = i
            encontrado = True
        i = i + 1
    return posicao


lista = []
a_correr = True

while a_correr:
    print("""
    "----------MENU----------"
    "(1) Criar Lista"
    "(2) Ler Lista"
    "(3) Soma"
    "(4) Média"
    "(5) Maior"
    "(6) Menor"
    "(7) estaOrdenada por ordem crescente"
    "(8) estaOrdenada por ordem decrescente"
    "(9) Procura um elemento"
    "(0) Sair""")

    try:
        modo = int(input("Escolha a operação: "))
    except ValueError:
        print("Opção inválida! Introduza um número.")
        continue

    if modo == 1:
        lista = criarLista()
        print("Lista guardada:", lista)

    elif modo == 2:
        lista = lerLista()
        print("Lista guardada:", lista)

    elif modo == 3:
        if len(lista) == 0:
            print("A lista está vazia! Crie ou leia uma lista primeiro.")
        else:
            print("A soma dos elementos é:", soma(lista))

    elif modo == 4:
        if len(lista) == 0:
            print("A lista está vazia! Crie ou leia uma lista primeiro.")
        else:
            print("A média dos elementos é:", media(lista))

    elif modo == 5:
        if len(lista) == 0:
            print("A lista está vazia!")
        else:
            print("O maior elemento é:", maior(lista))

    elif modo == 6:
        if len(lista) == 0:
            print("A lista está vazia!")
        else:
            print("O menor elemento é:", menor(lista))

    elif modo == 7:
        if len(lista) == 0:
            print("A lista está vazia!")
        else:
            print("Está ordenada por ordem crescente?", estaOrdCres(lista))

    elif modo == 8:
        if len(lista) == 0:
            print("A lista está vazia!")
        else:
            print("Está ordenada por ordem decrescente?", estaOrdDecres(lista))

    elif modo == 9:
        if len(lista) == 0:
            print("A lista está vazia!")
        else:
            num = int(input("Qual é o elemento que quer procurar? "))
            pos = procElem(lista, num)

            if pos != -1:
                print("Elemento encontrado na posição:", pos)
            else:
                print("Elemento não encontrado:", pos)

    elif modo == 0:
        print("A terminar a aplicação...")
        print("Lista guardada no momento:", lista)
        a_correr = False

    else:
        print("Opção inválida! Tente novamente.")