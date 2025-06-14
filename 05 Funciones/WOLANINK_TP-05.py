# Ejercicios con Listas en Python
# 1) 
multiplos_de_4 = list(range(4, 101, 4))
print("Ejercicio 1:", multiplos_de_4)

# 2) 
mis_favoritos = ["pizza", "música", "libros", "cine", "viajar"]
print("Ejercicio 2:", mis_favoritos[-2]) 

# 3)
lista_vacia = []
lista_vacia.append("sol")
lista_vacia.append("luna")
lista_vacia.append("estrella")
print("Ejercicio 3:", lista_vacia)

# 4) 
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"      
animales[-1] = "oso"      
print("Ejercicio 4:", animales)

# 5) 
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print("Ejercicio 5:", numeros)


# 6)
lista_numeros = list(range(10, 31, 5))
print("Ejercicio 6:", lista_numeros[:2])

# 7)
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["camioneta", "jeep"]
print("Ejercicio 7:", autos)

# 8) 
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("Ejercicio 8:", dobles)

# 9) 
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
# a)
compras[2].append("jugo")

# b)
indice_fideos = compras[1].index("fideos")
compras[1][indice_fideos] = "tallarines"

# c) 
compras[0].remove("pan")

print("Ejercicio 9:", compras)

# 10) 
lista_anidada = [
    15,                            # lista_anidada[0]
    True,                          # lista_anidada[1]
    [25.5, 57.9, 30.6],            # lista_anidada[2][0], [2][1], [2][2]
    False                          # lista_anidada[3]
]
print("Ejercicio 10:", lista_anidada)

