from choosePins import  wheels
from verifyLugg import drum
from impressionWheel import *

#La rueda normal imprime y luego imprime la de cifrado con un desplazamiento que viene dado por el numero de dientes en el engranaje,
# el numero de dientes se corresponde con el numero de barras del tambor que han sido desplazadas (las barras de desplazamineto no cuentan).
# Una barra es desplazada cuando, durante la revolución del tambor, una de sus orejetas hace contacto con un brazo guía activo.
# Un brazo guía está activo cuando la rueda que le corresponde (del 1 al 6 de izquierda a derecha) tiene un pin activo en esa posición de la rueda.
# Las barras de desplazamiento se encargan del avance de las ruedas (no añaden desplazamineto a la impresión). La 1ª rueda siempre avanza y 
# las demás dependerán de si hay un brazo guía activo en esa posición. Si está activo el de la posición 1 se moverán las 
# ruedas 2,3,4,5 y 6; si está activo el de la posición 2 se moverán la 3,4,5 y 6; etc.
#   Luego está el desplazamineto de las ruedas de impresión entre sí usando el modo variable y eso pero por ahora lo dejamos de lado mejor (diría yo)

#Creamos las ruedas con sus pines y el tambor con sus orejetas. Tambien las ruedas de impresión con su desplazamiento inicial
ruedas, posRuedas = wheels()
tambor = drum()
ruedaImp1, ruedaImp2 = impressionWheels(1)


