def Factorial_Interactivo(n):
    '''Escribir una función que reciba un número entero positivo y
    devuelva su factorial. Realiza el ejercicio mediante bucles
    interactivos.
    Parámetro:
            Un número entero
    Salida:
            Número factorial de n'''
    
    if n > 0:
        resultado = 1
        for i in range(1,n+1):
            resultado = resultado * i
        return f"Factorial de {n} es resultado {resultado}"
    else:
        return "Escriba números enteros mayores a 0"
    
print(Factorial_Interactivo(7))


def Factorial_Recursiva(n):
   '''Escribir una función que reciba un número entero positivo y
    devuelva su factorial. Realiza el ejercicio mediante una 
    función recursiva.
    Parámetro:
            Un número entero
    Salida:
            Número factorial de n'''
   
   if n >0 and n <= 1:
       return 1
   else:
       return n * Factorial_Recursiva(n - 1)
   
print(Factorial_Recursiva(7))