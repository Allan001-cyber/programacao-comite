# Lista de Numeros pares!

# Função defini o que numero par!
def pares(a):
    par=[]
    for b in a:
        if b % 2 ==0:
            par.append(b)

    return par 

# Define ate que numero a Fução deve ir, e mostra pro ossuario com ( main() ) 
def main():
    a = range(1,100)
    lista_final = pares(a)

    for n in lista_final:
        print(n,end=' ')
    print()
main()