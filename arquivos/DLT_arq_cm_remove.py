# Pra remover deve guiar o ( os.remove() ) até a pasta desse jada

# exemplo:  
# Teste com esta fomula abaixo!
# arquivos/arquivo_teste/Primeira_linha.txt

import os

def removee(pasta):
    try:
        os.remove(pasta)
        print("Arquivo removida com sucesso!")
    except FileNotFoundError:
        print("Arquivo, não existe ou ja foi apagado!")


def main():
    removee(input("Qual Arquivo vamos apagar! "))


main()

