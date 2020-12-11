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
    

                





def max() :
    i = 2
    j = 2
    print (j != i )


deal_array()
#max()