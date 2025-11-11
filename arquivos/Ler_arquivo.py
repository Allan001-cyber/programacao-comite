
with open("arquivos/arquivo_teste/Lista_de_fruta.txt") as f:
    frutas = f.readlines()
    for fruta in frutas:
        print(fruta.strip())
      