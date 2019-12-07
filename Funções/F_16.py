def comprimento(nome,idade):
    return f'Ola {nome}, para bem pelos {idade} anos! '

def main():
    nome = input('Qual seu nome? ')
    idade = int(input('Qual sua idade? '))

    boas_vindas = comprimento(nome,idade)
    print(boas_vindas)
main()