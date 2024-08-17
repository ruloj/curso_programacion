### OPERADORES DE COMPARACIÓN
# Los operadores de comparación se utilizan para comparar dos valores y devuelven un valor booleano (True o False).

a = 5
b = 3

# Igual (==): Verifica si dos operandos son iguales.
resultado = (a == b)  # resultado es False
print(str(a) + " == " + str(b) + " es " + str(resultado))

# Distinto (!=): Verifica si dos operandos son diferentes.
resultado = (a != b)  # resultado es True
print(str(a) + " != " + str(b) + " es " + str(resultado))

# Mayor que (>): Verifica si el primer operando es mayor que el segundo.
resultado = (a > b)  # resultado es True
print(str(a) + " > " + str(b) + " es " + str(resultado))

# Menor que (<): Verifica si el primer operando es menor que el segundo.
resultado = (a < b)  # resultado es False
print(str(a) + " < " + str(b) + " es " + str(resultado))

# Mayor o igual que (>=): Verifica si el primer operando es mayor o igual que el segundo.
resultado = (a >= b)  # resultado es True
print(str(a) + " >= " + str(b) + " es " + str(resultado))

# Menor o igual que (<=): Verifica si el primer operando es menor o igual que el segundo.
resultado = (a <= b)  # resultado es False
print(str(a) + " <= " + str(b) + " es " + str(resultado))



### OPERACIONES Y MÉTODOS DE CADENAS QUE DEVUELVEN VALORES BOOLEANOS

cadena1 = "Hola Mundo"
cadena2 = "hola mundo"
cadena3 = "Mundo"
cadena4 = "Hola"

# Igualdad (==): Verifica si dos cadenas son iguales.
resultado = (cadena1 == cadena2)  # resultado es False
print('"' + cadena1 + '" == "' + cadena2 + '" es ' + str(resultado))

# Desigualdad (!=): Verifica si dos cadenas son diferentes.
resultado = (cadena1 != cadena2)  # resultado es True
print('"' + cadena1 + '" != "' + cadena2 + '" es ' + str(resultado))

# Método .isdigit(): Verifica si todos los caracteres de la cadena son dígitos.
resultado = "12345".isdigit()  # resultado es True
print('"12345" ¿es digito? ' + str(resultado))

# Método .isalpha(): Verifica si todos los caracteres de la cadena son alfabéticos.
resultado = "Hola".isalpha()  # resultado es True
print('"Hola" ¿es alfabetico? ' + str(resultado))

# Método .isspace(): Verifica si todos los caracteres de la cadena son espacios en blanco.
resultado = "   ".isspace()  # resultado es True
print('"   " son puros espacios es ' + str(resultado))


# NOTAS
"""
    Los operadores de comparación son útiles en las estructuras de control de flujo como las 
    instrucciones if, bucles while, etc., para tomar decisiones basadas en condiciones.
"""
