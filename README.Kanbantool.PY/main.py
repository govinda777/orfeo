from kanbantool import *

def main():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação (3) Teste New")

    item = int(input("Qual item? "))

    if(item == 1):
        print("Jogando forca")
        forca.jogar()
    elif(item == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar()
    elif(item == 3):
        print("List Boards")
        board.list()

if(__name__ == "__main__"):
    main()