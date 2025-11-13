
import json

dados = {
    "Nome": "Ana",
    "Idade": 30 }

with open(json):
    try:
        with open("dados.json","w") as f:
            json.dump( dados, f, indent = 4 )
            print('Json criado com sucesso!')
    
    except FileNotFoundError:
        print(f'Json já foi criado\n{f}')




