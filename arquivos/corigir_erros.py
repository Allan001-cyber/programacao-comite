
try:
    with open("arquivos/arquivo_teste/    _linha.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("Arquivo nao encontrado!")