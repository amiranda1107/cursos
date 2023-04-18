# Creacion de la Variable
animal = "   chanCHito feliz  "

# Metodos: Convierte todos los caracteres en letras MAYUSCULAS
print(animal.upper())
# Metodos: Convierte todos los caracteres en letras minusculas
print(animal.lower())
# Metodos: Elimina los espacion en blancos y convierte la 1ra letra en mayuscula
print(animal.strip().capitalize())
# Metodos: Convierte la 1ra letra en mayuscula
print(animal.title())
# Metodos: Elimina los espacios en blanco de la izquiera (lstrip)
print(animal.lstrip())
# Metodos: Elimina los espacios en blanco de la derecha (rstrip)
print(animal.rstrip())
# Metodos: Busca un caracter o cadena de caracteres y devuelve el indece
print(animal.find("cH"))
# Metodos: Reemplaza un caracter o cadena de caracteres por otro
print(animal.replace("nCH", "j"))
# Metodos: Pregunta si se encuentra esa cadeva en la variable y devuelva TRUE o FALSE
print("nCH" in animal)
# Metodos: Pregunta si no se encuentra esa cadeva en la variable y devuelva TRUE o FALSE
print("nCH" not in animal)
