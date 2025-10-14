cord=[]
cont=0

# Criar coordenadas

for lnh in range(3):
    temp=[]
    for cln in range(2):
        temp.append(cont+1)
        cont+=1
    
    cord.append(tuple(temp))

cord=tuple(cord)
print(cord,'\n')

# Forma 1

for l in cord:
    cont=0
    x=0
    y=0

    for c in l:
        if cont==0:
            x=c
        else:
            y=c
        cont+=1
    print(f'Ponto: x={x}, y={y}')

print()

# Forma 2

for linha in cord:
    print(f'Ponto: x={linha[0]}, y={linha[1]}')

print()

# Forma 3

for d,e in cord:
    print(f'Ponto: x={d}, y={e}')
