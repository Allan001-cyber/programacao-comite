candidatos={

}
Opção=-1

while (Opção != 0):
    Opção = int (input('O que deseja fazer ? \n' \
    'Opção 1: Cadrasta os Candidatos ? \n' \
    'Opção 2: Comesa a Votação ? \n' \
    'Opção 3: Mostra todos os votos ? \n' \
    'Opção 4: Mostra candidato mais votado ? \n' \
    'Opção 0: Sair \n\n' \
    'Opção ->  '))
     
     # Cadrasto dos Candidatos!

    if Opção == 1:
        O_candidato = len(candidatos) + 1
        Informações = {}
        
        candidato = input('Informe o nome do candidato -> ')
        numero_do_candidato = int(input('Informe o numero do candidato -> '))

        candidatos.update({'Candidato' : candidato,
                           'Voto' : numero_do_candidato})
        
        candidatos.update({O_candidato: Informações})
        print()

    # elif Opção == 2: