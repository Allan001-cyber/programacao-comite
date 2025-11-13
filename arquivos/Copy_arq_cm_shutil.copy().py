# Pode se usar assim tambem ( from shutil import copy )




import shutil

def copy_arq():
    try:
        shutil.copy('Teste=1.py', 'arquivos/arquivo_teste/pasta/bkp_copy_Teste=1.py')
        print('Arquivo copiado com sucesso!')
    except FileNotFoundError:
        print('Arquivo ja foi copiado')

def main():
    copy_arq()
main()