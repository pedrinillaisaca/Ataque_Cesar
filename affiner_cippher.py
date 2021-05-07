
def getModInver(a,abecedario):
    for i in range(0,len(abecedario)):
        if (a*i)%len(abecedario) == 1:
            return i
            break
    return 0

def decode(a,b,texto):
    texto=texto.replace(" ","")
    salida=""
    mI=getModInver(a,abecedario)  
    for y in texto:
        # print((y))
        x=mI*(abecedario.index(y)-b) % len(abecedario)
        print("Letra: ",y,"  y-b= ",abecedario.index(y)-b," a^-1 (y-b)", mI*(abecedario.index(y)-b),"  a^-1 (y-b) mod 30= ",x," salida=",abecedario[x])
        salida+=abecedario[x]
    return salida


abecedario=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","ä","ö","ü","ß"]

print(decode(17,1,"ä u ß w ß"))