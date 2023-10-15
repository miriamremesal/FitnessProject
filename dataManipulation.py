# Preguntar al usuario su nivel (beginner, intermediate, expert) (1, 2 o 3)
# A partir de ahi, filtrar por qué músculo quiere entrenar
# Falta ordenamiento (yo lo haría x level)
# name, force, level, mechanic, equipment, primaryMuscles, secondaryMuscles, instructions, category


# # Si JSON: 
# {
#     "ejercicio1": {
#         "nombre": "Ejercicio 1",
#         "duracion": 30,
#         "calorias": 100
#     },
#     "ejercicio2": {
#         "nombre": "Ejercicio 2",
#         "duracion": 45,
#         "calorias": 150
#     },
#     "ejercicio3": {
#         "nombre": "Ejercicio 3",
#         "duracion": 20,
#         "calorias": 75
#     }
# }

# exercise_data = {
#     "ejercicio1": {
#         "nombre": "Ejercicio 1",
#         "duracion": 30,
#         "calorias": 100
#     },
#     # Resto de los datos...
# }


# # Búsqueda x nombre de ejercicio:
# nombre_a_buscar = "Ejercicio 2"
# if nombre_a_buscar in exercise_data:
#     ejercicio_encontrado = exercise_data[nombre_a_buscar]
#     print("Ejercicio encontrado:")
#     print(ejercicio_encontrado)
# else:
#     print(f"Ejercicio '{nombre_a_buscar}' no encontrado.")


# # Filtrado x duracion minima:
# exercise_data = {
#     "ejercicio1": {
#         "nombre": "Ejercicio 1",
#         "duracion": 30,
#         "calorias": 100
#     },
#     # Resto de los datos...
# }

# nombre_a_buscar = "Ejercicio 2"
# if nombre_a_buscar in exercise_data:
#     ejercicio_encontrado = exercise_data[nombre_a_buscar]
#     print("Ejercicio encontrado:")
#     print(ejercicio_encontrado)
# else:
#     print(f"Ejercicio '{nombre_a_buscar}' no encontrado.")


# # Ordenamiento x calorias:
# ejercicios_ordenados = sorted(exercise_data.items(), key=lambda x: x[1]["calorias"])

# print("Ejercicios ordenados por calorias:")
# for nombre, ejercicio in ejercicios_ordenados:
#     print(nombre, ejercicio)


# # Calculo de calorias totales:
# calorias_totales = sum(ejercicio["calorias"] for ejercicio in exercise_data.values())
# print("Calorías totales:", calorias_totales)







import json

# Cargar datos desde el archivo JSON
with open("all_exercises.json", "r") as json_file:
    exercise_data = json.load(json_file)

# Función para buscar ejercicios por nivel de dificultad
def buscar_ejercicios_por_nivel(nivel):
    ejercicios_encontrados = []
    for name, ejercicio in exercise_data.items():
        if ejercicio["level"].lower() == nivel.lower():
            ejercicios_encontrados.append((name, ejercicio))
    return ejercicios_encontrados

# Interfaz de línea de comandos
print("¡Bienvenido a tu aplicación fitness!")

while True:
    nivel = input("¿Cuál es tu nivel? (1 para principiante, 2 para intermedio, 3 para experto): ")
    
    if nivel in ["1", "2", "3"]:
        nivel_texto = ["beginner", "intermediate", "expert"][int(nivel) - 1]
        ejercicios = buscar_ejercicios_por_nivel(nivel_texto)
        
        if ejercicios:
            print(f"Ejercicios para nivel {nivel_texto}:")
            for ejercicio in ejercicios:
                print("- " + ejercicio[0])
            
            musculo = input("¿Qué músculo te gustaría entrenar hoy? Ingrese el nombre del músculo: ")
            musculo = musculo.lower()
            
            ejercicios_musculo_nivel = {
                name: ejercicio
                for name, ejercicio in ejercicios
                if musculo in [m.lower() for m in ejercicio[1]["primaryMuscles"]]
            }
            
            if ejercicios_musculo_nivel:
                print(f"Ejercicios de {musculo} en nivel {nivel_texto}:")
                for nombre, ejercicio in ejercicios_musculo_nivel.items():
                    print("- " + nombre)
            else:
                print(f"No se encontraron ejercicios de {musculo} en nivel {nivel_texto}.")
        else:
            print(f"No se encontraron ejercicios para nivel {nivel_texto}.")
    else:
        print("Nivel no válido. Por favor, ingrese 1, 2 o 3.")

    continuar = input("¿Deseas realizar otra búsqueda? (s/n): ")
    if continuar.lower() != "s":
        break

print("Gracias por usar la aplicación de ejercicios. ¡Hasta pronto!")










# import json

# # Cargar datos desde el archivo JSON
# with open("all_exercises.json", "r") as json_file:
#     exercise_data = json.load(json_file)

# # Función para buscar ejercicios por nivel de dificultad
# def buscar_ejercicios_por_nivel(nivel):
#     ejercicios_encontrados = []
#     for name, ejercicio in exercise_data.items():
#         if ejercicio["level"].lower() == nivel.lower():
#             ejercicios_encontrados.append(name)
#     return ejercicios_encontrados

# # Interfaz de línea de comandos
# print("¡Bienvenido a tu aplicación fitness!")

# while True:
#     nivel = input("¿Cuál es tu nivel? (1 para principiante, 2 para intermedio, 3 para experto): ")
    
#     if nivel in ["1", "2", "3"]:
#         nivel_texto = ["beginner", "intermediate", "expert"][int(nivel) - 1]
#         ejercicios = buscar_ejercicios_por_nivel(nivel_texto)
        
#         if ejercicios:
#             print(f"Ejercicios para nivel {nivel_texto}:")
#             for ejercicio in ejercicios:
#                 print("- " + ejercicio)
#         else:
#             print(f"No se encontraron ejercicios para nivel {nivel_texto}.")
#     else:
#         print("Nivel no válido. Por favor, ingrese 1, 2 o 3.")

#     continuar = input("¿Deseas realizar otra búsqueda? (s/n): ")
#     if continuar.lower() != "s":
#         break

# print("Gracias por usar la aplicación de ejercicios. ¡Hasta pronto!")

# # Ahora me está diciendo que filtre x si tiene maquina o no (libre), y luego x musculo, que no ordene.
# # Y que cree otro diccionario con los ejercicios que han aparecido segun el nivel 
# #  Cuando elija un ejercicio, mostrarle los datos del json (con instrucciones incluidas o solo las inst)