with open("dados.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    print("Número de linhas:", len(linhas))
    print("Conteúdo do arquivo:")
    for linha in linhas:
        print(linha.strip())
