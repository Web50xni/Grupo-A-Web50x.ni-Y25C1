# Funciones de utilidad

# 1. Refactorizar (un poco XD) la forma de obtener inputs del usuario
def validar_entrada(dato, contrasena=None):
    while True:
        
        entrada = input(f"Ingrese su {dato}: ")
        
        if not entrada:
            # Omitir que se elecuten los demás condicionales para ahorrar tiempo.
            continue

        if dato == "nombre":
            return entrada
        # Establecer correo
        elif dato == "correo" and "@" in entrada and "." in entrada:
            return entrada
        # Etableciendo contraseña
        elif dato == "contrasena" and len(entrada) > 5:
            return entrada
        # Validación de contraseña
        elif dato == "confirmacion":
            if entrada == contrasena:
                return entrada
        else:
            # Si el dato no fue válido, solicitar nuevamente
            continue

def registrar_producto(dato):
    while True:
        entrada = input(f"Ingrese {dato} de producto: ")

        if not entrada:
            continue

        if dato == "nombre":
            return entrada
        elif dato == "precio":
            # Uso de excepción
            try:
                return float(entrada)
            # Si no se puede parsear el tipo de dato a entero, repetir la entrada del usuario
            except ValueError:
                continue
        elif dato == "descripcion":
            return entrada
        else:
            continue