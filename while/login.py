t=2 
em='email'
sn = 'as'
e = input('informe o e-mail! ')
s = input('informe a senha! ')
while  t >=0: 
    if e == em :
        if s == sn:
            print('Acesso permitido!')
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