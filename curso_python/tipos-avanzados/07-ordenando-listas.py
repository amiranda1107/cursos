numeros = [2, 4, 1, 45, 75, 22]

# numeros.sort()  # Ordenando una lista ascendentemente
# numeros.sort(reverse=True)  # Ordenando una lista descendentemente.

numeros2 = sorted(numeros)  # Devuelve una nueva lista ordenada ascendentemente
# Devuelve una nueva lista ordenada descendentemente
numeros2 = sorted(numeros, reverse=True)

print(numeros)
print(numeros2)

# usuarios = [[4, "Chanchito"],
#             [1, "Felipe"],
#             [5, "Pulga"]
#             ]

usuarios1 = [["Chanchito", 4],
             ["Felipe", 1],
             ["Pulga", 5]
             ]


# def ordena(elemento):
#     return elemento[1]


# usuarios1.sort(key=ordena, reverse=True)
# Con lambda accede al 2do elemento de un listado
usuarios1.sort(key=lambda el: el[1])
print(usuarios1)
