# Diseña un sistema en python que permita gestionar un cliente y los productos que ingresa.
"""
Requisitos:
    1. Clase base <Usuario>
        1.1. Atributos privados: <nombre>, <correo>, <contraseña>
        1.2. Métodos: <constructor>, <mostrar_info> (menos password), <verificar_contraseña> (valida contraseña ingresada)
    
    2. Clases que heredan de <Usuario>
        2.2. <cliente>: puede editar su perfil y ver productos.
    
    3. Clase <Producto>
        3.1. id, nombre, precio, descripcion
        3.2 método <mostrar_detalle>
        3.3. método <registrar_producto>

    4. Clase <Sistema>
        4.1. Lista de productos.
        4.2. Método <mostrar_productos>
"""
#


class Usuario:
    def __init__(self, nombre, correo, contrasena):
        self.__nombre = nombre
        self.__correo = correo
        self.__contrasena = contrasena

    def mostrar_info(self):
        print(f"Nombre: {self._Usuario__nombre} | Correo: {self._Usuario__correo}")

    def verificar_contrasena(self, confirmacion):
        # Una forma más concisa sería: return self.__contrasena == confirmacion [Pero para especificar las instrucciones, se hace de la siguiente forma.]
        return True if confirmacion == self._Usuario__contrasena else False

# Solicitar el registro del usuario

# --------- REFACTORIZAR -----------

while True:
    nombre = input("Ingrese su nombre de usuario: ")
    if nombre:
        break
while True:
    correo = input("Ingrese su correo: ")
    if correo:
        break
while True:
    contrasena = input("Digite su contraseña: ")
    if contrasena:
        break


# Una función que obtenga la entrada del usuario y la asigne a la variabe

# Crear objeto con los datos del usuario 
usuario1 = Usuario(nombre, correo, contrasena)

print("---------- Confirmación de contraseña -----------")

while True:
    confirmacion = input("Ingrese la contraseña: ")

    if usuario1.verificar_contrasena(confirmacion):
        # Si retornó True, las contraseñas son iguales. No hace falta continuar el ciclo
        break


# imprimir datos en consola (atributos privados)