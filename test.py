# lista = []
# def v_repetidos (nuevo, valor):            
#     if nuevo == 1 :
#         lista = []
#         print("nueva verificación")
#     if nuevo == 0 :
#         ver (valor)
#         print("Lista existente")
            

# def ver (valor) :
#     print (lista)    
#     if len(lista) == 0 :
#         lista.append(valor)
#     else :
#         for value in lista :
#             if value == valor :
#                 print ('hay valores repetidos con ', value)
#             else :
#                 lista.append(value)        

#arr1, arr2, longitud


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


print (str(arr_compar([3,4,5,6], [3,4,5])))

            
# v_repetidos(1, "hola")
# v_repetidos(0, "hol")
# v_repetidos(0, "ho")
# v_repetidos(0, "h")
# v_repetidos(0, "h")


