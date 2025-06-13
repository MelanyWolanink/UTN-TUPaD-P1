import random

def ejercicio1():
    for i in range(101):
        print(i)

def ejercicio2():
    numero = int(input("Ingresa un número entero: "))
    contador = len(str(abs(numero)))
    print("Cantidad de dígitos:", contador)

def ejercicio3():
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    if a > b:
        a, b = b, a
    suma = sum(range(a + 1, b))
    print("Suma:", suma)

def ejercicio4():
    suma = 0
    while True:
        numero = int(input("Ingresa un número (0 para terminar): "))
        if numero == 0:
            break
        suma += numero
    print("Suma total:", suma)

def ejercicio5():
    numero_secreto = random.randint(0, 9)
    intentos = 0
    while True:
        intento = int(input("Adivina el número (entre 0 y 9): "))
        intentos += 1
        if intento == numero_secreto:
            print(f"¡Correcto! Lo adivinaste en {intentos} intentos.")
            break

def ejercicio6():
    for i in range(100, -1, -2):
        print(i)

def ejercicio7():
    n = int(input("Ingresa un número entero positivo: "))
    if n < 0:
        print("Debe ser un número positivo.")
    else:
        suma = sum(range(n + 1))
        print("Suma:", suma)

def ejercicio8():
    pares = impares = positivos = negativos = 0
    cantidad = 100  # Cambia este valor para pruebas
    for _ in range(cantidad):
        num = int(input("Ingresa un número: "))
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
        if num > 0:
            positivos += 1
        elif num < 0:
            negativos += 1
    print("Pares:", pares)
    print("Impares:", impares)
    print("Positivos:", positivos)
    print("Negativos:", negativos)

def ejercicio9():
    suma = 0
    cantidad = 100  # Cambia este valor para pruebas
    for _ in range(cantidad):
        num = int(input("Ingresa un número: "))
        suma += num
    media = suma / cantidad
    print("Media:", media)

def ejercicio10():
    numero = int(input("Ingresa un número: "))
    invertido = int(str(abs(numero))[::-1])
    print("Número invertido:", invertido)
