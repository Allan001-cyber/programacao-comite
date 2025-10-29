# Calcula a media dos numeros a baicho
a= int(input('Qual o primriro valor? '))
b= int(input('Qual o segundo valor? '))
c= int(input('Qual o treseiro valor? '))

def media(a,b,c):
 return a+b+c

resultado = media(a,b,c)
print(f'Resultado = {resultado/3}')