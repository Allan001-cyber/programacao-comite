try:
    with open("arquivos/arquivo_teste/Log_Registra_a_Data_e_a_Hora.txt","w") as f:
        f.write("Registro de data e hora do sistema:\n")
        from datetime import datetime
        agora = datetime.now()
        print("Data e hora atual:", agora)
        f.write(str(agora))
        

        
except FileNotFoundError:
    print("Arquivo não encontrado!")