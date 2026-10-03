vez = input("""Quem chegar ao número 100 somando números de 1 a 10 à vez ganha!
Quem joga primeiro? eu/tu : """)

def jogar1():
    total = 0

    num = int(input("Quanto jogas? "))
    while num > 10 or num < 1:
        print("Tenta outra vez")
        num = int(input("Quanto jogas? "))

    lista = [1, 12, 23, 34, 45, 56, 67, 78, 89]
   
    while total < 100:
        total = total + num
        if total == 100:
            print("O total é 100! Venceste o jogo!")
            break
        if total >=100:
            print("O total é maior que 100! Perdeste o jogo!")
            break
    
        if total in lista:
            total = total + 10
            print(f"Eu jogo 10. total = {total}")
        else:
            resto = total % 11
            if resto == 0:
                total = total + 1
                print(f"Eu jogo 1. total = {total}")
            else:
                ad = 12 - resto
                total = total + ad
                print(f"Eu jogo {ad}. total = {total}")
        if total == 100:
                print("Perdeste! total = 100")
                break        
        num = int(input("Quanto jogas? "))
        while num > 10 or num < 1:
                    print("Tenta outra vez")
                    num = int(input("Quanto jogas? "))
    
    
         

def jogar2():
    print("Eu jogo 1. total = 1")
    total = 1

    jogada = int(input("Quanto jogas? "))
    while jogada > 10 or jogada < 1:
        print("Tenta outra vez")
        jogada = int(input("Quanto jogas? "))

    while total < 100:
        print(f"Neste momento, total = {total+jogada}")
        total = total + jogada
        ad = 11 - jogada
        total = total + ad
        print(f"Eu jogo {ad}. total = {total}")
        if total == 100:
            print("Perdeste! total = 100")
            break
        jogada = int(input("Quanto jogas? "))
        
    
if vez == "eu":
    jogar1()
elif vez == "tu":
    jogar2()


