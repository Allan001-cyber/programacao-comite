encerra_vtc = 1900
snh_fim = 9089
opcao = -1
cnd = []
cnt_voto={'Nulo',0}


# Menu principal
while opcao != snh_fim:
    opcao = input('O que deseja fazer? \n' \
    'Opção 1: Cadastra os candidatos! \n' \
    'Opção 2: \n' \
    'Opção 3: \n' \
    'Opção 4: \n' \
    'Opção 0: Sair \n\n' \
    'Opção ->  ')

if opcao == 1:
    qtd_cnd = int(input('Quantos candidatos' \
    'deseja cadastra?  '))
    
    # Laço para cadastrar os cnadidatos
    for c in range(1,qtd_cnd+1):
        cndd = []
        nm_cnd = input(f'Nome do Candidata {c} -> ')
        nmr_cnd = int(input(f'Numero do Candidato {c+1} -> '))

        # Salva os candidatos
        cndd.append(nm_cnd)
        cndd.append(nmr_cnd)

        # Adiciona candidato na lista principal
        cnd.append(tuple(cndd))

    print('\n\n')

elif opcao == 2:
    voto = -1
    
    while voto != encerra_vtc:
        for cndd in cnd:
            print(f'Candidato {cndd[0]} | Numero {cndd[1]}')

        voto = int(input('Vote no numero de um candidato -> '))
        
        cont = 0
        for cndd in cnd:
            cont += 1
            if voto == cndd[1]:
                if cndd[0] not in cnt_voto:
                    cnt_voto.update ({ cndd[0]: 1})
                    break
                else:
                    cnt_voto[cndd[0]]+=1
                    break
            else:
                if cont == len(cndd):
                    cnt_voto['Nulo'] +=1
        
elif opcao == 3:
    cnt_voto['Nulo'] -=1
    
    maior = 0
    vcd = ''
    for key, value in cnt_voto.items():
        if value > maior:
            maior = value
            vencedor = key
        print(f'{key} | Voto {maior}')
    
    print(f'O
          ')



        

 


