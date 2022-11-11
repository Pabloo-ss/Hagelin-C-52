from random import randint

#Partimos de la definición de las ruedas
ruedas = {
    25 : [],
    26 : [],
    29 : [],
    31 : [],
    34 : [],
    37 : [],
    38 : [],
    41 : [],
    42 : [],
    43 : [],
    46 : [],
    47 : []
}

#Rellenamos con el número de pines adecuado
for x,y in ruedas.items():
    for i in range(x):
        y.append(0)

#Se eligen 6 de las 12 ruedas al azar, con un orden también elegido al azar

ruedasSelected = []
for i in range(6):  #i = 0; i < 6
    esta = 1
    while (esta == 1):
        newWheel = randint(0,11)
        if  not (newWheel in ruedasSelected):
            esta = 0
    ruedasSelected.append(newWheel)
print(ruedasSelected)

#Wheels almacena las ruedas seleccionadas junto con sus pines
counter = 0
wheels = {}
for x,y in ruedas.items():
    if counter in ruedasSelected:
        wheels[x] = y
    counter += 1


#Para elegir qué pines se dejan activos y cuales no, se hace lanzando una moneda

""" pinesAct = []
pinesAct.append(randint(0,1))
pinesAct.append(randint(0,1))
pinesAct.append(randint(0,1))
#Suponiendo la CX-52 en la que todas las ruedas tienen 47 pines
for i in range(3,47):       
    pin = randint(0,1)      #Como si se lanzase la moneda
    if (pinesAct[i-1] != pin or pinesAct[i-2]!= pin or pinesAct[i-3] != pin):
        pinesAct.append(pin)
    else:
       # print("En el pin número ", i, " ha habido que cambiarlo porque  ", pinesAct[i-1] , " , ", pinesAct[i-2], " y ", pinesAct[i-3])
        if (pin == 0):
            pinesAct.append(1)
        else:
            pinesAct.append(0)    
print(pinesAct) """

#Hay que intentar tener aproximadamente el 50% de los pines activos
#pero para eso podemos suponer que al elegir cada uno como si se lanzase
#una moneda, se hará 50/50 aproximadamente

########## creo que la máquina q tenemos q hacer es la C-52 sin la 'X' entonces hay q tener en cuenta que no todas las ruedas tiene los mismos pines

for x,y in wheels.items():
    y[0] = randint(0,1)
    y[1] = randint(0,1)
    y[2] = randint(0,1)
    for i in range(3,x): 
        pin = randint(0,1)      #Como si se lanzase la moneda
        if (y[i-1] != pin or y[i-2]!= pin or y[i-3] != pin):
            y[i] = pin
        else:
        # print("En el pin número ", i, " ha habido que cambiarlo porque  ", pinesAct[i-1] , " , ", pinesAct[i-2], " y ", pinesAct[i-3])
            if (pin == 0):
                y[i] = 1
            else:
                y[i] = 0
print(wheels)

posWheels = [0,0,0,0,0,0]

message = ''
for i in range(6):
    message = "\nRango de 0 a " + str(list(wheels.keys())[i] - 1) + ' ---> Posicion inicial rueda ' + str(i + 1) + ': '
    posWheels[i] = int(input(message))

print(posWheels)