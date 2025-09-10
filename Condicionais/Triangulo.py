# Dias da semana em português e em ingles!

#n_1=float(input('Informe quanto vale um lado do Triangulo! '))
#n_2=float(input('Informe quanto vale o outro lado do Triangulo!'))
#n_3=float(input('Informe quanto vale a base do Triangulo!'))
#if n_1+n_2>n_3:
#    print('Triangulo Isosceles ') 
#elif n_1==n_2==n_3:
#    print('Triangulo Equilatero ')
#else:
#    print('Triangulo Escaleno ')

n_1=float(input('Informe quanto vale um lado do Triangulo! '))
n_2=float(input('Informe quanto vale o outro lado do Triangulo!'))
n_3=float(input('Informe quanto vale a base do Triangulo!'))
if n_1+n_2>n_3 or\
     n_1+n_3>n_2 or\
     n_3+n_2>n_1:
   
    if n_1==n_2==n_3:
        print('Triangulo Equilatero ')
    elif n_1==n_2 or\
       n_1==n_3 or\
       n_3==n_2 :
        print('Triangulo Isosceles ')
    else:
        print('Triangulo Escaleno ')
else:
       