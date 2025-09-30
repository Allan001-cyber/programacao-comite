
s= input('informe a infomer o texto! ')
ctd=0
vgs=0
while ctd <len(s):
        
    if s[ctd] == 'a':
        vgs+=1
    elif s[ctd] =='e':
        vgs+=1
    elif s[ctd] =='i':
        vgs+=1       
    elif s[ctd] =='o':
        vgs+=1
    elif s[ctd] =='u':
        vgs+=1

    ctd+=1

print(f'A palavra {s} tem {vgs} vogais')
