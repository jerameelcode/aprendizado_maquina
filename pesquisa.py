# Algorítmo de Kruskal em Python
# Dado um grafo não orientado conectado, uma árvore de extensão
# deste grafo é um subgrafo o qual é uma árvore que conecta 
# todos os vértices. Um único grafo pode ter diferentes 
# árvores de extensão.
from collections import defaultdict
 
# Representação do grafo
 
class Grafo:
 
    def __init__(self, vertices):
        self.V = vertices  # Nº. de vertices
        self.grafo = []  # dicionário padrão
        # to store grafo
 
    # Função para adicionar borda ao grafo
    def addBorda(self, u, v, w):
        self.grafo.append([u, v, w])
 
    # A utilidade da function buscar um elemento i dentro de uma collection
    # utilizando a técnica de compressão de caminho
    def buscar(self, parente, i):
        if parente[i] == i:
            return i
        return self.buscar(parente, parente[i])
 
    # A função une duas coleções por ranqueamento
    def unir(self, parente, rank, x, y):
        xraiz = self.buscar(parente, x)
        yraiz = self.buscar(parente, y)
 
        # Colocar o menor rank da arvore abaixo da 
        # raiz de maior rank (unir pelo rank)
        if rank[xraiz] < rank[yraiz]:
            parente[xraiz] = yraiz
        elif rank[xraiz] > rank[yraiz]:
            parente[yraiz] = xraiz
 
        # Se os ranks são iguais então um deles se torna raiz
        # e incrementa seu rank por 1
        else:
            parente[yraiz] = xraiz
            rank[xraiz] += 1
 
    # A função principar constroe MST ou Árvore de Expansão Mínima utilizando o algorítmo de Kruskal
    def KruskalMST(self):
 
        resultado = []  # Isto armazena o MST ou ARM resultadoado  
         
        # Indice utilizado para Bordas ordenadas
        i = 0
         
        # Variável indice, utilizada por resultado[]
        e = 0
 
        # Passo 1: Ordenar todas as bordas em
        # ordem crescente de pesos
        # Cria uma cópia do grafo para não alterá-lo
        self.grafo = sorted(self.grafo,
                            key=lambda item: item[2])
 
        parente = []
        rank = []
 
        # Cria V subsets com elementos individuais
        for o_no in range(self.V):
            parente.append(o_no)
            rank.append(0)
 
        # Número de Bordas Bordas a serem tomadas para V-1
        while e < self.V - 1:
 
            # Passo 2: Pegar a menos borda e incrementar o
            # indice para a próxima iteração
            u, v, w = self.grafo[i]
            i = i + 1
            x = self.buscar(parente, u)
            y = self.buscar(parente, v)
 
            # Se incluir esta borda não cria um ciclo
            # incluir no resultado
            # e incrementa o indice de resultado
            # para a próxima borda
            if x != y:
                e = e + 1
                resultado.append([u, v, w])
                self.unir(parente, rank, x, y)
            # Senão, descartar a borda
 
        minimumCost = 0
        print ("Bordas in the constructed MST")
        for u, v, weight in resultado:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree" , minimumCost)
 
# Codigo de definição
g = grafo(4)
g.addBorda(0, 1, 10)
g.addBorda(0, 2, 6)
g.addBorda(0, 3, 5)
g.addBorda(1, 3, 15)
g.addBorda(2, 3, 4)
 
# Function call
g.KruskalMST()
 
# This code is contributed by Neelam Yadav
