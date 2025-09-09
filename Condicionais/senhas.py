# Senhas :)

sn=input('Informe sua senha! ')
if sn=="aham123" or 'uma':
    print('Seu acesso foi permitido! ')
else:
    print('Seu acesso não foi permitido!',"\n",
         'Tente novamente! ')
    sn=input('Informe sua senha! ')
    if sn=="aham123":
        print('Seu acesso foi permitido! ')
    else:
        print('Seu acesso não foi permitido!',"\n",
         'Tente novamente! ')
        sn=input('Informe sua senha! ')
        if sn=="aham123":
            print('Seu acesso foi permitido! ')
        else:
            print('Seu acesso não foi permitido!',"\n",
         'Bloqueio foi ativado! ')