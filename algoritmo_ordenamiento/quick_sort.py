# ALGORITMO DE ORDENAMIENTO QUICKSORT

def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[-1] #Ultimo valor
    mayores = []
    menores = []
    iguales = [pivote]

    for elemento in lista[:-1]:
        if elemento > pivote:
            mayores.append(elemento)
        elif elemento < pivote:
            menores.append(elemento)
        else:
            iguales.append(elemento)

    return quick_sort(menores) + iguales + quick_sort(mayores)


lista_desordenada = [-2, 1, 3, -5, 1]
# print(lista_desordenada)
# lista_ordenada = quick_sort(lista_desordenada)
# print(lista_ordenada)



def quick_sort_print(lista, nivel=0):
    print(f'{"  " * nivel}Nivel {nivel}')
    print(f'{"  " * nivel}Lista actual: {lista}')

    if len(lista) <= 1:
        print(f'{"  " * nivel}Longitud <= 1\n')
        return lista

    pivote = lista[-1]  # Último valor
    mayores = []
    menores = []
    iguales = [pivote]

    for elemento in lista[:-1]:
        if elemento > pivote:
            mayores.append(elemento)
        elif elemento < pivote:
            menores.append(elemento)
        else:
            iguales.append(elemento)

    print(f'{"  " * nivel}Pivote = {pivote}')
    print(f'{"  " * nivel}Menores: {menores}')
    print(f'{"  " * nivel}Iguales: {iguales}')
    print(f'{"  " * nivel}Mayores: {mayores}\n')

    return quick_sort_print(menores, nivel + 1) + iguales + quick_sort_print(mayores, nivel + 1)

print(lista_desordenada)
lista_ordenada = quick_sort_print(lista_desordenada)
print(lista_ordenada)