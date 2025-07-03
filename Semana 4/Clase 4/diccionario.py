grades = {
    "Juan": 85,
    "María": 92,
    "Carlos": 78
}

name = input("Ingresa el nombre del estudiante: ")
if name in grades:
    print(f"La calificación de {name} es {grades[name]}")
else:
    print("Ese estudiante no está registrado.")