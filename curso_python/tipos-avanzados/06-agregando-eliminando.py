mascotas = ["Pelusa",
            "Wolfgang",
            "Pulga",
            "Felipe",
            "Pulga",
            "Chanchito feliz"
            ]

mascotas.insert(1, "Melvis")  # Insertas un elemento en una posicion dada
mascotas.append("Chanchito triste")  # Agregas un elemento al final de la lista


mascotas.remove("Pulga")  # Elimina un elemento de una lista
mascotas.pop()  # Elimina el ultimo elemento de la lista
mascotas.pop(1)  # Elimina un elemento especifico, por el indice
del mascotas[0]  # Elimina un elemento especifico, por el indice
mascotas.clear()  # Limpia la lista completa 
print(mascotas)
