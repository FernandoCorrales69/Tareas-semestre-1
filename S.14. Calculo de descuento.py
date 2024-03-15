#
print("UNIVERSIDAD ESTATAL AMAZÓNICA")
print("Fundamentos de la programación")
print("Ejercicio de calculo de descuento y porcentaje")
print("Estudiante:Fernando Corrales")
def calcular_descuento(compra, porcentaje_descuento=10):
    descuento = compra * (porcentaje_descuento / 100)
    return descuento

def calcular_valor_final(compra, descuento):
    valor_final = compra - descuento
    return valor_final

# Ingreso del valor de la compra
valor_compra = float(input("Ingrese el valor de la compra: "))

# Calcular descuento
descuento = calcular_descuento(valor_compra)

# Calcular valor final
valor_final = calcular_valor_final(valor_compra, descuento)

print(f"Su descuento aplicado es: ${descuento}")
print(f"Valor final de la compra: ${valor_final}")


