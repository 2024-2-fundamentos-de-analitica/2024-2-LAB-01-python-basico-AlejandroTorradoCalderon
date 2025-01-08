def pregunta_02():
    
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]
    """
   
    contador = {}

 
    with open('files/input/data.csv', 'r') as file:
        for line in file:
          
            columnas = line.strip().split('\t')
            
            
            if columnas[0] in contador:
                contador[columnas[0]] += 1
            else:
                contador[columnas[0]] = 1

    
    resultado = sorted(contador.items())

    return resultado
