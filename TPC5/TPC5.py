turma = []
aluno = ()
def criar_turma():
    turma = []
    return turma
    
def ins_aluno(turma):
    nome = input("Insere o nome do aluno: ")
    id = input("Insere o id do aluno (ex: a1234): ")
    notaTPC = float(input("Quanto teve esse aluno no TPC? "))
    notaProj = float(input("Quanto teve esse aluno no Projeto? "))
    notaTeste = float(input("Quanto teve esse aluno no Teste? "))
    aluno = (nome, id, [notaTPC, notaProj, notaTeste])
    turma.append(aluno)
    return turma

def listar_turma(turma): 
    if turma == []:
        print("Insere primeiro alunos à turma")
    else:
        for aluno in turma:
            print(f"Nome: {aluno[0]} | ID: {aluno[1]} | Notas: {aluno[2]}")
    
def consultar_aluno(turma):
    encontrado = False
    con = input("Introduza o id do aluno que quer consultar: ")
    for aluno in turma:
        if aluno[1] == con:
            encontrado = True
            print(f"""O aluno cujo id é {con} é o/a {aluno[0]} e as notas dele/a são:
            TPC = {aluno[2][0]}
            Projeto = {aluno[2][1]}
            Teste = {aluno[2][2]}""")
    if encontrado == False:
        print("Aluno não encontrado...")

def guardar_turma(turma):
    ficheiro = open("turma.txt", "w")
    for aluno in turma:
        ficheiro.write(f"{aluno[0]}|{aluno[1]}|{aluno[2][0]}|{aluno[2][1]}|{aluno[2][2]}\n") 
    ficheiro.close()   

def carregar_turma():
    ficheiro = open("turma.txt", "r")
    turma2 = []
    for linha in ficheiro:
        linha = linha.strip()
        campos = linha.split("|")
        aluno = (campos[0], campos[1], [float(campos[2]), float(campos[3]), float(campos[4])])
        turma2.append(aluno)
    ficheiro.close()
    return turma2

a_correr = True
while a_correr:
    print("""
    ==========MENU==========
    "(1) Criar turma"
    "(2) Inserir aluno na turma"
    "(3) Listar a turma"
    "(4) Consultar um aluno por id"
    "(5) Guardar turma em ficheiro"
    "(6) Carregar a turma de um ficheiro"
    "(0) Sair da aplicação"
    """)

    modo = input("Escolha a operação: ")
    if modo == "0":
        print("A terminar a aplicação...")
        print("A turma está guardada no ficheiro turma.txt")
        a_correr = False
    elif modo == "1":
        turma = criar_turma()
        print("Turma criada.")
    elif modo == "2":
        ins_aluno(turma)
    elif modo == "3":
        listar_turma(turma)
    elif modo == "4":
        consultar_aluno(turma)
    elif modo == "5":
        guardar_turma(turma)
    elif modo == "6":
        turma = carregar_turma()
    else:
        print("Opção inválida, tenta novamente...")
