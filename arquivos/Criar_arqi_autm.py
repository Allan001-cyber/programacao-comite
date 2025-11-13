arq = 0
n = 0
while arq <= 4:
    try:
        with open(f"arquivos/arquivo_teste/arquivo_{n+1}.txt", "w") as f:
            f.write("Primeira linha do arquivo.\n")
            n += 1
            arq += 1
            print("arquivos/Primeira_linha.txt criado com sucesso!")
    
    except:
        print('Arquivo ja foi criado')