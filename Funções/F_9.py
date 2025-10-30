# Converção de Cº para Fº

def converter(temp):
    return temp * 1.8 + 32

def main():
    temp_f = converter(float(input('Informe a Temperatura' \
    'em Cº ')))
    print(f'A temperatura em é Fº {temp_f}')

main()