from collections import deque 

#Se puede desplazar la rueda de impresión

#inicialmente la rueda sería dos arrays

rueda1 = deque(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
rueda2 = deque(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
rueda2.rotate(1)
n = 1

print("Antes de desplazar: ", rueda1)
rueda1.rotate(n)
print("Después: ", rueda1)

def imprime(rueda):
    print(rueda[0])

def variable(letra):
    i = 0
    while letra != rueda1[i]:
        rueda1.rotate(1)
        i += 1
    imprime(rueda1)
    imprime(rueda2)


def constante(letra):
    i = 0
    while letra != rueda1[i]:
        rueda1.rotate(1)
        rueda2.rotate(1)
        i += 1
    imprime(rueda1)
    imprime(rueda2)
    


#En el modo Variable la posición entre la de la izq 
#la de la der cambia constantemente
#??????????????????????????????????????????????????