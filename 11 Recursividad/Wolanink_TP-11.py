#1) Factorial recursivo
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def factorial_usuario():
    num = int(input("Ingrese un número entero positivo para calcular factoriales hasta ese número: "))
    for i in range(1, num + 1):
        print(f"Factorial de {i}: {factorial(i)}")

#2) Fibonacci recursivo (posición)
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_usuario():
    num = int(input("Ingrese la posición para mostrar la serie Fibonacci hasta esa posición: "))
    print("Serie Fibonacci:")
    for i in range(num):
        print(fibonacci(i), end=" ")
    print()

#3) Potencia recursiva (base^exponente)
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

def potencia_usuario():
    base = int(input("Ingrese la base: "))
    exponente = int(input("Ingrese el exponente: "))
    print(f"{base} elevado a {exponente} es {potencia(base, exponente)}")

#4) Decimal a binario recursivo
def decimal_a_binario(num):
    if num == 0:
        return ""
    else:
        return decimal_a_binario(num // 2) + str(num % 2)

def decimal_a_binario_usuario():
    num = int(input("Ingrese un número decimal positivo para convertir a binario: "))
    if num == 0:
        print("0")
    else:
        print(decimal_a_binario(num))

#5) Palíndromo recursivo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

def palindromo_usuario():
    palabra = input("Ingrese una palabra sin espacios ni tildes para verificar si es palíndromo: ").lower()
    if es_palindromo(palabra):
        print("Es palíndromo")
    else:
        print("No es palíndromo")

#6) Suma de dígitos recursiva
def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)

def suma_digitos_usuario():
    num = int(input("Ingrese un número entero positivo para sumar sus dígitos: "))
    print(f"Suma de dígitos: {suma_digitos(num)}")

#7) Contar bloques pirámide recursivo
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

def contar_bloques_usuario():
    n = int(input("Ingrese el número de bloques en el nivel más bajo de la pirámide: "))
    print(f"Total de bloques necesarios: {contar_bloques(n)}")

#8) Contar ocurrencias de un dígito recursivo
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

def contar_digito_usuario():
    numero = int(input("Ingrese un número entero positivo: "))
    digito = int(input("Ingrese un dígito para contar sus apariciones: "))
    print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces en el número {numero}")

#Ejemplo de ejecución de todos (descomentar para probar)

# factorial_usuario()
# fibonacci_usuario()
# potencia_usuario()
# decimal_a_binario_usuario()
# palindromo_usuario()
# suma_digitos_usuario()
# contar_bloques_usuario()
# contar_digito_usuario()
