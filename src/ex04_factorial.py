"""
Ejercicio 4 (un poco más complejo):
Factorial de un número.
"""

def factorial(n: int) -> int:
    """
    Devuelve n! (n factorial).

    Reglas:
    - 0! = 1
    - Si n < 0, lanza ValueError.
    - Debe resolverse usando un bucle (no recursión).
    """
    if n < 0:
        raise ValueError("no definido para numeros negativos")
    resultado = 1
    i = 1
    while i <= n:
        resultado *= i
        i += 1
    return resultado 

    raise NotImplementedError("Implementa factorial(n)")
