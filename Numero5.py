palavras = input("Digite palavras separadas por espaço: ").split()

print("Lista ordenada:", sorted(palavras))
print("Total de palavras:", len(palavras))
print("Palavras em maiúsculas:", [p.upper() for p in palavras])
