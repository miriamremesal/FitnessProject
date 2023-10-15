import requests
import json

# URL base del repositorio en GitHub
base_url = "https://raw.githubusercontent.com/wrkout/exercises.json/master/exercises/"

# Lista de nombres de ejercicios
exercise_names = ["Ab_Crunch_Machine", "Ab_Roller", "Adductor", "Adductor_Groin", "Advanced_Kettlebell_Windmill", "Air_Bike", "All_Fours_Quad_Stretch", "Alternate_Hammer_Curl", "Alternate_Heel_Touchers", "Alternate_Incline_Dumbbell_Curl", "Alternate_Leg_Diagonal_Bound", "Alternating_Cable_Shoulder_Press", "Alternating_Deltoid_Raise", "Alternating_Floor_Press", "Alternating_Hang_Clean", "Alternating_Kettlebell_Press", "Alternating_Kettlebell_Row", "Alternating_Renegade_Row", "Ankle_Circles", "Ankle_On_The_Knee", "Anterior_Tibialis-SMR", "Anti-Gravity_Press", "Arm_Circles", "Arnold_Dumbbell_Press", "Around_The_Worlds", "Atlas_Stone_Trainer", "Atlas_Stones", "Axle_Deadlift", "Back_Flyes_-_With_Bands", "Backward_Drag", "Backward_Medicine_Ball_Throw", "Balance_Board", "Ball_Leg_Curl", "Band_Assisted_Pull-Up", "Band_Good_Morning", "Band_Good_Morning_(Pull_Through)", "Band_Hip_Adductions", "Band_Pull_Apart", "Band_Skull_Crusher", "Barbell_Ab_Rollout", "Barbell_Bench_Press_-_Medium_Grip", "Barbell_Curl", "Barbell_Deadlift", "Barbell_Full_Squat", "Barbell_Glute_Bridge", "Barbell_Guillotine_Bench_Press", "Barbell_Hack_Squat", "Barbell_Hip_Thrust", "Barbell_Incline_Shoulder_Raise", "Barbell_Lunge", "Barbell_Rear_Delt_Row", "Barbell_Rollout_from_Bench", "Barbell_Seated_Calf_Raise", "Barbell_Shoulder_Press", "Barbell_Shrug", "Barbell_Shrug_Behind_The_Back", "Barbell_Side_Bend", "Barbell_Side_Split_Squat", "Barbell_Squat", "Barbell_Step_Ups", "Barbell_Walking_Lunge", "Battling_Ropes", "Behind_Head_Chest_Stretch", "Bench_Dips", "Bench_Jump", "Bench_Press_-_Powerlifting", "Bench_Sprint", "Bent-Arm_Barbell_Pullover", "Bicycling"]

# Creamos un diccionario para almacenar los datos de todos los ejercicios
all_exercises_data = {}

# Recorremos la lista de nombres de ejercicios
for exercise_name in exercise_names:
    # Construimos la URL completa para el JSON del ejercicio actual
    exercise_url = base_url + f"{exercise_name}/exercise.json"

    # Realizar una solicitud GET para obtener el contenido JSON
    response = requests.get(exercise_url)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Analizar el contenido JSON y almacenarlo en el diccionario
        exercise_data = json.loads(response.text)
        all_exercises_data[exercise_name] = exercise_data
    else:
        print(f"No se pudo obtener el ejercicio {exercise_name}")

# Guardar todos los ejercicios en un solo archivo JSON
with open("all_exercises.json", "w") as json_file:
    json.dump(all_exercises_data, json_file, indent=4)

print("Ejercicios descargados y combinados en all_exercises.json")
