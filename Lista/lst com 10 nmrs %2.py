import random

nmr=[]
nmrp=[]

for i in range(10):
    nmr.append(random.randint(1,100))
    
for i in nmr:
    if i % 2==0:
       nmrp.append(i)

print('lst org:', *nmr)
print('lst de nmrs prs:', *nmrp)





#nmr.append(int(input(f'Informe o {i+1}º numero -> ')))
    
    