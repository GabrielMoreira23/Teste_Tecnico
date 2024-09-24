class FaturamentoPorEstado:
    def __init__(self, faturamento_estados):
        self.faturamento_estados = faturamento_estados

    def total_faturamento(self):
        return sum(self.faturamento_estados.values())

    def calcular_percentuais(self):
        total = self.total_faturamento()
        return {estado: (valor / total) * 100 for estado, valor in self.faturamento_estados.items()}
