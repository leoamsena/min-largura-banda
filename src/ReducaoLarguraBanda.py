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

    @staticmethod
    def gerarGrafoNx(nome):
        """
        Parameters
        ----------
        nome: str
            Nome do arquivo .mkt que contem a matriz do grafo 
            que se deseja inicializar um objeto da classe
            da biblioteca NetworkX
        Returns
        -------
        grafo
            Objeto da classe NetworkX que representa um grafo
        """
        matriz = mmread(nome + ".mtx")

        simetrica = ReducaoLarguraBanda.ehSimetrica(matriz)
        if (not simetrica):
            matriz += matriz.transpose()
        # print(matriz)

        grafo = nx.from_scipy_sparse_matrix(matriz)
        return grafo, simetrica
    

    @staticmethod
    def calcularLarguraBanda(grafo):
        matriz = nx.to_scipy_sparse_matrix(grafo)
        naoZeros = matriz.nonzero()
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

    @staticmethod
    def ehSimetrica(a):
        if a.shape[0] != a.shape[1]:
            raise Exception("Matriz não quadrada!")
        return np.allclose(a.A, (a.transpose()).A)

    @staticmethod
    def reverseCuthillMckee(grafo):
        lista_permutacao = list(reverse_cuthill_mckee_ordering(
            grafo))
        return nx.Graph(nx.adjacency_matrix(grafo, nodelist=lista_permutacao))

    @staticmethod
    def salvarImagem(grafo, nome, path):
        matriz = nx.to_scipy_sparse_matrix(grafo)
        plt.spy(matriz)
        plt.savefig(
            path+"/"+nome+".png")
        plt.cla()
