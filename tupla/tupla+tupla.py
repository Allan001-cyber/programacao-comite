mtz=((1,2,3),(4,5,6),(7,8,9))

print(mtz[1][1])

for linha in mtz:
    for coluna in linha:
        print(coluna, end='')
    print()
