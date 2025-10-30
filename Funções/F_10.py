# Calculando o fatorial
def calcular_fatorial_for(n):
    fatorial = 1
    if n < 0:
        return "O fatorial não é definido para números negativos"
    elif n == 0:
        return 1
    else:
        for i in range(1, n + 1):
            fatorial = fatorial * i
        return fatorial

# Exemplo de uso
numero = int(input('Imforme um numero! '))
print(f"O fatorial de {numero} é {calcular_fatorial_for(numero)}")
