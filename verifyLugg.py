
from operator import truediv
from random import randint
from xml.etree.ElementTree import tostring

while True:
    sumaTot=0
    lista = []
    #Quiero obtener 6 números "random" entre 1 y 14
    while (sumaTot!=27):
        lista.clear()
        for i in range(6):  #i = 0; i < 6
            lista.append(randint(1,14))
        # print("Rand número " , i, " es ", lista[i])

        #Debo comprobar que su suma es 27
        suma=0
        for n in lista:
            suma += n
        #print("La suma es " , suma)
        if (suma==27):
            sumaTot=27

    #print("Hemos salido del bucle")

    #Tras generar dichos números, los paso a binario
    for i in range(6):
        print(lista[i])

    #Función para pasar un número de decimal a binario, teniendo cada número 6 dígitos
    def dec_bin(n):
        bin = 0
        mult = 1

        while n != 0:
            bin = bin + n%2*mult
            n //= 2
            mult *= 10
        
        toStr = str(bin)
        while (len(toStr) < 6):
        #  print(toStr , " tiene longitud ", len(toStr))
            toStr = '0' + toStr

        return toStr

    #
    #listaBin = []
    #for i in range(6):
    #    listaBin.append(dec_bin(lista[i]))
    #    print(lista[i], " en binario es ", listaBin[i])
    #

    #Hago una lista con los números del 1 al 64 en binario

    listaBin = []
    for i in range(64):
        listaBin.append(dec_bin(i))
        print(i, " en binario es ", listaBin[i])

    #Con el algoritmo de las sumas compruebo que sea adecuado

    sumaVerify = []
    for i in range(64):
        sumaVerify.append(0)
        caracteres = list(listaBin[i])
        pos = 0

        for c in caracteres:
        #    print("el número ", i, "tiene ", c )
            if (c == '1'):
                sumaVerify[i] += lista[pos]
        #        print("por eso entra y suma " , lista[pos])
            pos = pos + 1
                
        if (sumaVerify[i] > 25):
            sumaVerify[i] -= 26
        print(i ,": ", sumaVerify[i])

    todos=0;
    for i in range(25):
        if i in sumaVerify:
            print("El número " , i, "Sí está")
            todos = todos+1
        else:
            print(i, "no está")
    
    if todos == 25:
        break

