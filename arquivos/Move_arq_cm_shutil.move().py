from shutil import move

def mover():
    move('arquivos/arquivo_teste/pasta/bkp_copy_Teste=1.py','bkp_copy_Teste=1.py')
    print('Movido com sucesso!')

def main():
    mover()
main()