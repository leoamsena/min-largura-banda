from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import reverse_cuthill_mckee
import scipy as sp
import networkx as nx
from networkx.utils import reverse_cuthill_mckee_ordering
import matplotlib.pyplot as plt


matriz_adj = [
    [0, 1, 2, 0],
    [0, 0, 0, 1],
    [2, 0, 0, 3],
    [0, 0, 0, 0]
]
print(type(matriz_adj))


print("grafo inicial(matriz adj) = ", matriz_adj)

grafo = csr_matrix(matriz_adj)
print(type(grafo))


graph = nx.from_scipy_sparse_matrix(grafo)
print("graph = ", type(graph))

rcm = list(reverse_cuthill_mckee_ordering(
    graph))

solution = [nx.to_scipy_sparse_matrix(graph, nodelist=rcm)]

print("solucao = ", solution)


plt.spy(solution)
plt.savefig("teste.png")
plt.cla()
# aux = reverse_cuthill_mckee(grafo)

# print("aux = ", aux)


# print("solução = ",solution)
