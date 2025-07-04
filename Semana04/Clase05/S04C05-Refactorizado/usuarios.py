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
        3.2. método <mostrar_detalle>
        3.3. método <registrar_producto>

    4. Clase <Sistema>
        4.1. Lista de productos.
        4.2. Método <mostrar_productos> 
"""
from utils import validar_entrada, registrar_producto


class Usuario:
    def __init__(self, nombre, correo, contrasena):
        self.__nombre = nombre
        self.__correo = correo
        self.__contrasena = contrasena

    def mostrar_info(self):
        print(f"Nombre: {self._Usuario__nombre} | Correo: {self._Usuario__correo}")

    # Se elimina el método verificar contraseña, ya que se validó en el módulo utils.py con la función validar_entrada
    """def verificar_contrasena(self, confirmacion):
        # Una forma más concisa sería: return self.__contrasena == confirmacion [Pero para especificar las instrucciones, se hace de la siguiente forma.]
        return True if confirmacion == self._Usuario__contrasena else False"""

# Crear clases que heredan (tipos de usuario)
class Cliente(Usuario):
    # No obtiene parámetros adicionales, sólo tiene permitido más métodos
    def __init__(self, nombre, correo, contrasena):
        super().__init__(nombre, correo, contrasena)

class Producto:
    def __init__(self, id, nombre, precio, descripcion):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

    def mostrar_detalle(self): 
        print(f"Producto: {self.nombre} | Descripcion: {self.descripcion} | su precio: {self.precio} | su id: {self.id}")

    def registrar_producto(self, objeto_sistema):
        objeto_sistema.productos.append({"id": self.id})


# Registra productos y usuarios
class Sistema:
    def __init__(self):
        self.productos = []

    def mostrar_productos(self):
        if self.productos:
            for producto in self.productos:
                print(producto)
        else:
            print("No hay productos registrados")




# Solicitar el registro del usuario

# --------- REFACTORIZADO -----------
sistema = Sistema()

nombre = validar_entrada("nombre")
correo = validar_entrada("correo")
contrasena = validar_entrada("contrasena")
confirmacion = validar_entrada("confirmacion", contrasena)

pepe = Cliente(nombre, correo, contrasena)
pepe.mostrar_info()

contador_id = 0

while True:
    opcion = input("¿Ingresar un producto? (s/n): | Listar productos (L): ")
    
    if opcion == 'n':
        # Para el bucle infinito
        print("--------- Programa Finalizado ---------")
        break
    elif opcion == 's':
        print("\n--------- Registrando Producto ---------")

        nombre_producto = registrar_producto("nombre")
        precio_producto = registrar_producto("precio")
        descripcion_producto = registrar_producto("descripcion")

        nuevo_producto = Producto(contador_id, nombre_producto, precio_producto, descripcion_producto)
        sistema.productos.append({"nombre": f"{nuevo_producto.nombre}", "precio": f"{nuevo_producto.precio}"})

        print("------- Nuevo Producto Creado --------")
        nuevo_producto.mostrar_detalle()
        
        
        contador_id += 1

    elif opcion == "L":
        print("--------- Productos Registrados ----------")
        sistema.mostrar_productos()
    else:
        # Solicitar entrada nuevamente. 
        continue
