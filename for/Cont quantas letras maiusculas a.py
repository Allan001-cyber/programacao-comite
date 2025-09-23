q=0

p='ABCDEFGHIJKLMNOPQRSTUVWYZ'

v=input('informe uma letra ')

for lt in v:
   for l in p:
    if lt ==l:
      q+=1

print(q)