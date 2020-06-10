import pygame
import Entidades
import os
import operator
import ArvoreBinariaBusca
from ArvoreBinariaBusca import ArvoreBinariaBusca,NodoArvore
from UI import interface, limpar_tela
from metodos import tocar, iniciar,perguntar
pygame.init()
notas = ('c', 'd', 'e', 'f', 'g', 'a','b')
lista = []
ranking = ArvoreBinariaBusca()
asr ='sim'

interface()
while asr == 'sim':
        os.system('cls' if os.name == 'nt' else 'clear')
        terminarPartida = False
        nome = input("Digite seu nome: ")
        pais = input("Digite seu país: ")
        iniciar(lista, notas)
        while len(lista) < 10:
            attempt, answer = perguntar(lista,notas)
            if attempt == answer:
                print("\n\n ---------------Acertou!!-------------")
                lista = answer
                limpar_tela()   ## limpar a tela

            else:
                erro = 0
                while attempt != answer:
                    erro += 1
                    if erro>2:
                        print("Perdeu suas chances:")
                        print("Resposta: \n", answer)
                        terminarPartida = True  #terminar partida após 3 erros
                        break
                    print("\n\n ----------- Errado-------------")
                    tocar(answer)
                    attempt = list(input("tente novamente: "))

                if terminarPartida == True:  #terminar partida após 3 erros
                    break
                print("\n\n ---------------Acertou!!-------------")
                lista = answer
                limpar_tela() ## limpar tela após acertar
        pontuacao = ((len(lista)) - 1) *10
        jogador = Entidades.jogadores(nome, pais, pontuacao)
        ranking.insert(jogador)
        print("Dados da partida:")
        print(jogador)
        asr = input("\n Quer outra partida?   sim / nao \n")

# FIM DA RODADA E MOSTRA DO RESULTADOS
print("__________RANKING________")

ranking.emOrdem(ranking.getRoot())

print("\n---------VENCEDOR DA RODADA-----------")

vencedor = ranking.maxx(ranking.getRoot())            #FOLHA A DIREITA
print(vencedor)
print("---- PARABENS------")
print(":D :D :D :D")



