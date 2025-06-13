# Trabajo Práctico 1 - Condicionales

Materia: **Programación I**  
Carrera: **Tecnicatura Universitaria en Programación**  
Universidad: **UTN**  
Comisión: **23**

## Alumna

- **Nombre:** Melany Luz Valeria Wolanink  
- **Correo:** wolaninkmelany@gmail.com  

---

## Ejercicio 1: Categorías por edad

python
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif 12 <= edad < 18:
    print("Adolescente")
elif 18 <= edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")
numero = int(input("Ingrese un número: "))
#Ejercicio 2
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")
numero = int(input("Ingrese un número: "))
#Ejercicio 3
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

if a > b:
    print("El primer número es mayor.")
elif a < b:
    print("El segundo número es mayor.")
else:
    print("Ambos números son iguales.")
# Ejercicio 4: Año bisiesto
anio = int(input("Ingrese un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print("El año es bisiesto.")
else:
    print("El año no es bisiesto.")

# Ejercicio 5: Nota final
nota = float(input("Ingrese la nota (0 a 10): "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# Ejercicio 6: Mayor de tres números
x = int(input("Ingrese el primer número: "))
y = int(input("Ingrese el segundo número: "))
z = int(input("Ingrese el tercer número: "))

if x >= y and x >= z:
    print("El mayor es:", x)
elif y >= x and y >= z:
    print("El mayor es:", y)
else:
    print("El mayor es:", z)

# Ejercicio 7: Calculadora básica
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación (+, -, *, /): ")

if operacion == "+":
    print("Resultado:", num1 + num2)
elif operacion == "-":
    print("Resultado:", num1 - num2)
elif operacion == "*":
    print("Resultado:", num1 * num2)
elif operacion == "/":
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("Error: división por cero")
else:
    print("Operación no válida")

# Ejercicio 8: Edad válida
edad = int(input("Ingrese su edad: "))

if edad < 0 or edad > 120:
    print("Edad no válida.")
else:
    print("Edad válida.")

# Ejercicio 9: Signo del zodiaco (simplificado)
dia = int(input("Ingrese el día de nacimiento: "))
mes = int(input("Ingrese el mes de nacimiento (1-12): "))

if (mes == 3 and dia >= 21) o


