sld=5000
sqm=1

print(f' Seu saldo é {sld}')

# Teste 1


# while sqm!=0:
#     sqm = float(input('informe o valor do saque! '))
#     sld -= sqm
#     print(f' Seu saldo é {sld}')

# Teste 2

while sld>=0:
    sqm = float(input('informe o valor do saque! '))
    sld -= sqm
    print(f' Seu saldo é {sld}')