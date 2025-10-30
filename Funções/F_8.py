# Contador de letras!

def contagende_caracterios(palavra):
    return len(palavra)

def main():
    tamanho = contagende_caracterios(input('Digite uma palavra! '))
    print(f'A palavra tem {tamanho} caracterios')

main()