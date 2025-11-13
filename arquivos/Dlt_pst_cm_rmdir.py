# Pra remover deve guiar o ( os.rmdir() ) até a pasta desse jada

# exemplo: 
# Teste com esta fomula abaixo!
# arquivos/arquivo_teste/pasta

import os

def removee(pasta):
    try:
        os.rmdir(pasta)
        print("Arquivo removida com sucesso!")
    except FileNotFoundError:
        print("Arquivo, não existe ou ja foi apagado!")


def main():
    removee(input("Qual Arquivo vamos apagar! "))


main()