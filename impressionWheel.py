from collections import deque 

#Se puede desplazar la rueda de impresión

#inicialmente la rueda sería dos arrays
def impressionWheels(n):
    rueda1 = deque(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    rueda2 = deque(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    rueda2.rotate(n)

    return (rueda1, rueda2)

def imprime(rueda):
    #print(rueda[0], end=" ")
    return rueda[0]

def imprimeTextoR1(letra, rueda1, rueda2):
    while letra != rueda1[0]:
        rueda1.rotate(-1)
        rueda2.rotate(1)
    return imprime(rueda1)

def imprimeTextoR2(rueda1, rueda2, n):
    rueda1.rotate(-n)
    rueda2.rotate(n)
    return imprime(rueda2)