# Calculadora





def calculo(a,b,c):
    

    while a != 'sair':
     for i in b:
        if i == '+':
           d = a + c
        elif i == '-':
           d = a - c
        elif i == '*':
           d = a * c
        elif i == '%':
           d = a % c
        elif i == '/':
           d = a / c
        print(d)
        a = input('Primeiro numero! ')
        if a.isdigit():
            a = float(a)
        else:
            print('Opção invalida!')

        b = input('infome a variavel! ')

        c = input('Segundo numero! ')
        c = input('Segundo numero! ')
        if c.isdigit():
            c = float(c)
        else:
            print('Opção invalida!')

        break
     
def main():
    a = input('Primeiro numero! ')
    if a.isdigit():
       a = float(a)
    else:
       print('Opção invalida!')

    b = input('infome a variavel! ')

    c = input('Segundo numero! ')
    if c.isdigit():
       c = float(c)
    else:
       print('Opção invalida!')
    
    resposta = calculo(a,b,c)
    print(resposta)
main()