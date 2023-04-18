# Sets significa grupos o conjuntos
primer = {1, 1, 2, 2, 3, 4}
# primer.add(5)
# primer.remove(1)
# print(primer)
segundo = [3, 4, 5]
segundo = set(segundo)
# Union
# print(primer | segundo)
# Interseccion
# print(primer & segundo)
# Diferencia
# print(primer - segundo)
# Diferencia simetrica
print(primer ^ segundo)

if 5 in segundo:
    print("Hola Mundo")
