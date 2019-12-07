
ano =2025

def idade(id):
    return ano-id


def main():
    id =int(input('Qual sua data de nacimento? '))
    n = idade(id)
    print(f'Você tem {n} anos.')
main()
  


