m=int(input('informe até qual numero vc que! '))
r=int(input('Qual multiplicardo vai ser escolido? '))

for n in range(m+1):
    if n % r==0:
        print(n)