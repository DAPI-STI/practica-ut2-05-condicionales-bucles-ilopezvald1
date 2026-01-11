"""
Ejercicio 5:
Tabla de multiplicar.
"""

def multiplication_table(n: int) -> list[int]:
    """
    Devuelve una lista con 10 elementos:
    [n*1, n*2, ..., n*10]
    """
    tabla = []
    i = 1
    while i <= 10:
        tabla.append(n * i)
        i += 1
    return tabla 
    raise NotImplementedError("Implementa multiplication_table(n)")
