# Las tuplas no se pueden nodificar
numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

punto = tuple([1, 2])
print(punto)

menosNumeros = numeros[:2]
print(menosNumeros)

# Realiza todas las operaciones que una lista pero no se puede modificar las tuplas
primero, segundo, *otros = numeros
print(primero, segundo, otros)
for n in numeros:
    print(n)

# Se crea una lista para modificarla
listaNumeros = list(numeros)
listaNumeros[0] = "Chanchito feliz"
print(listaNumeros)
