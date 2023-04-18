# # print(1, 2, 3, 4)
# # print(*lista)

# Uso de tuplas
# lista1 = [1, 2, 3, 4]
# lista2 = [5, 6]

# combinada = ["Hola", *lista1, "mundo", *lista2, "chanchito"]
# print(combinada)

# Uso de diccionario
punto1 = {"x": 19, "y": "Hola"}
punto2 = {"y": 15}

# operador de desempaquetamiento (**)
nuevoPunto = {**punto1, **punto2, "z": "Mundo"}
print(nuevoPunto)
