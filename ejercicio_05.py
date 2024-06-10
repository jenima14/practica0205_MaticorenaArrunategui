def Número_al_Cuadrado(lista):
    '''Escribir una función que reciba una muestra de números en una
    lista y devuelva otra lista con sus valores al cuadrado.
    Parámetro:  
            Una lista con números
    Salida:
            Otra lista pero con los números al cuadrado'''
   
    cuadrado = []
    for i in lista:
        x = i**2
        cuadrado.append(x)
    return cuadrado

print(Número_al_Cuadrado([2,4,6]))