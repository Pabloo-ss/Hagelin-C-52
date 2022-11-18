from drum import *
from impressionWheel import *
from wheels import *

#La rueda normal imprime y luego imprime la de cifrado con un desplazamiento que viene dado por el numero de dientes en el engranaje,
# el numero de dientes se corresponde con el numero de barras del tambor que han sido desplazadas (las barras de desplazamineto no cuentan).
# Una barra es desplazada cuando, durante la revolución del tambor, una de sus orejetas hace contacto con un brazo guía activo.
# Un brazo guía está activo cuando la rueda que le corresponde (del 1 al 6 de izquierda a derecha) tiene un pin activo en esa posición de la rueda.
# Las barras de desplazamiento se encargan del avance de las ruedas (no añaden desplazamineto a la impresión). La 1ª rueda siempre avanza y 
# las demás dependerán de si hay un brazo guía activo en esa posición. Si está activo el de la posición 1 se moverán las 
# ruedas 2,3,4,5 y 6; si está activo el de la posición 2 se moverán la 3,4,5 y 6; etc. La barra 1 avanza la rueda 2, la barra 2 avanza la rueda 3...
#   Luego está el desplazamineto de las ruedas de impresión entre sí usando el modo variable y eso pero por ahora lo dejamos de lado mejor (diría yo)
# Pero creo q es que primero imprime la normal y a la segunda se le aplica el desplazamiento: en el modo variable este desplazamiento se aplica
# solo a segundo rueda de impresión, mientras que em el constante se aplica a las dos.

#Creamos las ruedas con sus pines y el tambor con sus orejetas. Tambien las ruedas de impresión con su desplazamiento inicial
ruedas, posRuedas = wheels()
tambor = drum()
n = int(input("\nDesplazamiento inicial de la rueda de impresión: "))
ruedaImp1, ruedaImp2 = impressionWheels(n)
variable = bool(input("\¿Quiere que sea variable? 1/0: "))

configInicial = {
    "ruedasI": ruedas,
    "posRuedasI": posRuedas.copy(), #Solamente es necesrio el .copy() en esta porque es la única que se modifica
    "tamborI": tambor,
    "ruedaImp": n
}

#Se pide al usuario el texto a cifrar y se codifica pasándolo a mayúsculas y sustituyendo los espacios por 'X'
print("\n-------> Proceso de cifrado")
texto = input("Texto a cifrar: ").upper()
texto = texto.replace(" ", "X")
textoPlano = ""
textoCifrado = ""
for letra in texto:
    textoPlano += imprimeTextoR1(letra, ruedaImp1, ruedaImp2)

    # Comprobar el desplazamiento a aplicar empezando por la columna de la izquierda. También comprobamos las barras de desplazamiento
    barrasDesp = [1, 0, 0, 0, 0, 0]
    col = -1
    colDesp = 0
    barras = 0
    # ***Columnas 1-5***
    for i in range(5):
        col += 1    
        colDesp += 1
        # 1º miramos si el brazo guía está activo comprobando el pin de la posición de la rueda de esa columna
        if (isBrazoActivo(list(ruedas.values())[col], posRuedas[col])):
            # 2º si está activo comprobamos cuantas barras se verían desplazadas para añadir un paso a la rueda de impresión de cifrado
            barras += orejetasInCol(list(tambor.values())[col])
            # 3º comprobamos las barras de desplazaminto desplazadas a la izuqierda
            desplazamientos  = orejetasInColDespl(list(tambor.values())[col])
            for i in range(colDesp, len(barrasDesp)):
                barrasDesp[i] += desplazamientos / (len(barrasDesp) - colDesp)
        # si no está activo pasamos a la siguiente columna
    
    # ***Columna 6***
    col += 1
    # 1º miramos si el brazo guía está activo comprobando el pin de la posición de la rueda de esa columna
    if (isBrazoActivo(list(ruedas.values())[col], posRuedas[col])):
        # 2º si está activo comprobamos cuantas barras se verían desplazadas para añadir un paso a la rueda de impresión de cifrado
        barras += orejetasInCol(list(tambor.values())[col])
        # En la última columna no es necesario comprobar las barras de desplazamiento


    # Tenemos el numero de pasos extra que se aplicarán a la rueda de impresión para el cifrado
    textoCifrado += imprimeTextoR2(ruedaImp1, ruedaImp2, barras, variable)

    # Tenemos el desplazamiento de cada rueda
    advanceWheels(ruedas, posRuedas, barrasDesp)

print("Texto codificado: ", textoPlano)
print("Texto cifrado: ", textoCifrado)

##############################

#Iniciamos el proceso de descifrado
#Recuperamos la configuración inicial
ruedas = configInicial["ruedasI"] #no es realmente necesario porque no se modifica
posRuedas = configInicial["posRuedasI"]
tambor = configInicial["tamborI"] #no es realmente necesario porque no se modifica
ruedaImp1, ruedaImp2 = impressionWheels(configInicial["ruedaImp"])

print("\n-------> Proceso de descifrado")

textoDescifrado = ""
for letra in textoCifrado:
    textoPlano += imprimeTextoR1(letra, ruedaImp1, ruedaImp2)

    # Comprobar el desplazamiento a aplicar empezando por la columna de la izquierda. También comprobamos las barras de desplazamiento
    barrasDesp = [1, 0, 0, 0, 0, 0]
    col = -1
    colDesp = 0
    barras = 0
    # ***Columnas 1-5***
    for i in range(5):
        col += 1    
        colDesp += 1
        # 1º miramos si el brazo guía está activo comprobando el pin de la posición de la rueda de esa columna
        if (isBrazoActivo(list(ruedas.values())[col], posRuedas[col])):
            # 2º si está activo comprobamos cuantas barras se verían desplazadas para añadir un paso a la rueda de impresión de cifrado
            barras += orejetasInCol(list(tambor.values())[col])
            # 3º comprobamos las barras de desplazaminto desplazadas a la izuqierda
            desplazamientos  = orejetasInColDespl(list(tambor.values())[col])
            for i in range(colDesp, len(barrasDesp)):
                barrasDesp[i] += desplazamientos / (len(barrasDesp) - colDesp)
        # si no está activo pasamos a la siguiente columna

    # ***Columna 6***
    col += 1
    # 1º miramos si el brazo guía está activo comprobando el pin de la posición de la rueda de esa columna
    if (isBrazoActivo(list(ruedas.values())[col], posRuedas[col])):
        # 2º si está activo comprobamos cuantas barras se verían desplazadas para añadir un paso a la rueda de impresión de cifrado
        barras += orejetasInCol(list(tambor.values())[col])
        # En la última columna no es necesario comprobar las barras de desplazamiento


    # Tenemos el numero de pasos extra que se aplicarán a la rueda de impresión para el cifrado
    textoDescifrado += imprimeTextoR2(ruedaImp1, ruedaImp2, barras, variable)

    # Tenemos el desplazamiento de cada rueda
    advanceWheels(ruedas, posRuedas, barrasDesp)


print("Texto cifrado: ", textoCifrado)
print("Texto descifrado: ", textoDescifrado)
print("Texto original: ", textoDescifrado.replace("X", " "))

