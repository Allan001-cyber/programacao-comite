qtd_p=0

for n in range(1, 1000):
    n_vzs_div=0

    for n2 in range(1,n+1):
        if n % n2 == 0:
            n_vzs_div += 1

    if n_vzs_div == 2:
        print(f'Numero primo {n}')
        qtd_p +=1

    if qtd_p == 20:
        break