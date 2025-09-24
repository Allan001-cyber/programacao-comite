# Senhas :)

sn='aham123' or 'uma'

if sn==input('Informe sua senha! '):
    print('Seu acesso foi permitido! ')
else:
    print('Seu acesso não foi permitido!',"\n",
         'Tente novamente! ')
    if  sn==input('Informe sua senha! '):
        print('Seu acesso foi permitido! ')
    else:
        print('Seu acesso não foi permitido!',"\n",
         'Tente novamente! ')
        
        if sn==input('Informe sua senha! '):
            print('Seu acesso foi permitido! ')
        else:
            print('Seu acesso não foi permitido!',"\n",
         'Bloqueio foi ativado! ')