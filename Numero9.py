class Animal:
    def fazer_som(self):
        print("Som genérico")

class Cachorro(Animal):
    def fazer_som(self):
        print("Au au!")

class Gato(Animal):
    def fazer_som(self):
        print("Miau!")

a1 = Cachorro()
a2 = Gato()

a1.fazer_som()
a2.fazer_som()
