r=int(input('Qual seria o multiplicador? '))

for n in range(101):
    if n % r==0:
        print(n)