import json

class FaturamentoDistribuidora:
    def __init__(self, arquivo_json):
        with open(arquivo_json, 'r') as f:
            self.dados = json.load(f)
        self.faturamento = [dia["valor"] for dia in self.dados["faturamento_diario"] if dia["valor"] > 0]

    def menor_faturamento(self):
        return min(self.faturamento)

    def maior_faturamento(self):
        return max(self.faturamento)

    def media_mensal(self):
        return sum(self.faturamento) / len(self.faturamento)

    def dias_acima_media(self):
        media = self.media_mensal()
        return sum(1 for valor in self.faturamento if valor > media)
