print("UNIVERSIDAD ESTATAL AMAZÓNICA")
print("Tecnologías de la información")
print("Estudiante: Fernando Corrales Tarira")
def buscar_numero(matriz, numero):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                return True, i, j
    return False, -1, -1

# Crear una matriz 3x3 de ejemplo
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Solicitar al usuario el número a buscar
numero_buscado = int(input("Ingrese el número que desea buscar en la matriz: "))

# Llamar a la función buscar_numero y mostrar el resultado
encontrado, fila, columna = buscar_numero(matriz, numero_buscado)

if encontrado:
    print(f"El número {numero_buscado} se encontró en la posición ({fila}, {columna}) de la matriz.")
else:
    print(f"El número {numero_buscado} no se encontró en la matriz.")

