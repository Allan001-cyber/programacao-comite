

ps=input('informe a palavra secreta! ')
penct=['_'] * len(ps)
ct=''
tttvs=10

for tttv in range(tttvs+1):
    ct=input(f'Chute uma letra {penct} ->')

    for t in range(len(ps)):
        if ps[t]==ct:
            penct[t]=ct

    if '_' not in penct:
        print('Você venceu!!!!')
        break

    print(f'Faltam apenas {tttvs-tttv} tentativas')


else:
    print(f'Você perdeu, a palavra era {ps}')