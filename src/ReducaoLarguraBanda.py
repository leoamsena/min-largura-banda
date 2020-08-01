from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import reverse_cuthill_mckee
import scipy as sp
import networkx as nx
from networkx.utils import reverse_cuthill_mckee_ordering
import matplotlib.pyplot as plt
from scipy.io import mmread
import numpy as np


class ReducaoLarguraBanda:
    """
    Classe para definir as propriedades e métodos a serem usados 
    afim de otimizar a solução.

    Attributes
    ----------
    grafo: scipy.sparse.csr.csr_matrix
        Grafo original em formato scipy
    nxGrafo: networkx.classes.graph.Graph
        Grafo original em formato networkx

    """

    def __init__(self, nome):
        """
        Parameters
        ----------
        nome: str
            Nome do arquivo .mkt que contem a matriz do grafo 
            que se deseja reduzir a largura de banda
        """
        matriz = mmread(nome+".mtx")

        #self.grafo = csr_matrix(matriz_adj)

        if (not self.ehSimetrica(matriz)):
            print("NAO E SIMETRICA")
            matriz += matriz.transpose()

        self.nxGrafo = nx.from_scipy_sparse_matrix(matriz)

    def calcularLarguraBandaInicial(self):
        return self.calcularLarguraBanda(nx.to_scipy_sparse_matrix(self.nxGrafo))

    def calcularLarguraBanda(self, grafo):
        naoZeros = grafo.nonzero()
        maior = -9999999999
        ultimaLinha = -1
        for i in range(len(naoZeros[0])):
            linhaAtual = naoZeros[0][i]
            if (ultimaLinha != linhaAtual):
                ultimaLinha = linhaAtual
                larguraBandaLinha = naoZeros[0][i] - naoZeros[1][i]
                if (larguraBandaLinha > maior):
                    maior = larguraBandaLinha
        return maior

    def ehSimetrica(self, a):
        if a.shape[0] != a.shape[1]:
            raise Exception("Matriz não quadrada!")
        return np.allclose(a.A, (a.transpose()).A)

    def salvarImagemAntes(self, nome):
        self.salvarImagem(nx.to_scipy_sparse_matrix(
            self.nxGrafo), nome, "before")

    def reverseCuthillMckee(self, framework="nx"):
        if (framework == "nx"):
            lista_permutacao = list(reverse_cuthill_mckee_ordering(
                self.nxGrafo))
            return nx.to_scipy_sparse_matrix(self.nxGrafo, nodelist=lista_permutacao)

    def salvarImagem(self, grafo, nome, path):
        plt.spy(grafo)
        plt.savefig(
            "/home/leoamsena/UFLA-2020-1/CPA/trab 4//images/"+path+"/"+nome+".png")
        plt.cla()
