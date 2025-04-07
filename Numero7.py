class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_detalhes(self):
        print(f"{self.marca} {self.modelo}, ano {self.ano}")

carro1 = Carro("Toyota", "Corolla", 2020)
carro2 = Carro("Honda", "Civic", 2022)

carro1.exibir_detalhes()
carro2.exibir_detalhes()
