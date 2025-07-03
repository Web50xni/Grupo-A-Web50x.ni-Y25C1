def anuncio(func):
    def wrapper(param):
        print("La funcion se va a ejecutar")
        func(param)
        print("Funcion finalizada")
    return wrapper

@anuncio
def saludar(nombre):
    print(f"Hola, soy {nombre}")

saludar("Juanito")

