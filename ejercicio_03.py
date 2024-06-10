import math
def Area_Circulo(radio):
    '''Escribir una función que calcule el área de un círculo
    Fórmula:  Area = pi*r**2
     Parámetro:
            número entero o con decimal
     Salida:
            El resultado del área de un círculo'''
    
    Area = math.pi * radio**2
    return Area

def Volumen_Cilindro(altura):
    '''Escribir una función que calcule el volumen de un cilindro 
    usando la primera función
    Fórmula:  Volumen = Area * altura
    Parametro:
            número entero o con decimal
    Salida:
            El resultado del área de un círculo'''
    
    Volumen = area* altura
    return Volumen

area = Area_Circulo(5)
print(Volumen_Cilindro(2))