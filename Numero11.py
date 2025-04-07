class Contador:
    def __init__(self, limite):
        self.limite = limite
        self.atual = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.atual < self.limite:
            self.atual += 1
            return self.atual
        else:
            raise StopIteration

n = int(input("Contar até: "))
for numero in Contador(n):
    print(numero)
