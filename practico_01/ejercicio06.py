"""Type, Comprensión de Listas, Sorted y Filter."""

from typing import List, Union


def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Toma una lista de enteros y strings y devuelve una lista con todos los
    elementos numéricos al final.
    """

    lista_numeros = []
    lista_strings = []

    for i in lista:
        if isinstance(i, float) or isinstance(i, int):
            lista_numeros.append(i)
        else:
            lista_strings.append(i)

    return lista_strings + lista_numeros

    pass  # Completar


# NO MODIFICAR - INICIO
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == [
    "a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Re-escribir utilizando comprensión de listas."""

    lista_numeros = [i for i in lista if isinstance(
        i, float) or isinstance(i, int)]
    lista_strings = [i for i in lista if not isinstance(
        i, float) and not isinstance(i, int)]

    return lista_strings + lista_numeros

    pass  # Completar


# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == [
    "a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_sorted(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Re-escribir utilizando la función sorted con una custom key.
    Referencia: https://docs.python.org/3/library/functions.html#sorted
    """

    lista_numeros = sorted((x for x in lista if isinstance(x, (int, float))), key=float) # key=float para que ordene los numeros y no los strings, el isInstance es para que ordene los numeros y no los strings
    lista_strings = sorted((x for x in lista if isinstance(x, str)))
    return lista_strings + lista_numeros 

    pass  # Completar


# NO MODIFICAR - INICIO
assert numeros_al_final_sorted([3, "a", 1, "b", 10, "j"]) == [
    "a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_filter(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """CHALLENGE OPCIONAL - Re-escribir utilizando la función filter.
    Referencia: https://docs.python.org/3/library/functions.html#filter
    """

    lista_numeros = list(filter(lambda x: isinstance(
        x, float) or isinstance(x, int), lista))
    lista_strings = list(filter(lambda x: not isinstance(
        x, float) and not isinstance(x, int), lista))

    return lista_strings + lista_numeros
    pass  # Completar


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_filter([3, "a", 1, "b", 10, "j"]) == [
        "a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_recursivo(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """CHALLENGE OPCIONAL - Re-escribir de forma recursiva."""

    if len(lista) == 0:
        return []

    if isinstance(lista[0], float) or isinstance(lista[0], int):
        return numeros_al_final_recursivo(lista[1:]) + [lista[0]]
    else:
        return [lista[0]] + numeros_al_final_recursivo(lista[1:])

    pass  # Completar


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_recursivo([3, "a", 1, "b", 10, "j"]) == [
        "a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN
