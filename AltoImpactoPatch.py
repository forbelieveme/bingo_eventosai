file = open("C:\\Users\\Jimenez Medina\\Desktop\\Archivos Backup\\bingo_eventosai\\cartonescomas.csv")
numline = len(file.readlines())
print (numline)
arreglo = []
with open('C:\\Users\\Jimenez Medina\\Desktop\\Archivos Backup\\bingo_eventosai\\cartonescomas.csv', 'r') as f:
    data = f.read()
    #print (str(data))    
    print (str(type(data)))
    #for line in data:
    arreglo = data.split("\n")
    #
    rows = len(arreglo)
    #
    cols = len(arreglo[0].split(";"))    

    print ("Número de files: ",rows, " Número de columnas: ", cols)


for i, carton in arreglo :
    values = carton.split(";")
    for j, col in values :
        #Columna B
        if j > 5 and j < 11 :
            if col > 0 and col < 16 :
            else :
                print ("Valor incorrecto en ",i, ",",j".")

        #Columna I
        if j > 10 and j < 16 :
            if col > 15 and col < 31 :

        #Columna N1, N2
        if j > 15 and j < 18 :
            if col > 30 and col < 46 :
        
        #Columna número del cartón
        if j == 18 :
            print ("i: "i, "j:",j)

        #Columna N1, N2
        if j > 18 and j < 21 :
            if col > 30 and col < 46 :
        
        #Columna G        
        if j > 20 and j < 26 :
            if col > 45 and col < 61 :

        #Columna O
        if j > 25 and j < 31 :
            if col > 60 and col < 75 :





        