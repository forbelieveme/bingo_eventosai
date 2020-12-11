import time
start_time = time.time()
repetidos = []
def main ():
    # file = open("C:\\Users\\Jimenez Medina\\Desktop\\Archivos Backup\\bingo_eventosai\\cartonescomas.csv")
    # numline = len(file.readlines())
    # print (numline)
    # arreglo = []
    with open('C:\\Users\\Jimenez Medina\\Desktop\\Archivos Backup\\bingo_eventosai\\300000.csv', 'r') as f:
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
        print ("Número de errores: "+str(len(elementos)))
        for elemento in elementos :
            print (elemento)

# def v_repetidos (nuevo, valor):    
#     if nuevo == 1 :
#         repetidos = []
#         repetidos.append(valor)
#     if nuevo == 0 :
#         repetidos.append(valor)
#         print ("Valores repetidos en la misma columna")

    
#     for valor in repetidos :
#         temp = repetidos.remove(valor)
#         for temps in temp :
#             if valor == temps :
#                 print ('hay valores repetidos')

def repeated ():
    with open('C:\\Users\\Jimenez Medina\\Desktop\\Archivos Backup\\bingo_eventosai\\cartonescomas.csv', 'r') as f:
        data = f.read()
        #print (str(data))    
        #print (str(type(data)))    
        arreglo = data.split("\n")
        #
        rows = len(arreglo)
        #
        cols = len(arreglo[0].split(";"))    

        print ("Número de files: ",rows, " Número de columnas: ", cols)



#main()
repeated()

print("--- %s seconds ---" % (time.time() - start_time))

        