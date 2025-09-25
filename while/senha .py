# s=''

# while s !='ola':
#     s= input('Informe sua senha: ')

# print('Acesso liberado!')

# T 2

t=2 
# True
sn = 'as'
s = input('informe a senha! ')
while  t >=0: 
    if s == sn :
        print('Acesso permitido!')
        break 
    else:
        s= input( 'Informe a senha! ')
        t -=1
else:
    print('Acesso negado!')