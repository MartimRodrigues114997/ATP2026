# TP1

# a) Elementos que não estão em comum às duas listas
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
ncomuns = [n for n in lista1 + lista2 if (n in lista1) != (n in lista2)]
print(ncomuns)  # [1, 2, 3, 6, 7, 8]
# (o "resultado esperado" do enunciado tem uma gralha: falta o 6)

# b) Palavras do texto com mais de 3 letras
texto = """Vivia há já não poucos anos algures num concelho do Ribatejo
    um pequeno lavrador e negociante de gado chamado Manuel Peres Vigário"""

lista_comp = [palavra for palavra in texto.split() if len(palavra) > 3]
print(lista_comp)

# c) Pares (índice, valor), com índice a começar em 1
lista = ['anaconda', 'burro', 'cavalo', 'macaco']
listaRes = [(i + 1, lista[i]) for i in range(len(lista))]

 
print(listaRes)

#TPC2

# a) Número de ocorrências de uma substring, sem sobreposição
def strCount(s, subs):
    count = 0
    i = 0
    while i <= len(s) - len(subs):
        if s[i:i + len(subs)] == subs:
            count += 1
            i += len(subs)     
        else:
            i += 1
    return count

print(strCount("catcowcat", "cat"))  # 2
print(strCount("catcowcat", "cow"))  # 1
print(strCount("catcowcat", "dog"))  # 0


# b) Produto dos 3 menores inteiros da lista
def produtoM3(lista):
    if len(lista) < 3:
        return None             
    ordenada = sorted(lista)    
    primeiro = ordenada[0]
    segundo = ordenada[1]
    terceiro = ordenada[2]
    return primeiro * segundo * terceiro
 
print(produtoM3([12, 3, 7, 10, 12, 8, 9]))


# c) Soma repetida dos dígitos até restar um só dígito
def reduxInt(n):
    while n >= 10:              
        soma = 0
        for digito in str(n):   
            soma = soma + int(digito)
        n = soma                
    return n

print(reduxInt(38))   # 2
print(reduxInt(777))  # 3


# d) Índice da primeira ocorrência de s2 em s1 (-1 se não existir)
def myIndexOf(s1, s2):
    for i in range(len(s1) - len(s2) + 1):
        igual = True
        for j in range(len(s2)):
            if s1[i + j] != s2[j]:
                igual = False
        if igual:
            return i
    return -1

indexOf = myIndexOf  # o enunciado invoca-a com este nome

print(indexOf("Hoje está um belo dia de sol!", "belo"))   # 13
print(indexOf("Hoje está um belo dia de sol!", "chuva"))  # -1


#TPC3

# a) Quantos posts estão registados
def quantosPost(redeSocial):
    return len(redeSocial)


# b) Lista de posts de um autor
def postsAutor(redeSocial, autor):
    resultado = []
    for post in redeSocial:
        if post['autor'] == autor:
            resultado.append(post)
    return resultado


# c) Lista de autores (sem repetições), ordenada alfabeticamente
def autores(redeSocial):
    lista_autores = []
    for post in redeSocial:
        if post['autor'] not in lista_autores:   
            lista_autores.append(post['autor'])
    lista_autores.sort()                      
    return lista_autores


# d) Insere um novo post; o id é calculado a partir dos existentes
def insPost(redeSocial, conteudo, autor, dataCriacao, comentarios):
    ultimo = 0
    for p in redeSocial:
        numero = int(p['id'][1:])   # 'p3' -> 3
        if numero > ultimo:
            ultimo = numero
    novo = {
        'id': 'p' + str(ultimo + 1),
        'conteudo': conteudo,
        'autor': autor,
        'dataCriacao': dataCriacao,
        'comentarios': comentarios,
    }
    redeSocial.append(novo)
    return redeSocial


# e) Remove o post com o id dado
def remPost(redeSocial, id):
    nova_rede = []
    for post in redeSocial:
        if post['id'] != id:            
            nova_rede.append(post)
    return nova_rede


# f) Distribuição de posts por autor
def postsPorAutor(redeSocial):
    distribuicao = {}
    for post in redeSocial:
        autor = post['autor']
        if autor in distribuicao:
            distribuicao[autor] = distribuicao[autor] + 1   
        else:
            distribuicao[autor] = 1                       
    return distribuicao


# g) Posts comentados por um dado autor
def comentadoPor(redeSocial, autor):
    resultado = []
    for post in redeSocial:
        comentou = False
        for comentario in post['comentarios']:
            if comentario['autor'] == autor:
                comentou = True
        if comentou:
            resultado.append(post)
    return resultado
