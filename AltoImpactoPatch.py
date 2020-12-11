import time
start_time = time.time()
repetidos = []

def main (ruta):
    # file = open("C:\\Users\\Jimenez Medina\\Desktop\\Archivos Backup\\bingo_eventosai\\cartonescomas.csv")
    # numline = len(file.readlines())
    # print (numline)
    # arreglo = []
    with open(ruta, 'r') as f:
        data = f.read()
        #print (str(data))    
        #print (str(type(data)))    
        arreglo = data.split("\n")
        #
        rows = len(arreglo)
        #
        cols = len(arreglo[0].split(";"))    

        print ("Número de files: ",rows, " Número de columnas: ", cols)
        
        #j recorre las columnas
        j = 0
        #i recorre las filas
        i = 0
        
        elementos = []
        for carton in arreglo :
            values = carton.split(";")
            if i > 0 :
                for col in values :
                    #Columna B
                    if j > 5 and j < 11 :
                        if int(col) > 0 and int(col) < 16 :            
                            a = 1 + 2  
                        else :
                            mensaje = "Valor incorrecto en "+str(i)+ ","+str(j)+",out of range b."+ "valor: "+col
                            elementos.append(mensaje)

                                                
                    #Columna I
                    elif j > 10 and j < 16 :
                        if int(col) > 15 and int(col) < 31 :
                            a = 1 + 2    
                        else :
                            mensaje = "Valor incorrecto en "+str(i)+ ","+str(j)+",out of range i."+ "valor: "+col
                            elementos.append(mensaje)
                        

                    #Columna N1, N2
                    elif j > 15 and j < 18 :
                        if int(col) > 30 and int(col) < 46 :
                            a = 1 + 2
                        else :
                            mensaje = "Valor incorrecto en "+str(i)+ ","+str(j)+",out of range n1."+ "valor: "+col
                            elementos.append(mensaje)

                    #Columna número del cartón
                    elif j == 18 :
                        a = 1 + 2
                        #print ("i: ",i, "j:",j)

                    #Columna N3, N4
                    elif j > 18 and j < 21 :
                        if int(col) > 30 and int(col) < 46 :
                            a = 1 + 2
                        else :
                            mensaje = "Valor incorrecto en "+str(i)+ ","+str(j)+",out of range n2."+ "valor: "+col
                            elementos.append(mensaje)
                            
                    
                    #Columna G        
                    elif j > 20 and j < 26 :
                        if int(col) > 45 and int(col) < 61 :
                            a = 1 + 2
                        else :
                            mensaje = "Valor incorrecto en "+str(i)+ ","+str(j)+",out of range g."+ "valor: "+col
                            elementos.append(mensaje)

                    #Columna O
                    elif j > 25 and j < 31 :
                        if int(col) > 60 and int(col) < 76 :
                            a = 1 + 2
                        else :
                            mensaje = "Valor incorrecto en "+str(i)+ ","+str(j)+",out of range o."+ "valor: "+col
                            elementos.append(mensaje)
                    

                    
                    #Incremento del contador de columnas
                    if (j == 30) :
                        j = 0
                    else :
                        j = j + 1
                    #print(j)
            #Incremento del contador de filas
            i = i + 1            
            #print(i)
        print ("Número de errores de rango: "+str(len(elementos)))
        for elemento in elementos :
            print (elemento)


#Aquí se formatea la información del archivo de cartones de bingo, y posteriormente se
#verifica se hay cartones repetidos, se utiliza el formatod de cartones y la ruta del archivo.
def repeated (ruta):
    deal_array(ruta)
      
#Se encarga de tomar el formato de cartones de bingo y formatearlo con
#el propósito de que queden unicamente los valores de las columnas.
#Este método es llamado en el método repeated
def deal_array(ruta):
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
    filas = len(arr_format)
    columnas = len(arr_format[0])
    
    print ("numero de filas: "+str(filas)+ " y número de columnas: "+str(columnas))

    # for el in arr_format:
    #     print (el)

    repeat(arr_format)
           
#Método óptimo para hallar cartones repetidos en un arreglo
#Este método es llamado en el método deal_array
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


#Metodo que formatea el archivo con el propósito de analizarlo.
def getFormat(ruta):
    arr_format = []
    #lee el archivo
    f = open(ruta, 'r')
    data = f.read()
    
    #Convierte cada carton en una posición de un arreglo.
    arreglo = data.split("\n")        
    
    #bandera
    #print (type(arreglo))    

    #bandera
    #print (len(arreglo))

    #metodo para formatear un
    for elemento in arreglo :                
        #Separación de valores por comas
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

    return arr_format

#Corrección de valores fuera de rango.
#entra un arreglo y el arreglo de archivos sale corregido.

def fix_out_range(numero_carton, ruta):
    #se obtiene el arreglo a través del formateo de la ruta
    arreglo = getFormat(ruta)
    









#Definición de la ruta
ruta = 'C:\\Users\\Jimenez Medina\\Desktop\\Archivos Backup\\bingo_eventosai\\cartonescomas.csv'
main(ruta)


print("--- %s seconds ---" % (time.time() - start_time))

        