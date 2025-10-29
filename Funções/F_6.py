a= int(input('Qual o numero valor? '))

def impar(a):
 if a % 2 ==0:
  return 'par'
 else:
  return 'impar'
 
resultado = impar(a)
print(resultado)