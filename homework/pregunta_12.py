"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    datos = {}
    with open('files/input/data.csv', 'r') as file:
        for line in file:
            columnas = line.strip().split('\t')
            letra = columnas[0]
            separaciones = columnas[4].split(',')
            valores = [i.split(':')[1] for i in separaciones]
            numero = sum([int(i) for i in valores])
            if letra in datos:
                datos[letra] += numero
            else:
                datos[letra] = numero
    return datos