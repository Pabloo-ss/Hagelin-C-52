from random import randint

#Se eligen 6 de las 12 ruedas al azar, con un orden también elegido al azar

ruedas = []
for i in range(6):  #i = 0; i < 6
    esta = 1
    while (esta == 1):
        newWheel = randint(1,12)
        if  not (newWheel in ruedas):
            esta = 0
    ruedas.append(newWheel)
print(ruedas)

#Para elegir qué pines se dejan activos y cuales no, se hace lanzando una moneda

pinesAct = []
pinesAct.append(randint(0,1))
pinesAct.append(randint(0,1))
#Suponiendo la CX-52 en la que todas las ruedas tienen 47 pines
for i in range(2,47):       
    pin = randint(0,1)      #Como si se lanzase la moneda
    if (pinesAct[i-1] != pin or pinesAct[i-2]!= pin):
        pinesAct.append(pin)
    else:
       # print("En el pin número ", i, " ha habido que cambiarlo porque  ", pinesAct[i-1] , " y ", pinesAct[i-2] )
        if (pin == 0):
            pinesAct.append(1)
        else:
            pinesAct.append(0)    
print(pinesAct)

#Hay que intentar tener aproximadamente el 50% de los pines activos
#pero para eso podemos suponer que al elegir cada uno como si se lanzase
#una moneda, se hará 50/50 aproximadamente
