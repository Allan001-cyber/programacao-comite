# Rescrever palavra de duas formas diferentes!

def re_screva(palavra):
    
    # Formula 1
    # a =''.join(reversed(palavra))
    
    # Formula 2
    a=palavra[::-1]
    return a

def main():
    palavra = input('O que você quer rescreve de tra pra frente? ')

    rescrito = re_screva(palavra)
    print(rescrito)
main()