
a= int(input('Qual o numero valor? '))
b= int(input('Qual a porcentagem? ')) 

def impar(a,b):
  n = a + ( a * ( b / 100 ))

  return n
 
resultado = impar(a,b)
print(resultado)