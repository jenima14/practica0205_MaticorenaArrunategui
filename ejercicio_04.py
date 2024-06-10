def Calculo_Media(lista):
    '''Escribir una función que reciba una muestra de números en una
    lista y devuelva su media.
    Parámetro:
            Una lista con números enteros o con decimales
    Salida:
            La 'media' de la suma de la lista dividido por su longitud '''
   
    if len(lista) == 0:
        return "Lista vacía"
    else:
        return sum(lista) / len(lista)
   
print(Calculo_Media([1,2.5,3,4,5]))