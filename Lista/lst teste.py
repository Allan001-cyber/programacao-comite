# Teste 1 com ( while )

# mtz=[]
# qntd=4

# while qntd>=0:
#     mtz.append(int(input('infome um numero! ')))
#     qntd -=1
    
# max_nm= max(mtz)
# min_nm= min(mtz)
# md= sum(mtz)

# print(f'{mtz}\nO maior numero é {max_nm}\nO menor é {min_nm }\nA media é {md/5}')


# Teste 2 com ( for ) 

nmr=[]
for i in range(5):
    nmr.append(int(input(f'Informe o {i+1}º numero -> ')))

print(f'Os numeros digitados foram ', end=' ')
for i in nmr:
    print(i, end=' ')
print(f'\nO maior numero digitado é {max(nmr)}')
print(f'O menor numero digitado é {min(nmr)}')
print(f'A media dos numeros digitados é {sum(nmr)/len(nmr) }')