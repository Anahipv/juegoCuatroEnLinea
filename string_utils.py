def explode_string(s):
    """
    Transforma un string en una lista de caracteres
    """
    return list(s)

def explode_list_of_strings(l_of_s):
    return list(map(explode_string, l_of_s))