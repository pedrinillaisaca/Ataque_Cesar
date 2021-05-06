from collections import Counter
#condiciones de ejecucion 
#funciona solamenete para oraciones en idioma ingles

archivo=open("pedro.txt")
linea=archivo.readline()
abecedario=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# dictProb={}
# lisTaPro=[]
# while linea !='':
#     tem=linea.split(" ")
#     dictProb.setdefault(float(tem[1].replace("\n","")),tem[0])
#     lisTaPro.append(float(tem[1].replace("\n","")))
#     linea=archivo.readline()

# lisTaPro.sort(reverse=True)
# print("===================")


def contar_letras_repetidas(texto):    
    contador = Counter(texto)
    contador=str(contador)
    contador=contador[9:-2]
    print(contador)
    listTemp=contador.split(",") 
    cont=0   
    aux=0
    for i in listTemp:
        itemTemp=i.split(":")
        itemTemp[0]=itemTemp[0].replace("'","")
        itemTemp[0]=itemTemp[0].replace(" ","")        
        texto=texto.replace(itemTemp[0],dictProb.get(lisTaPro[cont]))#ESTE PUEDE NO SER EXACTO
        if aux != int(itemTemp[1]):
            cont+=1
        aux=int(itemTemp[1])
        

    return texto

def getLetrasUnicas(texto):
    contador = Counter(texto)
    contador=str(contador)
    contador=contador[9:-2]
    listTemp=contador.split(",")
    salida=[]
    for i in listTemp:
        itemTemp=i.split(":")
        itemTemp[0]=itemTemp[0].replace("'","")
        itemTemp[0]=itemTemp[0].replace(" ","")        
        salida.append(itemTemp[0])       
    return salida


def letraConcurrent(texto):    
    contador = Counter(texto)
    contador=str(contador)
    contador=contador[9:-2]    
    listTemp=contador.split(",")          
    return listTemp[0].split(":")[0].replace("'","")

def getK(texto):
    NumletraConcurrente=abecedario.index(letraConcurrent(texto))
    NumletraMasUsada=abecedario.index("e")
    return NumletraConcurrente-NumletraMasUsada #pilas aqui de pronto sale negativo

def decode(texto):
    salida=""   
    k=getK(texto)
    letrasUnicas=getLetrasUnicas(texto)    
    for i in letrasUnicas:
        y=abecedario.index(i)
        posicion=y-k  
        if posicion<0:
            posicion+=26          
        print("letra= ",i,"==>",y," - ",k," = ",posicion, " salida= ",abecedario[posicion])        
    
    for i in texto:
        y=abecedario.index(i)
        posicion=y-k
        salida+=abecedario[posicion]

    return salida





texto = 'xultpaajcxitltlxaarpjhtiwtgxktghidhipxciwtvgtpilpitghlxiwiwtxgqadds'
print(decode(texto))


