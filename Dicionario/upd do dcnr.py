# Exercicio 1

crr={
    'Marca':'Ford',
    'Modelo':'Eco Sport',
    'Ano':'2005'
}
print(crr)
print('----')

# Exercicio 2

crr.update({'Ano':'2022'})
print(crr)
print('----')

# Exercicio 3

del crr['Modelo']
print(crr)
print('----')

# Exercicio 4 com resultado

print(crr.get('Ano'))
print()
# Exercicio 4 sem resultado

print(crr.get('Modelo'))
print()

# Exercicio 5 com resultado

print(crr.keys())
print()

# Exercicio 5 sem resultado

for r in crr.keys():
    print(f'chave {r}|', end=' ',)

print('\n')

# Exercicio 5 com resultado

print(crr.values())
print()

# Exercicio 6 sem resultado

for r in crr.values():
    print(f'Chave {r} |', end=' ')

print('\n')

# Exercicio 7 com resultado

print(crr.items())
print()

# Exercicio 7 sem resultado

for r in crr.items():
    print(f'Chave {r} |', end=' ')

print('\n')
