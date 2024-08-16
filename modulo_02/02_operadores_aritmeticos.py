### OPERADORES ARITMETICOS
# Los operadores aritméticos se utilizan para realizar operaciones matemáticas entre valores. 


a = 5
b = 3

# Suma (+): Suma dos operandos.
resultado = a + b  # resultado es 8
print(str(a) + " + " + str(b) + " = " + str(resultado))

#Resta (-): Resta el segundo operando del primero.
resultado = a - b  # resultado es 2
print(str(a) + " - " + str(b) + " = " + str(resultado))

#Multiplicación (*): Multiplica dos operandos.
resultado = a * b  # resultado es 15
print(str(a) + " * " + str(b) + " = " + str(resultado))

#División (/): Divide el primer operando por el segundo. El resultado es un número de punto flotante.
resultado = a / b  # resultado es 1.6666666666666667
print(str(a) + " / " + str(b) + " = " + str(resultado))

#División entera (//): Divide el primer operando por el segundo y devuelve la parte entera de la división.
resultado = a // b  # resultado es 1
print(str(a) + " // " + str(b) + " = " + str(resultado))

#Módulo (%): Devuelve el resto de la división entre los dos operandos.
resultado = a % b  # resultado es 2
print(str(a) + " % " + str(b) + " = " + str(resultado))

#Exponenciación (**): Eleva el primer operando a la potencia del segundo.
resultado = a ** b  # resultado es 125
print(str(a) + " ** " + str(b) + " = " + str(resultado))


# NOTAS
"""
    Es valido hacer operaciones entre valores de tipo entero y tipo flotante.
    Consideraciones:
        * Si uno de los dos valores es flotante el resultado sera flotante
        * Si la operación de división el resultado será flotante
"""