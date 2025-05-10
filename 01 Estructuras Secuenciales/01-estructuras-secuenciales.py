
import math

# 1) Hola Mundo
print("Hola Mundo!")

# 2)
name = input("Ingrese su nombre: ")
print(f"Hola {name}!")

# 3)
name = input("Ingrese su nombre: ")
surname = input("Ingrese su apellido: ")
age = input("Ingrese su edad: ")
residence = input("Ingrese su lugar de residencia: ")
print(f"Soy {name} {surname}, tengo {age} años y vivo en {residence}.")

# 4)

radius = float(input("Ingrese el radio del círculo: "))
area = math.pi * radius ** 2
perimeter = 2 * math.pi * radius
print(f"Área: {area:.2f}, Perímetro: {perimeter:.2f}")

# 5)
seconds = int(input("Ingrese cantidad de segundos: "))
hours = seconds / 3600
print(f"{seconds} segundos equivalen a {hours:.2f} horas.")

# 6)
number = int(input("Ingrese un número: "))
print(f"Tabla del {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# 7)
number1 = int(input("Ingrese el primer número (≠ 0): "))
number2 = int(input("Ingrese el segundo número (≠ 0): "))
sum_result = number1 + number2
difference = number1 - number2
product = number1 * number2
division = number1 / number2
print(f"Suma: {sum_result}")
print(f"Resta: {difference}")
print(f"Multiplicación: {product}")
print(f"División: {division:.2f}")

# 8)
weight = float(input("Ingrese su peso en kg: "))
height = float(input("Ingrese su altura en metros: "))
bmi = weight / (height ** 2)
print(f"Su índice de masa corporal es: {bmi:.2f}")

# 9)
celsius = float(input("Ingrese la temperatura en °C: "))
fahrenheit = (9 / 5) * celsius + 32
print(f"{celsius}°C equivale a {fahrenheit:.2f}°F")

# 10)
number1 = float(input("Ingrese el primer número: "))
number2 = float(input("Ingrese el segundo número: "))
number3 = float(input("Ingrese el tercer número: "))
average = (number1 + number2 + number3) / 3
print(f"El promedio es: {average:.2f}")
