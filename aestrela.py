from vetor import vetorOrdenado


class AEstrela:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.encontrado = False

    def buscar(self, atual):
        print('-----')
        print("Atual: {}".format(atual.rotulo))
        atual.visitado = True

        if atual == self.objetivo:
            self.encontrado = True
        else:
            vetor_ordenado = vetorOrdenado(len(atual.adjacentes))
            for adjacente in atual.adjacentes:
                if not adjacente.vertice.visitado:
                    adjacente.vertice.visitado = True
                    vetor_ordenado.insere(adjacente)
                vetor_ordenado.imprime()

                if vetor_ordenado.ultima_posicao > 0:
                    proximo = vetor_ordenado.valores[0].vertice
                    if proximo is not None:
                        self.buscar(proximo)
