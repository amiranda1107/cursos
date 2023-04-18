# numero = 1

# while numero < 100:
#     print(numero)
#     numero *= 2

# Ejemplo de una terminar virtual con el control de flujo (while)

# comando = ""
# while comando.lower() != "salir":
#     comando = input("$ ")
#     print(comando)

# Loops Infinitos
while True: 
    comando = input("$ ")
    print(comando)
    if comando.lower() != "salir":
        break