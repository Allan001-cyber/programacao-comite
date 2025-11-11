
with open("arquivos/arquivo_teste/Primeira_linha.txt", "w") as f:
    f.write("Esta é a primeira linha do arquivo.\n")
    print("arquivos/Primeira_linha.txt criado com sucesso!")
    
with open("arquivos/arquivo_teste/Lista_de_fruta.txt","w") as f:
    f.write(f"Banana\nMaçã\nLaranja\nUva\nAbacaxi\n")
    print("arquivos/Lista_de_fruta.txt criado com sucesso!")