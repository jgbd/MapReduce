#!/usr/bin/python3

from collections import defaultdict
import sys

# Realizar la reducción
grupos = defaultdict(list)
for claveValor in sys.stdin:
    key, value = claveValor.split("\t", 1)
    grupos[key].append(int(value))

# Imprimir los resultados finales
for key, values in grupos.items():
    # Sumar los valores correspondientes a la clave
    total = sum(values)
    
    # Imprimir el resultado
    print(f"Clave: {key}, Total: {total}")
