print("UNIVERSIDAD ESTATAL AMAZÓNICA")
print("Fundamentos de la programación")
print("Estudiante: Fernando Corrales Tarira")

file_name = "my_notes.txt"

# Contenido de las notas personales
notes_content = ("\"\"\"\"\"Resolver los ejerciciosde matemática para el CPE.\n"
                 "Llevar el carro al mecánico para que chequee el sistema de frenos.\n"
                 "Imprimir los informes de tutoría para el trabajo. \n"
                 "6:30 retirar a mi esposa del trabajo para salir a Quevedo. \n"
                 "Ir los por los niños al curso de Karate para salir de vieje.\n"
                 "")

with open(file_name, "w") as file:
    file.write(notes_content)

print(f"Se han creado y guardado las notas en el archivo {file_name}.")


with open(file_name, "r") as file:
    input("Presiona Enter para ver la siguiente actividad:")
    first_line = file.readline()
    print("Primera línea del archivo:", first_line)

    input("Presiona Enter para ver la siguiente actividad:")
    second_line = file.readline()
    print("Segunda línea del archivo:", second_line)

    input("Presiona Enter para ver la siguiente actividad:")
    third_line = file.readline()
    print("Tercera línea del archivo:", third_line)

    input("Presiona Enter para ver la siguiente actividad:")
    fourth_line = file.readline()
    print("6:30 retirar a mi esposa del trabajo para salir a Quevedo:", fourth_line)

    input("Presiona Enter para ver la siguiente actividad:")
    fifth_line = file.readline()
    print("Ir por los niños al curso de Karate para salir de vieje:", fifth_line)

print("Tareas finalizadas, un buen feriado")