# Teste 1

t=2 
em='email'
sn = 'senha'
e = input('informe o e-mail! ')
s = input('informe a senha! ')
while  t >=0: 
    if e == em :
        if s == sn:
            print('Bem vindo!')
            break
        else:
             print('senha ou email errada!')
        e = input('informe o e-mail! ')
        s= input( 'Informe a senha! ')
        t -=1 
    else:
        print('senha ou email errada!')
        e = input('informe o e-mail! ')
        s= input( 'Informe a senha! ')
        t -=1
else:
    print('Acesso bloqueado!')

# Teste 2 ( Não deu 100% certo! )

# t= 3
# em='e'
# sn='s'

# while t>0:
#     e=input('Informe o Email! ')
#     s=input('Infome a Senha! ')

#     if e==em and s==sn :
#         print('Bem Vindo!')
#         break
#     else:
#          print('Senha ou Email errado!\nTente nova mente!')
#          t -=1
# else:
#     print('Acesso Bloqueado! ')
