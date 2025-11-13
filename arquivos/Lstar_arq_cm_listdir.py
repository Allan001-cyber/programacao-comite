import os

def Listar_arq():
    items = os.listdir('.')
    for item in items:
        print(item) 


def main():
    Listar_arq()

main()