class Somador:
    def __init__(self, indice):
        self.indice = indice
        self.soma = 0
        self.k = 0

    def calcular_soma(self):
        while self.k < self.indice:
            self.k += 1
            self.soma += self.k
        return self.soma
