import random
import sys

#Opção 1
def jogo1 ():
    num = random.randint(0, 100)
    tentativas = 1
    numesc = int(input("Tenta adivinhar um número entre 0 e 100: "))

    while num != numesc:
        if numesc > num:
            print("O número que pensei é menor...")
        elif numesc < num:
            print("O número que pensei é maior...")
        numesc = int(input("Tenta adivinhar um número entre 0 e 100: "))
        tentativas = tentativas + 1
    print(f"Acertaste! Foram precisas {tentativas} tentativas!")
    sys.exit()
    
#Opção 22

def jogo2 ():
    tries = 1
    min = 0
    max = 100 

    num1 = random.randint(min, max) 
    resposta = input(f"O número é {num1}? ")

    while resposta != "Acertaste":
        tries = tries + 1
        if resposta == "O número que pensei é menor":
            max = num1 - 1 
        elif resposta == "O número que pensei é maior":
            min = num1 + 1  
        num1 = random.randint(min, max) 
        resposta = input(f"O número é {num1}? ")
    print(f"Boa! Precisei de {tries} tentativas!")
    sys.exit()
            

mod = int(input("""Escolhe qual modalidadde queres jogar: 
1 - O Computador escolhe, tu adivinhas; 
2 - O Computador adivinha, tu escolhes. 
:"""))

if mod == 1:
    jogo1()
elif mod == 2:
    jogo2()
else:
    sys.exit()






