def multiplicador(fator):
    def multiplicar(n):
        return n * fator
    return multiplicar

dobro = multiplicador(2)
triplo = multiplicador(3)

print(dobro(10))  # 20
print(triplo(10)) # 30
