def contar_pares(n):
    for i in range(0, n+1, 2):
        yield i

n = int(input("Gerar pares até: "))
for par in contar_pares(n):
    print(par)
