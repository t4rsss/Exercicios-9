import pickle

numeros = [1, 2, 3, 4, 5]

with open("dados.bin", "wb") as arq:
    pickle.dump(numeros, arq)

with open("dados.bin", "rb") as arq:
    dados_lidos = pickle.load(arq)
    print("Números do arquivo binário:", dados_lidos)
