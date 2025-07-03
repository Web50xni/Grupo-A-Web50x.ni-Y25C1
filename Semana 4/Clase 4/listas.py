tasks = []

print("Escribe 3 tareas que tienes que hacer hoy:")
for i in range(3):
    task = input(f"Tarea {i + 1}: ")
    tasks.append(task)

print("\nTus tareas para hoy son:")
for task in tasks:
    print(f"- {task}")


