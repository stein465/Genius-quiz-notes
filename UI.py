import os
import time
def interface():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("_________________________GENIUS QUIZ NOTAS MUSICAIS_______________________ \n \n")

    print("Como jogar: ")
    print("1- Esse é um jogo para treinar as habilidades auditivas em relação as notas musicais juntamente com um treino de memória")
    print("2- Será informado ao jogador qual a primeira nota está sendo tocada")
    print("3- Logo após o jogo irá tocar uma outra nota e perguntará ao jogador quais notas foram tocada sequencialmente")
    print("4- A cada acerto, o jogo irá adicionar uma nota a mais para ser tocada")
    print("5- Caso o jogador erre 3 vezes seguidas, o jogo encerrará \n \n")


    input("Aperte qualquer tecla para continuar\n\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Cada letra representa uma nota: \n\n")
    print(" Dó  = c")
    print(" Ré  = d")
    print(" Mi  = e")
    print(" Fá  = f")
    print(" Sol = g")
    print(" Lá  = a")
    print(" si  = b")

    input("\n\nAperte qualquer tecla para continuar")
    os.system('cls' if os.name == 'nt' else 'clear')

def limpar_tela():
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')





