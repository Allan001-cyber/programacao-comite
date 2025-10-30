def maior(nm):
    lst = []
    for numero in nm:
        if numero == max(nm):
          lst.append(numero)  
    return lst

def main():
    nm = (132,212,5,5,1,4,864,8,4,5,22,8,12,558548,5,555)
    n = maior(nm)
    print(n)
main()






