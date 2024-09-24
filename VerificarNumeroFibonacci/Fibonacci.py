class Fibonacci:
    def __init__(self, numero):
        self.numero = numero

    def pertence_sequencia(self):
        a, b = 0, 1
        while b <= self.numero:
            if b == self.numero:
                return True
            a, b = b, a + b
        return False
