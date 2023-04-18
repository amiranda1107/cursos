usuarios = [["Chanchito", 4],
            ["Felipe", 1],
            ["Pulga", 5]
            ]

# Obtener el nombre en unalista, transformando la lista para que devuelva un listado de nombres.
# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)


# Otra version al ejercicio anterior transformar lista (map) - Comprension de listas
# nombres = [usuario[0] for usuario in usuarios]

# Filtrar listas (filter) - Comprension de listas
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]
# nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]

# Map
nombres = list(map(lambda usuario: usuario[0], usuarios))
print(nombres)
# Filter
menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)
