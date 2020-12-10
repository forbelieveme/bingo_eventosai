lista = []
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



            
v_repetidos(1, "hola")
v_repetidos(0, "hol")
v_repetidos(0, "ho")
v_repetidos(0, "h")
v_repetidos(0, "h")