from Entidades import jogadores

# -------------- # DECLARAÇÃO DE NÓ
class NodoArvore:
    def __init__(self, chave=jogadores):
        self.chave = chave
        self.esquerda = None
        self.direita = None
    def getchave(self):
        return self.chave

    def setchave(self, chave):
        self.chave = chave

    def getEsquerda(self):
        return self.esquerda

    def setEsquerda(self, esquerda):
        self.esquerda = esquerda

    def getDireita(self):
        return self.direita

    def setDireita(self, direita):
        self.direita = direita
    def __str__(self):
      return "NOME: " + str(self.chave)

# --------------DECLARAÇÃO DA ARVORE
class ArvoreBinariaBusca:
    def __init__(self):
        self.root = None

    def insert(self, chave):
        novo_no = NodoArvore(chave)

        if self.empty():            #verifica se a arvore está vazia
            self.root = novo_no
        else:                       # se não vazia, insere recursivamente
            no_raiz = None
            no_aux = self.root

            while (True):
                if no_aux != None:                                                   #se o nó verificado não for nulo
                    no_raiz = no_aux                                                 # nó verificado se torna o pai (ou raiz)
                    if novo_no.getchave().pontuacao < no_aux.getchave().pontuacao:   # se a pontuação do novo nó for menor que o nó verificado, vai para esquerda
                        no_aux = no_aux.getEsquerda()
                    else:                                        # se não, vai para direita
                        no_aux = no_aux.getDireita()
                else:                                            # se o no verificado for nulo, é inserido o novo nó

                     if novo_no.getchave().pontuacao < no_raiz.getchave().pontuacao:    # se a pontuação do novo no for menor que a verificada, novo é botado a esquerda
                        no_raiz.setEsquerda(novo_no)

                     else:                                                              # se a pontuação do novo no for maior que a verificada, novo é botado a esquerda
                        no_raiz.setDireita(novo_no)

                     break # sair do loop

    def empty(self):
        if self.root == None:
            return True
        return False

    #----------------- MANEIRAS DE PERCORRER A ARVORE ------------#
    def emOrdem(self, atual):
        if atual != None:
            self.emOrdem(atual.esquerda)
            print(atual.chave, end="\n")
            self.emOrdem(atual.direita)

    def preOrdem(self, atual):
        if atual != None:
            print(atual.chave, end="\n")
            self.preOrdem(atual.esquerda)
            self.preOrdem(atual.direita)

    def posOrdem(self, atual):
        if atual != None:
            self.posOrdem(atual.esquerda)
            self.posOrdem(atual.direita)
            print(atual.chave, end=" \n")

# ------------ ACHAR FOLHA A DIREITA ----------------
    def maxx(self, atual):
        anterior = None
        while atual is not None:
            anterior = atual
            atual = atual.direita
        return anterior

#------------ RETORNAR A RAIZ DA ARVORE -------------
    def getRoot(self):
        return self.root






