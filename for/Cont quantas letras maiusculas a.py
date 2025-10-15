

#p='ABCDEFGHIJKLMNOPQRSTUVWYZ'

q=0
p='abcdefghijklmnopqrstuvwyz'

v=input('informe uma letra ')

for lt in v:
   for l in p:
    if lt ==l:
      q+=1

print(q)