class InversorString:
    def __init__(self, string):
        self.string = string

    def inverter(self):
        invertida = ''
        for i in range(len(self.string) - 1, -1, -1):
            invertida += self.string[i]
        return invertida
