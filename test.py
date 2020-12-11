#lista = []
def v_repetidos (nuevo, valor):            
    if nuevo == 1 :
        lista = []
        print("nueva verificación")
    if nuevo == 0 :
        ver (valor)
        print("Lista existente")
            

def ver (valor) :
    print (lista)    
    if len(lista) == 0 :
        lista.append(valor)
    else :
        for value in lista :
            if value == valor :
                print ('hay valores repetidos con ', value)
            else :
                lista.append(value)        



#Compara dos arreglos, si son iguales retorna 1, si son distintos retorna 0.
def arr_compar (arr1, arr2):    
    
    if len(arr1) == len(arr2) :
        print("misma longitud")
        contador = 0
        for elementos in arr1 :      
            if arr1[contador] == arr2[contador] :                
                igual = 1

            else :
                igual = 0

            if igual == 0 :
                #tan pronto como encuentre que un elemento es desigual, retorna 0
                print ("arreglos distintos")
                return 0                

            contador = contador + 1
        print ("arreglos iguales")
        return igual
    else :
        print ("distinta longitud")
        return 0


#print (str(arr_compar([3,4,5,6], [3,4,5])))


def deal_array():
    arr_format = []
    #lee el archivo
    f = open('C:\\Users\\Jimenez Medina\\Desktop\\Archivos Backup\\bingo_eventosai\\300000.csv', 'r')
    data = f.read()
    
    #Convierte cada carton en una posición de un arreglo.
    arreglo = data.split("\n")        
    
    #bandera
    print (type(arreglo))    

    #bandera
    print (len(arreglo))

    #metodo para formatear un
    for elemento in arreglo :
                
        test = elemento.split(";")        

        #Eliminación de campos innecesarios para comparar
        test.pop(0)
        test.pop(0)
        test.pop(0)
        test.pop(0)
        test.pop(0)
        test.pop(0)
        test.pop(12)
                
        arr_format.append(test)


    ##Número de filas y columnas del arreglo formateado para comparación
    filas = len(arr_format)
    columnas = len(arr_format[0])
    
    print ("numero de filas: "+str(filas)+ " y número de columnas: "+str(columnas))

    # for el in arr_format:
    #     print (el)

    repeat(arr_format)

        
    
#Método óptimo para hallar cartones repetidos en un arreglo
def repeat (arr):
    n = len(arr)
    repetidos = []
    it = 0
    j = 0
    while (j < n):
        print ("checking bingo card number: "+str(j))
        i = j
        while (i < n) :
            it += 1
            if arr [j] == arr[i] and j != i:                
                repetidos.append("Cartón repetido en :"+str(j)+", y :"+str(i)+".")
            i = i + 1        
        j = j + 1
        

    print ("Hay "+str(len(repetidos))+" cartones repetidos.")

    for elementos in repetidos :
        print (elementos)
    print ("Total de iteraciones: "+str(it))
    

                
#Método para chechar que un cartón no se repita con los demás



#Da formato al archivo de cartones tomando la ruta de ubicación.

def getFormat(ruta):
    arr_format = []
    #lee el archivo
    f = open(ruta, 'r')
    data = f.read()
    
    #Convierte cada carton en una posición de un arreglo.
    arreglo = data.split("\n")        
    
    #bandera
    print (type(arreglo))    

    #bandera
    print (len(arreglo))

    #metodo para formatear un
    for elemento in arreglo :
                
        test = elemento.split(";")        

        #Eliminación de campos innecesarios para comparar
        if (len(test) > 1) : 
            test.pop(0)
            test.pop(0)
            test.pop(0)
            test.pop(0)
            test.pop(0)
            test.pop(0)
            test.pop(12)
            arr_format.append(test)


    ##Número de filas y columnas del arreglo formateado para comparación    
    
    #pos = ""   
    # print ("[B][B][B][B][B][I][I][I][I][I][NN][NN][NN][NN][GG][GG][GG][GG][GG][OO][OO][OO][OO][OO]")
    # for el in arr_format :
    #     pos = ""
    #     for al in el :
    #         pos = pos+"["+str(el.index(al))+"]"
    #     print (pos+"\n")
    #     break        
    return arr_format


#Metodo que toma un arreglo y clasifica los valores en un arreglo inteligente
def getSublists(arr) :
    #tamaño 24
    B = []
    I = []
    N = []
    G = []
    O = []
    #Contador para 
    j = 0
    for letra in arr:
        #Valores de la b
        if j > -1 and j < 5:
            B.append(letra)
        #Valores de la i
        if j > 4 and j < 10:
            I.append(letra)

        #Valores de la n
        if j > 9 and j < 14:
            N.append(letra)
        
        #Valores de la g
        if j > 13 and j < 19:
            G.append(letra)
        #Valores de la o
        if j > 18 and j < 24:
            O.append(letra)
        j = j + 1
        
    carton = [B,I,N,G,O]

    for letra in carton :
        if carton.index(letra) == 0 :
            print("Valores de la letra B:")
            print(letra)
        if carton.index(letra) == 1 :
            print("Valores de la letra I:")
            print(letra)
        if carton.index(letra) == 2 :
            print("Valores de la letra N:")
            print(letra)
        if carton.index(letra) == 3 :
            print("Valores de la letra G:")
            print(letra)
        if carton.index(letra) == 4 :
            print("Valores de la letra O")            
            print(letra)                                    
    return carton
            
        
    # #definición de rangos
    # rangoB = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    # rangoI = [16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    # rangoN = [31,32,33,34,35,36,37,38,39,40,41,42,43,44,45]
    # rangoG = [46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]
    # rangoO = [61,62,63,64,65,66,67,68,69,70,71,72,73,74,75]
    
    #def corregir_valores()

ruta = 'C:\\Users\\Jimenez Medina\\Desktop\\Archivos Backup\\bingo_eventosai\\cartonescomas.csv'
test = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

getSublists(test)
#getFormat(ruta)
#test()
#max()

