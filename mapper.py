#!/usr/bin/python3

import sys
index = 0

p1=0
p2=0

# Leemos la entrada estandar linea a linea 
for linea in sys.stdin:
    linea = linea.replace('"', "")
    temp = linea.split(",")
    # Obtenemos la cabecera del archivo y determínanos los índices de la combinación de campos que se usaran como clave 
    if index == 0:
        p1 = temp.index("servicio")
        p2 = temp.index("sexo")
    else:
        # Imprimimos el resultado de la reducción 
        print("%s-%s\t%s" % (temp[p1], temp[p2], 1))
    index+=1
