idade=int(input('Qual sua idade?'))

if idade>18:
    print('Você pode fazer a abilitação')
    CPF=input('Vou pricisar do seu CPF para o cadastro ->')
    nmc=input('Informe o seu nome completo')
elif idade<18:
    print('Você não tem idade necesaria para fazer a sua abilitação')
else:
    print('Você pode fazer a abilitação')
    CPF=input('Vou pricisar do seu CPF para o cadastro ->')
    nmc=input('Informe o seu nome completo')

print('CPF:',CPF,"\n",
     'Nome completo:',nmc,"\n",
     'Idade:', idade)
