# Calculadora

n_1=float(input('Informe um numero! '))
n_2=float(input('Informe outro numero! '))
n_3=input('Qual variavel sera usada? ')

if n_3=='-':
    soma=n_1-n_2
    print('resultado é', soma)
elif n_3=='+':
    soma=n_1+n_2
    print('resultado é', soma)
elif n_3=='/': 
    soma=n_1/n_2
    print('resultado é', soma )
   
elif n_3=='*':
    soma=n_1*n_2
    print('resultado é', soma)
else:
    print('Conta nao existente')
