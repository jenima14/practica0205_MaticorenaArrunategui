def Binario(n):
    '''Escribir una función que convierta un número binario en decimal
    y otra que convierta un número decimal en binario.
    Parámetro:
            Número decimal
    Salida:
            El Número decimal pero en Binario'''

    binario = bin(n)
    return binario[2:]

print(Binario(128))


def Decimal(n):
    '''Escribir una función que convierta un número decimal en binario
    y otra que convierta un número binario en decimal.
    Parámetro:
            Número Binario
    Salida:
            El Número Binario pero en Decimal'''
   
    decimal = int(n,2)
    return decimal

print(Decimal("10000000"))