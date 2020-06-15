from random import sample
import numpy as np

class Mega(object):
    def __init__(self):
        self.quantidade_de_jogos = int(input('Quantos jogos deseja fazer ? : '))
        self.quantidade_de_dezenas = 6
        self.quantidade_de_numeros = 60
        self.cria_jogos()


    def cria_jogos(self):
        self.todos_jogos = [sample(range(1,self.quantidade_de_numeros + 1),self.quantidade_de_dezenas) for x in range(self.quantidade_de_jogos)]


    def exibir_jogos(self):
        for indice, valor in enumerate(self.todos_jogos,1):
            print(f'Jogo {indice}: {valor}')

    def contagem_de_numeros(self):
        contagem , _ = np.histogram([dezena for dezena in [jogo for jogo in self.todos_jogos]], range(1,self.quantidade_de_numeros + 2))
        self.lista =  [(dezena,frequencia) for dezena, frequencia in enumerate(contagem[1:],1)]

        return [(dezena,frequencia) for dezena, frequencia in enumerate(contagem[:],1)]

    def valor_mais_repetido(self):
        self.lista_mais_repetidos = []
        for indice, valor in enumerate(self.lista):
            if (max(int(numero) for indice ,numero in self.lista)) == valor[1]:
                 print(f'O numero {indice} foi o que mais se repetiu , {valor[1]} vezes ')
                 self.lista_mais_repetidos.append([indice,valor[1]])
        return  self.lista_mais_repetidos

    def exibir_contagem(self):
        for dezena,frequencia in self.contagem_de_numeros():
            print(f'Número {dezena} ocorreu {frequencia} vezes ')
        print(f'Para um total de {self.quantidade_de_jogos}')
        self.valor_mais_repetido()


m = Mega()
m.exibir_jogos()
m.exibir_contagem()
