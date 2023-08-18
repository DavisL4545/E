
#Ingrese una cantidad en metros y convertir a kilómetros, sabiendo que 
#1km=1000m
def tabla_de_multiplicar(numero):
    print("Tabla de multiplicar del", numero)
    print("Factor  Producto")
    for i in range(1, 11):
        producto = numero * i
        print(f"{numero:5.2f}  x {i:2d} = {producto:7.2f}")

def convertir_metros_a_kilometros(metros):
    kilometros = metros / 1000
    return kilometros

# Pregunta 1
metros = float(input("Ingrese una cantidad en metros: "))
kilometros = convertir_metros_a_kilometros(metros)
print(f"{metros:.2f} metros equivalen a {kilometros:.2f} kilómetros.\n")

numero_tabla = float(input("Ingrese un número para la tabla de multiplicar: "))
tabla_de_multiplicar(numero_tabla)




#Ingrese dos números y visualizar el número mayor y número menor.
def tabla_de_multiplicar(numero):
    print("Tabla de multiplicar del", numero)
    print("Factor  Producto")
    for i in range(1, 11):
        producto = numero * i
        print(f"{numero:5.2f}  x {i:2d} = {producto:7.2f}")

def encontrar_mayor_menor(num1, num2):
    mayor = max(num1, num2)
    menor = min(num1, num2)
    return mayor, menor

numero_tabla = float(input("Ingrese un número para la tabla de multiplicar: "))
tabla_de_multiplicar(numero_tabla)

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
mayor, menor = encontrar_mayor_menor(num1, num2)
print(f"El número mayor es {mayor} y el número menor es {menor}.")




#Ingresar 5 números y visualizarlos ordenados de forma ascendente (Abstenerse 
#del uso de la librería sort())

def tabla_de_multiplicar(numero):
    print("Tabla de multiplicar del", numero)
    print("Factor  Producto")
    for i in range(1, 11):
        producto = numero * i
        print(f"{numero:5.2f}  x {i:2d} = {producto:7.2f}")

def ordenar_numeros_ascendente(numeros):
    for i in range(len(numeros)):
        for j in range(i + 1, len(numeros)):
            if numeros[i] > numeros[j]:
                numeros[i], numeros[j] = numeros[j], numeros[i]
    return numeros

numero_tabla = float(input("Ingrese un número para la tabla de multiplicar: "))
tabla_de_multiplicar(numero_tabla)

numeros = []
for i in range(5):
    num = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

numeros_ordenados = ordenar_numeros_ascendente(numeros)
print("Números ordenados de forma ascendente:", numeros_ordenados)




#Visualizar los n primeros números en forma descendente. (Puede utilizar While o 
#for)
def tabla_de_multiplicar(numero):
    print("Tabla de multiplicar del", numero)
    print("Factor  Producto")
    for i in range(1, 11):
        producto = numero * i
        print(f"{numero:5.2f}  x {i:2d} = {producto:7.2f}")

def mostrar_numeros_descendente(n):
    print(f"Los primeros {n} números descendentes son:")
    for i in range(n, 0, -1):
        print(i, end=" ")

numero_tabla = float(input("Ingrese un número para la tabla de multiplicar: "))
tabla_de_multiplicar(numero_tabla)

n_descendente = int(input("Ingrese el valor de n para los primeros n números descendentes: "))
mostrar_numeros_descendente(n_descendente)



