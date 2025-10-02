
# (random) é uma biblioteca de numero

import random

s=random.randint(1,100)
e=0
t=0

while True: 
    e = int(input('informe um numero! '))
    t+=1

    if e==s:
        print(f'PARABÉNS VOCÊ ACERTOU COM {t} TENTATIVAS!!!') 
        break
    elif e < s:
        print(f'O numero {e} é menor que o numero secreto!')
    elif e > s:
        print(f'O numero {e} é maior que o numero secreto!')
    