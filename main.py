from grafo import Grafo
from aestrela import AEstrela

if __name__ == "__name__":
    grafo = Grafo()
    busca_aestrela = AEstrela(grafo.bucharest)
    busca_aestrela.buscar(grafo.arad)
