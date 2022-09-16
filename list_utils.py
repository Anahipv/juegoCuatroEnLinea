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