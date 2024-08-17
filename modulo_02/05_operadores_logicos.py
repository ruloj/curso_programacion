### OPERADORES LÓGICOS
# Los operadores lógicos se utilizan para combinar múltiples condiciones booleanas.

# Definimos algunas variables booleanas para las demostraciones.
a = True
b = False

print("Operadores lógicos:")

# Operador AND (and): Devuelve True si ambas condiciones son verdaderas.
resultado = (a and b)  # resultado es False (porque b es False)
print(str(a) + " and " + str(b) + " es " + str(resultado))

# Operador OR (or): Devuelve True si al menos una de las condiciones es verdadera.
resultado = (a or b)  # resultado es True (porque a es True)
print(str(a) + " or " + str(b) + " es " + str(resultado))

# Operador NOT (not): Devuelve True si la condición es falsa, y False si la condición es verdadera.
resultado = not a  # resultado es False (porque a es True)
print("not " + str(a) + " es " + str(resultado))



### NOTAS

## TABLAS DE VERDAD

# AND (y)
"""
    +-------+-------+---------+
    |   A   |   B   | A AND B |
    +-------+-------+---------+
    | True  | True  | True    |
    | True  | False | False   |
    | False | True  | False   |
    | False | False | False   |
    +-------+-------+---------+
    * requiere que todas las condiciones sean verdaderas para devolver True.
    Ejemplo:
        Quiero enviar un correo los dias que sean viernes y la fecha sea 15.
"""


# OR (o)
"""
    +-------+-------+---------+
    |   A   |   B   |  A OR B |
    +-------+-------+---------+
    | True  | True  | True    |
    | True  | False | True    |
    | False | True  | True    |
    | False | False | False   |
    +-------+-------+---------+
    * requiere que al menos una condición sea verdadera para devolver True.
    Ejemplo:
        Quiero enviar un correo los dias que sean viernes y la fecha sea 15.
"""

# NOT (no)
"""
    +-------+--------+
    |   A   | NOT A  |
    +-------+--------+
    | True  | False  |
    | False | True   |
    +-------+--------+
    * invierte el valor booleano de una condición.
    Ejemplo:
        Quiero enviar un correo los dias que no sean viernes.
"""