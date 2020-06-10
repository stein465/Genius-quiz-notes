class jogadores():


    def __init__(self, nome = None, pais = None, pontuacao = None):
        self.nome = nome
        self.pais = pais
        self.pontuacao = pontuacao

    def __str__(self):
      return "NOME: " + str(self.nome) + "        \PAÍS: " + str(self.pais) + "        \PONTOS: " + str(self.pontuacao)
