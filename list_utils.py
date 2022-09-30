## comentarios con doble numeral: mi solucion
# comentarios de un solo numeral: relacionados al video


def find_one(l, needle):
    ## if needle in list:
    ##      return True
    ## else:
    ##      return False

    """
    Devuelve True si encuentra una o mas coincidencias de needle en list
    """

    #inicializamos el booleano que representa la condicion de haber encontrado o no y el indice
    # found = False
    # index = 0
    #miestras no encontramos o hayamos terminado con la lista
    #while not found and index < len(list):
        #miramos si esta en la posicion actual y actualizamos la condicion
        #if needle == list[index]:
            #found = True
        #avanzamos al siguiente elemento
        #index += 1
    #devolvemos si hemos encontrado o no
    #return found

    ### refactoriza find_one como un caso de find_n ###
    return find_n(l, needle, 1)
    
def find_n(l, needle, n):
    ## list_needle = list(filter(lambda p: p == needle, l))
    ## if n >= 0:
    ##    return len(list_needle) >= n
    ## else:
    ##    return False


    """
    Devuleve True si en l hay n o mas ocurrencias de needle
    False si hay menos o si n < 
    """

    #si n >= 0...
    if n >= 0:
        #inicializamos el indice y el contador
        index = 0
        count = 0
        #mientras no hayamos encontrado el elemento n veces o no hayamos terminado la lista
        while count < n and index < len(l):
            #si lo encontramos, actualizamos el contador
            if needle == l[index]:
                count += 1
            #avanzamos al siguiente elemento
            index += 1
        #devolvemos el resultado de comparar contador con n
        return count >= n
    #en caso de n < 0
    else:
        return False

def find_streak(l, needle, n):
    """
    Devuelve True si en list hay n o mas needles seguidos
    False, para todo lo demas
    """
    ## count = 0  
    ## if needle in l:
    ##     index = l.index(needle)
    ##     while index < len(l) and count != n:
    ##         if l[index] == needle:
    ##             count += 1
    ##         else:
    ##             count = 0
    ##         index += 1 
    ##     return count == n
    ## else:
    ##     return False

    #si n >= 0
    if n >= 0:
        #inicializo el indice, el contador y el indicador de racha
        index = 0
        count = 0
        streak = False
        #mientras no haya encontrado n seguidos o la lista no se haya acabado
        while count < n and index < len(l):
            #si lo encuentro activo el indicador de racha y actualizo el contador
            if needle == l[index]:
                streak = True
                count += 1
            #si no lo encuentro, desactivo el indicador de racha y pongo a cero el contador
            else:
                streak = False
                count = 0
            #avanzo al siguiente elemento
            index += 1
        #devolvemos el resultado de comparar el contador con n Siempre y Cuando estemos en racha
        return n <= count and streak
    else:
        return False

def first_elements(l_of_ls):
    ## list_first_element = []
    ## for l in l_of_ls:
    ##     list_first_element.append(l[0])
    ## return list_first_element

    """
    Recibe una lista de listas y devuelve una lista con los primeros elementos de la original
    """
    #la solucion dada fue igual a la mia
    
    ### refactor

    return nth_elements(l_of_ls, 0)

def nth_elements(l_of_ls, n):
    """
    Recibe una lista de listas + una posicion y devuelve una lista con los elementos de la original en el indice indicado
    """
    list_first_element = []
    for l in l_of_ls:
        list_first_element.append(l[n])
    return list_first_element

    #la solucion dada fue igual a la mia

def transpose(matrix):
    """
    Recibe una matriz y devuelve su transpuesta
    """
    length = len(matrix[0])
    transposed = []
    for i in range(length):
        transposed.append(nth_elements(matrix, i))
    return transposed

    #la solucion dada fue igual a la mia

def displace(l, distance, filler = None):
    if distance == 0 or len(l) == 0:
        return l
    elif distance > 0:
        ## i = 0
        ## while i in range(distance) and i < len(l):
        ##     l.insert(i, filler)
        ##     l.pop()
        ##     i +=1
        ## return l
        filling = [filler] * distance
        res = filling + l
        res = res[:-distance]
        return res
    else:
        ## i = distance
        ## while i in range(distance, 0) and i < len(l):
        ##     l.insert(len(l), filler)
        ##     l.pop(0)
        ##     i += 1 
        ## return l
        filling = [filler] * abs(distance)
        res = l + filling
        res = res[abs(distance):]
        return res

def displace_matrix(matrix, filler = None):
    #creamos una matriz vacia
    m = []
    #por cada columna de la matriz original la desplazamos su indice -1
    for i in range(len(matrix)):
        #añadimos la columna desplazada a m
        m.append(displace(matrix[i], i - 1, filler))
    #devolvemos m
    return m

    # return recorrer_matrix(matrix, displace())

def reverse_list(l):
    return list(reversed(l))

def reverse_matrix(m):
    rm = []
    for l in m:
        rm.append(reverse_list(l))
    return rm

    # return recorrer_matrix(m, reverse_list())

# def recorrer_matrix(matrix, function):
#     m = []
#     for i in range(len(matrix)):
#         m.append(function(m[i]))
#     return m